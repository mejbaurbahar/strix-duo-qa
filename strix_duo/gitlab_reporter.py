"""
GitLab Reporter
Generates GitLab-compatible Markdown reports, MR discussions, and CI badge summaries.
"""
from .models import ScanSummary

class GitLabReporter:
    @staticmethod
    def render_markdown(summary: ScanSummary) -> str:
        status_badge = "🟢 **PASSED**" if summary.passed else "🔴 **FAILED (Security Gate Triggered)**"

        md = [
            f"# 🛡️ Strix-Duo QA & Security Gate Report",
            f"",
            f"**Evaluation Status:** {status_badge}  ",
            f"**Target System:** `{summary.target}`  ",
            f"**Merge Request:** `{summary.mr_id or 'Local Run'}`  ",
            f"",
            f"| Total Findings | Critical | High | Medium | Low |",
            f"| :---: | :---: | :---: | :---: | :---: |",
            f"| **{summary.total_findings}** | **{summary.critical_count}** | **{summary.high_count}** | **{summary.medium_count}** | **{summary.low_count}** |",
            f"",
            f"---",
            f"## Discovered Vulnerabilities & Proofs of Concept",
            f""
        ]

        for finding in summary.findings:
            md.extend([
                f"### [{finding.severity.value}] {finding.title}",
                f"",
                f"> **Category:** `{finding.category.value}` | **Confidence:** `{int(finding.confidence_score * 100)}%`",
                f"",
                f"{finding.description}",
                f"",
                f"**Location:** `{finding.file_path or 'Dynamic'}:{finding.line_number or 0}`",
                f""
            ])

            if finding.poc_script:
                md.extend([
                    f"#### 🧪 Verified Exploit Proof-of-Concept",
                    f"```bash",
                    f"{finding.poc_script}",
                    f"```",
                    f""
                ])

            if finding.remediation_patch:
                md.extend([
                    f"#### 🛠️ Automated GitLab Duo Fix Patch",
                    f"```diff",
                    f"{finding.remediation_patch}",
                    f"```",
                    f""
                ])

        return "\n".join(md)
