# import openai module
from openai import OpenAI
# using openai subscription api_key 
ashu_apiKey = ""
# Initializing openai with key 
ashu_api_client = OpenAI(api_key=ashu_apiKey)

# doing query with fine tuned model 
ashu_model_response = ashu_api_client.chat.completions.create(
    model="ft:gpt-4o-mini-2024-07-18:delvex:ashu-modelsarcastic-openaicode:As2elBnD",
    messages=[
        {"role": "system", "content": "Ashutoshh is a factual chatbot that is also sarcastic."},
        {"role": "user", "content": "i think i can calculate numbers faster than super computer ?"}
    ]
)
# print response
#print(ashu_model_response)
# only response to be printed
print(ashu_model_response.choices[0].message.content)