import sys
import argparse
try:
    from .orchestrator import StrixDuoOrchestrator
    from .gitlab_reporter import GitLabReporter
except ImportError:
    from strix_duo.orchestrator import StrixDuoOrchestrator
    from strix_duo.gitlab_reporter import GitLabReporter

def main():
    parser = argparse.ArgumentParser(description="Strix-Duo QA: Autonomous DevSecOps Testing Engine for GitLab")
    parser.add_argument("--target", default="http://localhost:8000", help="Target application URL")
    parser.add_argument("--repo", default=".", help="Local repository path")
    parser.add_argument("--mr-id", default=None, help="GitLab Merge Request ID")
    parser.add_argument("--output", default="gitlab_qa_report.md", help="Output Markdown report path")
    parser.add_argument("--fail-on-critical", action="store_true", default=True, help="Exit with code 1 if critical/high bugs found")

    args = parser.parse_args()

    print(f"🚀 Initializing Strix-Duo QA Engine...")
    print(f"🎯 Target: {args.target}")
    print(f"📂 Analyzing Repository & API Contracts via REA & Strix...")

    orchestrator = StrixDuoOrchestrator(target_url=args.target, repo_path=args.repo)
    summary = orchestrator.execute_pipeline_audit(mr_id=args.mr_id)

    report_md = GitLabReporter.render_markdown(summary)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report_md)

    print(f"\n✅ Audit complete! Discovered {summary.total_findings} findings.")
    print(f"📄 Report written to: {args.output}")

    if not summary.passed and args.fail_on_critical:
        print(f"\n❌ Pipeline Gate: Critical or High vulnerabilities detected! Exiting with 1.")
        sys.exit(1)
    else:
        print(f"\n🎉 Pipeline Gate: Passed!")
        sys.exit(0)

if __name__ == "__main__":
    main()
