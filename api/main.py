from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from protocol import MCPServer

app = FastAPI()
mcp = MCPServer()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    response = mcp.handle(user_input)
    return {"response": response}
