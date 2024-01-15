import os
import openai
openai.api_key = os.getenv('OPENAI_API_KEY')
# chat
# response = openai.Completion.create(
#   model="text-davinci-003",
#   # \n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\n
#   prompt="what are AutoGPT and GPT-4",
#   temperature=0.9,
#   max_tokens=150,
#   top_p=1,
#   frequency_penalty=0.0,
#   presence_penalty=0.6,
#   stop=[" Human:", " AI:"]
# )
# print(response['choices'][0]['text'])

#Q&A try to make it remember what is said ealier/api usauge
# \n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president o
while True:
    query = input('Send a message: ')
    if query == 'q':
        break
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="\n\n" + query + "\nA:",
      temperature=0, # higher value more creative, random
      echo=True,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      # stop=["\n"]
    )
    print(response['choices'][0]['text'])
# code generation
# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="\"\"\"\nprovide me the python code for system logging.\n\"\"\"\n",
#   temperature=0,
#   max_tokens=64,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0,
#   stop=["\"\"\""]
# )
# print(response.choices[0].text)

#code explaination
# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="source code\n\n\"\"\"\ndesciption\n1.",
#   temperature=0,
#   max_tokens=150,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0,
#   stop=["\"\"\""]
# )
# print(response.choices[0].text)