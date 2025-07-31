import requests

API_KEY = "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"
url = "https://api.groq.com/openai/v1/chat/completions"

question = input("Ask your Linux question: ")

payload = {
    "model": "llama3-70b-8192",
    "messages": [{"role": "user", "content": question}]
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json()["choices"][0]["message"]["content"])
