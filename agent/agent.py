from llm.intent_router import IntentRouter

from tools import ActionPlanGeneratorWrite
from tools import ActionPlanGenerator


class Agent:

    def __init__(self):
        self.intent_router = IntentRouter()

    def handle_query(self, user_query: str):

        intent = self.intent_router.detect_intent(user_query)

        print("Detected intent:", intent)

        if intent == "CREATE":
            return ActionPlanGeneratorWrite().run(user_query)

        if intent == "UPDATE":
            return ActionPlanGeneratorWrite().run(user_query)

        if intent == "SEARCH":
            return ActionPlanGenerator().run(user_query)

        if intent == "HELP":
            return "Help RAG flow will be executed"

        return "Unable to understand the request."
