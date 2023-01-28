import openai
openai.api_key = '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'

model = 'text-davinci-003'

response = openai.Completion.create(
    prompt="How big is the moon?",
    model = model
)