from openai import OpenAI

client = OpenAI(
    api_key="sk-aKGeEFMZB0gXEcE51FTc0A",
    base_url="http://pluto/v1/",
    timeout=120,
)

try:
    response = client.chat.completions.create(
        model="GPT-OSS-120B",
        messages=[
            {"role": "system", "content": "You are a helpful assistant!"},
            {"role": "user", "content": "Say hello in one short sentence."}
        ],
        max_tokens=20,
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(type(e).__name__)
    print(repr(e))