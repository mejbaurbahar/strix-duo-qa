from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Dict, Any

class Severity(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"

class FindingCategory(str, Enum):
    SECURITY = "SECURITY"
    REGRESSION = "REGRESSION"
    CONTRACT_DRIFT = "CONTRACT_DRIFT"
    PERFORMANCE = "PERFORMANCE"
    FUNCTIONAL = "FUNCTIONAL"

@dataclass
class VerificationFinding:
    id: str
    title: str
    category: FindingCategory
    severity: Severity
    description: str
    file_path: Optional[str] = None
    line_number: Optional[int] = None
    poc_script: Optional[str] = None
    remediation_patch: Optional[str] = None
    confidence_score: float = 0.95
    evidence: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ScanSummary:
    target: str
    mr_id: Optional[str] = None
    total_findings: int = 0
    critical_count: int = 0
    high_count: int = 0
    medium_count: int = 0
    low_count: int = 0
    findings: List[VerificationFinding] = field(default_factory=list)
    passed: bool = True
