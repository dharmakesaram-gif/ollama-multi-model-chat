from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, StreamingResponse
import requests
import json

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"

CHAT_HISTORY = []
MAX_HISTORY = 10


@app.get("/")
def serve_index():
    return FileResponse("chatbot/index.html")


def build_prompt(user_message):

    prompt = ""

    for msg in CHAT_HISTORY:
        prompt += f"{msg['role'].upper()}: {msg['content']}\n"

    prompt += f"USER: {user_message}\nASSISTANT:"

    return prompt


def stream_ollama(model, prompt):

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }

    full_response = ""

    with requests.post(OLLAMA_URL, json=payload, stream=True) as r:

        for line in r.iter_lines():

            if not line:
                continue

            data = json.loads(line.decode())

            if "response" in data:

                token = data["response"]
                full_response += token
                yield token

    CHAT_HISTORY.append({"role": "assistant", "content": full_response})


@app.post("/chat")
async def chat(req: Request):

    body = await req.json()

    user_message = body.get("prompt")
    model = body.get("model")

    CHAT_HISTORY.append({
        "role": "user",
        "content": user_message
    })

    if len(CHAT_HISTORY) > MAX_HISTORY * 2:
        CHAT_HISTORY[:] = CHAT_HISTORY[-MAX_HISTORY * 2:]

    prompt = build_prompt(user_message)

    return StreamingResponse(
        stream_ollama(model, prompt),
        media_type="text/plain"
    )
