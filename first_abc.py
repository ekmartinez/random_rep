import openai

openai.api_key = "key"
def gpt(prompt):
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
            ) 

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = gpt(user_input)
        print("Helper: ", response)
