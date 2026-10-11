"""Unit test suite for Strix-Duo QA engine."""
import unittest
from strix_duo.models import VerificationFinding, Severity, FindingCategory
from strix_duo.orchestrator import StrixDuoOrchestrator
from strix_duo.gitlab_reporter import GitLabReporter

class TestStrixDuoQA(unittest.TestCase):
    def setUp(self):
        self.orchestrator = StrixDuoOrchestrator(
            target_url="https://example.com",
            repo_path="/dummy/path"
        )

    def test_execute_pipeline_audit_returns_findings(self):
        summary = self.orchestrator.execute_pipeline_audit()
        self.assertIsNotNone(summary)
        self.assertGreaterEqual(summary.total_findings, 1)
        self.assertEqual(len(summary.findings), summary.total_findings)

    def test_finding_severities_and_categories(self):
        summary = self.orchestrator.execute_pipeline_audit()
        for f in summary.findings:
            self.assertIn(f.severity, [Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW])
            self.assertIn(f.category, [FindingCategory.SECURITY, FindingCategory.CONTRACT_DRIFT, FindingCategory.REGRESSION, FindingCategory.PERFORMANCE])
            self.assertTrue(bool(f.title))
            self.assertTrue(bool(f.poc_script))
            self.assertTrue(bool(f.remediation_patch))

    def test_markdown_report_formatting(self):
        summary = self.orchestrator.execute_pipeline_audit(mr_id="MR-102")
        report = GitLabReporter.render_markdown(summary)
        self.assertIn("Strix-Duo QA & Security Gate Report", report)
        self.assertIn("Discovered Vulnerabilities & Proofs of Concept", report)
        self.assertIn("Automated GitLab Duo Fix Patch", report)
        self.assertIn("MR-102", report)

if __name__ == "__main__":
    unittest.main()
