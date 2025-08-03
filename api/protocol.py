from model import mock_llm
from context import ContextMemory

class MCPServer:
    def __init__(self):
        self.context = ContextMemory()

    def handle(self, user_input: str) -> str:
        ctx = self.context.get_context(user_input)
        full_prompt = f"{ctx}User: {user_input}\nAI:"
        response = mock_llm(full_prompt)
        self.context.update(user_input, response)
        return response
