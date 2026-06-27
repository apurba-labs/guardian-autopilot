from src.agents.parser_agent import ParserAgent
from src.agents.investigation_agent import InvestigationAgent
from src.agents.decision_agent import DecisionAgent
from src.agents.report_agent import ReportAgent


class GuardianOrchestrator:
    """Coordinates the Guardian Autopilot workflow."""

    def __init__(self, provider):
        self.parser = ParserAgent(provider)
        self.investigator = InvestigationAgent(provider)
        self.decision = DecisionAgent(provider)
        self.report = ReportAgent()

    def run(self, incident):
        incident = self.parser.run(incident)
        incident = self.investigator.run(incident)
        incident = self.decision.run(incident)
        incident = self.report.run(incident)

        return incident