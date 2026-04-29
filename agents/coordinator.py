
from agents.extraction import ExtractionAgent
from agents.reasoning import ReasoningAgent
from agents.review import ReviewAgent
from utils.file_parser import parse_file

class CoordinatorAgent:
    def __init__(self):
        self.extractor = ExtractionAgent()
        self.reasoner = ReasoningAgent()
        self.reviewer = ReviewAgent()

    def run(self, file_path):
        text = parse_file(file_path)
        clauses = self.extractor.run(text)
        risks = self.reasoner.run(clauses)
        report = self.reviewer.run(clauses, risks)
        return report
