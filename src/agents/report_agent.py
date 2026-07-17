from src.models.incident import Incident, WorkflowState
from src.models.report import IncidentReport

ENTITY_DISPLAY_NAMES = {
    "<PRODUCTION_AWS_ACCESS_KEY>": "AWS Access Key",
    "<AWS_SECRET_KEY_PLACEHOLDER>": "AWS Secret Access Key",
    "<GITHUB_PAT_PLACEHOLDER>": "GitHub Personal Access Token",
    "<SLACK_BOT_PLACEHOLDER>": "Slack Bot Token",
}

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
        
        memory = incident.metadata.get("memory", {})

        history = memory.get("history", [])
        matched = memory.get("matched", False)
        count = memory.get("count", 0)
        
        incident.state = WorkflowState.COMPLETED
        
        if matched:
            repeated = sorted({
                ENTITY_DISPLAY_NAMES.get(entity, entity)
                for item in history
                for entity in item.get("entities", [])
            })

            indicators = "\n".join(f"• {item}" for item in repeated)

            historical_section = f"""
Historical Correlation
----------------------------------------
Correlation Status : MATCH FOUND
Previous Related Incidents : {count}

Repeated Indicators
{indicators}

Assessment
This incident shares indicators with previous investigations,
suggesting repeated credential exposure or an ongoing security issue.
""".strip()
        else:
            historical_section = """
Historical Correlation
----------------------------------------
Correlation Status : NONE
No previous related incidents found.
""".strip()
        
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
{incident.metadata.get("summary", incident.reasoning)}

Decision Summary
----------------------------------------
{incident.decision_reasoning}

Recommended Actions
----------------------------------------
{recommendations}

{historical_section}
""".strip(),
        )
        
        incident.metadata["report"] = report.model_dump()

        return incident