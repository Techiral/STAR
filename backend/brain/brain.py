from time import sleep
from rich import print
from os import environ
from dotenv import load_dotenv
import requests

rq = requests.session()
load_dotenv()
API = environ['HF_TOKEN']

URL = 'https://kaushikshresth12-kaushikbhaiyakaserver.hf.space/generate-text'

def format_prompt(message, custom_instructions=None):
    prompt = ""
    if custom_instructions:
        prompt += f"[INST] {custom_instructions} [/INST]"
    prompt += f"[INST] {message} [/INST]"
    return prompt
    print(prompt)
  
instructions_L1 = """
You are Decision Making Model.
which select 2 options give below:
-> 'Query' if the input is a question that chatbot should answer.
-> 'Automation' if the input is an instruction to open or close anything in computer. Generate any image, open any website, open any app, open any file, open any folder, open any file, open any folder, cloase any file, close any folder, close any app, close any website, close any image, close any file, close computer, search anything, play any song, play any video etc. (whatever task that chat bot can perform)
***The output should be only one word***
Example (1) : hello can you open chrome for me?
Example Output (1) : Automation
Example (2) : who is akshay kumar?
Example Output (2) : Query
"""

template_L1 = """#reply only one of them ["Automation", "Query"]
Input : *{prompt}*
Output : 
"""

instructions_L2="""Today is 15/03/2024.
You are Decision Making Model.
which select 2 options give below:
-> 'Before' if the information is before 07/02/2023. if the information is about who was or any past event. or any chat bot response. like anything which a chat bot can answer without knowing current events. 
-> 'After' if the information is after 07/02/2023. if the information is about who will be or any future event. or any present event. time, date, month, year, recent event or any event. for present and future event. if the question is about any person. example: who is Kaushik Shresth? or any other person.
***The output should be only one word***
Example (1) : who was akbar?
Example Output (1) : Before
Example (2) : who is currently working as ceo of microsoft?
Example Output (2) : After
Example (3) : how are you
Example Output (3) : Before
Example (4) : do you know quantum computing?
Example Output (4) : Before
Example (5) : aaj ka weather kya hai?
Example Output (5) : After
Example (6) : aaj ki news batao
Example Output (6) : After"""

template_L2 = """#reply only one of them ["After", "Before"]
Input : *{prompt}*
Output : 
"""

def Mixtral(prompt, instructions, temperature=0.1, max_new_toxen=2, top_p=0.95, repetition_penalty=1.0):
    data = {'prompt' : prompt,
            'instructions' : instructions,
            'api_key' : API,}
    response = rq.post(URL, json=data)
    response = response.json()['response']
    return response

def L1(prompt):
    global template_L1
    response:str = Mixtral(template_L1.format(prompt=prompt), 
                            instructions=instructions_L1)

    return response.strip()

def L2(prompt):
    global template_L2
    response:str = Mixtral(template_L2.format(prompt=prompt), 
                            instructions=instructions_L2)
    
    return response.strip()

def L1_X_L2(query):
    L1_response = L1(query)
    if L1_response == "Query":
        print("It is a query")
        L2_response = L2(query)
        print(L2_response)

    else:
        print("It is an Automation")

while True:
    print(L1_X_L2(input("Enter The Query : ")))