import openai as ai

# Set the API key
ai.api_key = "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"

# Set the model to use
model_engine = "davinci"

# Set the prompt
prompt = "Write a short story about a robot that has feelings"

# Generate text
completion = ai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=1)

# Print the generated text
print(completion.text)
