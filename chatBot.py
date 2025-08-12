import openai

openai.api_key = 'AIzaSyBHoO8Mf_zTf_apMUb5RBT_dNviWZBz0wg'

messages = [{"role": "system", "content": "You are an intelligent assistant."}]

while True:
    message = input("User: ")
    if message.lower() == "exit":
        print("Chat ended.")
        break  # Exit the loop when user types 'exit'
    
    if message:
        messages.append({"role": "user", "content": message})

        chat = openai.ChatCompletion.create(  # Correct method
            model="gemini-2.5 flash",  # Correct model
            messages=messages
        )

        reply = chat["choices"][0]["message"]["content"]  # Correct response extraction
        print(f"ChatGPT: {reply}")

        messages.append({"role": "assistant", "content": reply})  # Append response
