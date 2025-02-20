import streamlit as st
import requests

# Set up Streamlit page
st.set_page_config(page_title="Ollama AI Chatbot", page_icon="🤖", layout="wide")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 LLaMA 3.2 Chatbot - Multi-Language AI Assistant")

# Dropdown for language selection
selected_language = st.selectbox("Select Language", ["English", "Urdu", "French", "Spanish"])

# Map language names to codes
language_codes = {"English": "en", "Urdu": "ur", "French": "fr", "Spanish": "es"}
lang_code = language_codes[selected_language]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Send request to API
    api_url = "http://127.0.0.1:8000/chat"  # Update if API is deployed elsewhere
    payload = {
        "conversation_id": "12345",  # Unique session ID
        "messages": st.session_state.messages,
        "language": lang_code
    }

    try:
        api_response = requests.post(api_url, json=payload)
        
        if api_response.status_code == 200:
            bot_response = api_response.json()["response"]
        else:
            bot_response = f"Error: {api_response.json().get('detail', 'Could not fetch response.')}"
    
    except requests.exceptions.RequestException as e:
        bot_response = f"Error: Unable to connect to API ({str(e)})"

    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
