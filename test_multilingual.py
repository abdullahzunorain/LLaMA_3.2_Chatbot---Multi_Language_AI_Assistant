import ollama

# Define test prompts in different languages
test_prompts = {
    "English": "Hello, how are you?",
    "French": "Bonjour, comment ça va?",
    "Spanish": "Hola, ¿cómo estás?",
    # "Urdu": "آپ کیسے ہیں؟"
}

# Test each language
for lang, prompt in test_prompts.items():
    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
    print(f"\n{lang} Response:\n", response["message"]["content"])
