import google.generativeai as genai

API_KEY = ""
genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-2.5 flash")

chat = model.start_chat()

print("Chat started. Type 'exit' to end the chat.")

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Chat ended.")
        break  # Exit the loop when user types 'exit'
    
    if user_input:
        response = chat.send_message(user_input)
        print(f"ChatGPT: {response.text}")  # Print the response from the model