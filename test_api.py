from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

#  Test 1: Successful chatbot response
def test_chat_response():
    response = client.post("/chat", json={
        "conversation_id": "test123",
        "messages": [{"role": "user", "content": "Hello"}],
        "language": "en"
    })
    assert response.status_code == 200
    assert "response" in response.json()

#  Test 2: Missing required fields (should return 422 Unprocessable Entity)
def test_missing_fields():
    response = client.post("/chat", json={})  # Empty request
    assert response.status_code == 422  # FastAPI handles missing fields as 422

#  Test 3: Empty messages list
def test_empty_messages():
    response = client.post("/chat", json={
        "conversation_id": "test123",
        "messages": [],
        "language": "en"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Messages cannot be empty."

#  Test 4: Message without 'role' or 'content' (should return 422 instead of 400)
def test_invalid_message_structure():
    response = client.post("/chat", json={
        "conversation_id": "test123",
        "messages": [{"content": "Hello"}],  # Missing 'role'
        "language": "en"
    })
    assert response.status_code == 422  # Adjusted to expect 422

#  Test 5: Empty message content
def test_empty_message_content():
    response = client.post("/chat", json={
        "conversation_id": "test123",
        "messages": [{"role": "user", "content": ""}],  # Empty message
        "language": "en"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Message content cannot be empty."

#  Test 6: Ollama API failure simulation (mocked)
def test_ollama_failure(mocker):
    mocker.patch("ollama.chat", side_effect=Exception("Ollama API is down"))

    response = client.post("/chat", json={
        "conversation_id": "test123",
        "messages": [{"role": "user", "content": "Hi"}],
        "language": "en"
    })
    assert response.status_code == 500
    assert "Internal Server Error" in response.json()["detail"]
