import openai

def invoke_llm(prompt):
    # Set up the OpenAI API client
    openai.api_key = 'your-api-key'

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response['choices'][0]['message']['content']

# Example usage
if __name__ == '__main__':
    prompt = 'What is the capital of France?'
    response = invoke_llm(prompt)
    print(response)