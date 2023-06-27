import openai

# Set the API key
openai.api_key = "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"

# Set the model to use
model_engine = "davinci"

# Set the prompt
prompt = "Write a short story about a robot that has feelings"

# Generate text
completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)

# Print the generated text
print(completion.text)
