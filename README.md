# LLaMA-3.2 Chatbot Multi-Language-AI-Assistant

## Chatbot GUI Screenshot

![Chatbot GUI](Screenshot%20of%20the%20Chatbot%20GUI.jpg)


## Overview
This project is a locally hosted chatbot that utilizes the **Llama 3.2 model from Ollama**. The backend is powered by **FastAPI**, handling chat requests and processing responses, while the frontend is built using **Streamlit** for an interactive user experience.

## Features
- **Locally Hosted Model**: No API integration; the Llama 3.2 model runs directly on your system.
- **FastAPI Backend**: Processes chat requests and returns responses.
- **Streamlit Frontend**: Provides an intuitive and user-friendly chat interface.
- **Multilingual Support**: Allows users to communicate in multiple languages.

## Installation & Setup

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- Ollama (for Llama 3.2 model) → [Install Ollama](https://ollama.ai/)
- FastAPI & Uvicorn (for the backend)
- Streamlit (for the frontend)

### Step 1: Clone the Repository
```bash
git clone https://github.com/abdullahzunorain/LLaMA_3.2_Chatbot---Multi_Language_AI_Assistant.git
cd LLaMA_3.2_Chatbot---Multi_Language_AI_Assistant
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate  # (to activate the env)
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Download & Set Up Llama 3.2 Model
Ensure Ollama is installed and run the following command to download the model:
```bash
ollama pull llama3.2
```

### Step 5: Run the FastAPI Backend
```bash
uvicorn api:app --reload
```
This will start the FastAPI server at `http://localhost:8000`.

### Step 6: Run the Streamlit Frontend
```bash
streamlit run app.py
```
This will launch the chat interface in your browser.

## Project Structure
```
📁 project_directory
│── 📄 app.py          # FastAPI backend for processing chat requests
│── 📄 app.py         # Streamlit frontend for user interaction
│── 📄 requirements.txt # Python dependencies
│── 📄 test_api.py     # Unit tests for FastAPI endpoints
|__ 📄 test_multilingual.py # used for to test the multilanguage capabilities
└── 📄 README.md       # Project documentation
```

## Usage
1. Open the Streamlit chat interface in your browser.
2. Enter a message and receive responses from the Llama 3.2 model.
3. The conversation history remains visible throughout the session.

## Testing
Run unit tests for the FastAPI backend using:
```bash
pytest test_api.py
pytest test_multilingual.py
```

## Design Decisions
- **FastAPI for Backend**: Chosen for its speed, asynchronous capabilities, and easy integration with modern applications.
- **Streamlit for Frontend**: Provides a lightweight and interactive UI with minimal setup.
- **Local Model Hosting**: Avoids API dependencies, ensuring complete control over the chatbot's performance and availability.
- **Session-Based Conversations**: Allows users to maintain context within a session for a more interactive experience.

## Future Improvements
- Enhance the UI with more styling options.
- Implement advanced session management for multi-user support.
- Improve error handling and logging for better debugging.



