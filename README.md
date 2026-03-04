
# 🧠 Ollama Multi-Model Web Chat

A simple **local AI chat application** that runs multiple LLM models using **Ollama** with a **FastAPI backend** and a lightweight web interface.

This project allows users to chat with different AI models directly from a browser while running everything locally.

No external APIs required.



# 🚀 Features

• Run **multiple local LLM models**
• **Model selection dropdown**
• **Real-time streaming responses**
• **Conversation memory support**
• **FastAPI backend**
• **Ollama local inference**
• Simple and lightweight UI



# 🧱 Project Structure
```
ollama-multi-model-chat/

backend.py
requirements.txt
README.md

chatbot/
    index.html
```


# 🐍 Python Requirements

This project requires **Python 3.10 or higher**.

Check your Python version:

```
python3 --version
```

Example output:

```
Python 3.12.3
```



# 📦 Install Python (if not installed)

### Ubuntu / Debian

```
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

### MacOS (Homebrew)

```
brew install python
```

### Windows

Download Python from:

https://www.python.org/downloads/

Make sure to enable:

```
Add Python to PATH
```


# 🧠 Install Ollama
Install Ollama:

```
curl -fsSL https://ollama.com/install.sh | sh
```

Start Ollama server:

```
ollama serve
```

Ollama runs on:

```
http://localhost:11434
```


# 🤖 Download AI Models

Pull the models you want to use:

```
ollama pull phi3:mini
ollama pull gemma:2b
ollama pull qwen2.5:3b
ollama pull mistral
ollama pull llama3:8b
ollama pull deepseek-r1:8b
```

Check installed models:

```
ollama list
```

Example output:

```
phi3:mini
gemma:2b
qwen2.5:3b
mistral
llama3:8b
deepseek-r1:8b
```


# 📥 Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/ollama-multi-model-chat.git
cd ollama-multi-model-chat
```


# 🧪 Create Virtual Environment

Create environment:

```
python3 -m venv venv
```

Activate it:

### Linux / Mac

```
source venv/bin/activate
```

### Windows

```
venv\Scripts\activate
```

You should now see:

```
(venv)
```


# 📚 Install Dependencies

Install required packages:

```
pip install -r requirements.txt
```

Dependencies include:

* fastapi
* uvicorn
* requests


# ▶️ Run the Server

Start the FastAPI backend:

```
uvicorn backend:app --host 0.0.0.0 --port 8000
```

You should see:

```
Uvicorn running on http://0.0.0.0:8000
```


# 🌐 Open the Web Interface

Open your browser and go to:

```
http://localhost:8000
```

If running on **AWS EC2**, open:

```
http://YOUR_PUBLIC_IP:8000
```

Make sure **port 8000 is open in the security group**.


# ⚙️ How It Works
```
Browser UI
     ↓
FastAPI Backend
     ↓
Ollama API
     ↓
Local AI Model
```

The backend sends requests to Ollama:

```
http://localhost:11434/api/generate
```

Ollama then runs the selected LLM model and streams the response back to the browser.


# 🧠 Supported Models

This project works with many Ollama models including:

| Model       | Size |
| ----------- | ---- |
| Phi-3 Mini  | ~4B  |
| Gemma 2B    | ~2B  |
| Qwen 2.5    | ~3B  |
| Mistral     | ~7B  |
| Llama 3     | ~8B  |
| DeepSeek R1 | ~8B  |


# 🧩 Future Improvements

Possible future features:

• ChatGPT-style UI
• Multi-model comparison mode
• Chat history sidebar
• Docker deployment
• Authentication system
• Model performance dashboard


# 📜 License

MIT License



# why i bulit it

Built for experimenting with **local LLMs** ended up knowing **ollama** and **fastapi**


