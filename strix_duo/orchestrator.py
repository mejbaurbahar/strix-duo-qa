"""
Strix-Duo Orchestrator
Coordinates REA contract analysis and Strix dynamic pentesting, compiling the final QA/Security verdict.
"""
from typing import List, Optional
from .models import ScanSummary, Severity
from .rea_engine import ReaEngine
from .strix_scanner import StrixScanner

class StrixDuoOrchestrator:
    def __init__(self, target_url: str = "http://localhost:8000", repo_path: str = "."):
        self.target_url = target_url
        self.repo_path = repo_path
        self.rea = ReaEngine(target_url, repo_path)
        self.strix = StrixScanner(target_url)

    def execute_pipeline_audit(self, endpoints: Optional[List[str]] = None, mr_id: Optional[str] = None) -> ScanSummary:
        if endpoints is None:
            endpoints = [
                "/api/v1/users/profile",
                "/api/v1/auth/login",
                "/admin/stats",
                "/api/v1/health"
            ]

        # 1. Run REA reverse engineering contract inspection
        contract_findings = self.rea.analyze_api_contracts(endpoints)

        # 2. Run Strix autonomous dynamic exploitation
        security_findings = self.strix.run_dynamic_pentest(endpoints)

        all_findings = contract_findings + security_findings

        summary = ScanSummary(
            target=self.target_url,
            mr_id=mr_id,
            total_findings=len(all_findings),
            critical_count=sum(1 for f in all_findings if f.severity == Severity.CRITICAL),
            high_count=sum(1 for f in all_findings if f.severity == Severity.HIGH),
            medium_count=sum(1 for f in all_findings if f.severity == Severity.MEDIUM),
            low_count=sum(1 for f in all_findings if f.severity == Severity.LOW),
            findings=all_findings,
            passed=(sum(1 for f in all_findings if f.severity in (Severity.CRITICAL, Severity.HIGH)) == 0)
        )

        return summary
