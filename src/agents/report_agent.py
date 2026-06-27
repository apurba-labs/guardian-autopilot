from src.models.incident import Incident, WorkflowState
from src.models.report import IncidentReport


class ReportAgent:
    """Generates the final human-readable incident report."""

    def run(self, incident: Incident) -> Incident:
        findings = "\n".join(
            f"• {item.type} ({item.provider})"
            for item in incident.findings
        )

        recommendations = "\n".join(
            f"✓ {item}"
            for item in incident.recommendation
        )
        
        incident.state = WorkflowState.COMPLETED
        
        report = IncidentReport(
            title="Guardian Incident Report",
            summary=f"Overall Risk: {incident.risk.value}",
            content=f"""
Incident ID
----------------------------------------
{incident.id}

Workflow State
----------------------------------------
{incident.state.value}

Decision
----------------------------------------
{incident.decision.value if incident.decision else "N/A"}

Approval Required
----------------------------------------
{"YES" if incident.approval_required else "NO"}

Findings
----------------------------------------
{findings}

Investigation Summary
----------------------------------------
{incident.reasoning}

Decision Summary
----------------------------------------
{incident.decision_reasoning}

Recommended Actions
----------------------------------------
{recommendations}
""".strip(),
        )
        
        incident.metadata["report"] = report.model_dump()

        return incident