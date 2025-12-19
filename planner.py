class Planner:
    REQUIRED_FIELDS = ["age", "income", "occupation"]

    def plan(self, memory):
        missing = [f for f in self.REQUIRED_FIELDS if f not in memory]

        if missing:
            return {
                "action": "ASK_INFO",
                "fields": missing
            }

        return {"action": "CHECK_ELIGIBILITY"}
