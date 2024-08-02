import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-jO87jCvYeFVqn8YN3bu1T3BlbkFJOk3KHLXSPyYwVNh7BC6h'

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine = "gpt-3.5-turbo",
            prompt = prompt,
            max_tokens = 1500,
            n = 1,
            stop = None,
            temperature = 0.7,
        )
        message = response.choices[0].text.strip()
        return message
    except Exception as e:
        return str(e)

def chat():
    print("Welcome to the OpenAI Chatbot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

if _name_ == "_main_":
    chat()
