"""
HTTP Webhook & Health Service for Google Cloud Run / Cloud Run deployment.
Accepts GitLab webhook triggers for autonomous merge request audits.
"""
import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from strix_duo.orchestrator import StrixDuoOrchestrator
from strix_duo.gitlab_reporter import GitLabReporter

class StrixDuoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/health", "/_health"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "service": "strix-duo-qa",
                "status": "online",
                "version": "1.0.0",
                "cloud": "Google Cloud Run",
                "gitlab_duo_agent_ready": True
            }
            self.wfile.write(json.dumps(response, indent=2).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/webhook/gitlab":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)
            
            try:
                payload = json.loads(post_data.decode("utf-8")) if post_data else {}
            except Exception:
                payload = {}

            target = payload.get("target_url", "https://httpbin.org")
            mr_id = str(payload.get("mr_id", "CI-TRIGGERED"))

            orchestrator = StrixDuoOrchestrator(target_url=target)
            summary = orchestrator.execute_pipeline_audit(mr_id=mr_id)
            report_md = GitLabReporter.render_markdown(summary)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "status": "success",
                "audit_passed": summary.passed,
                "total_findings": summary.total_findings,
                "critical": summary.critical_count,
                "high": summary.high_count,
                "report_preview": report_md[:300] + "..."
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def run(port: int = 8080):
    server_address = ("", port)
    httpd = HTTPServer(server_address, StrixDuoHandler)
    print(f"🚀 Strix-Duo Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    run(port)
