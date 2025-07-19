from openai import OpenAI

client= OpenAI(
    api_key="Your_api_key",
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_input= input("you: ")
    if user_input == "quit":
        print("bot: Goodbye!")
        break
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "you are a medical bot, provide information only related to medical"}, #You can change this to any role
            {"role": "user", "content": user_input} 
        ]
    )
    print("Bot:, ", response.choices[0].message.content)