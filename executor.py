from eligibility import check_eligibility
from scheme_retriever import retrieve_scheme

class Executor:
    def execute(self, memory):
        schemes = check_eligibility(memory)
        return retrieve_scheme(schemes)
