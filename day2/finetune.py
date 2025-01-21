# importing all required modules
from openai import OpenAI
import json

# location of data 
ashu_datapath = "/content/ashudataset.jsonl"
# creating list 
dataset = []
# verify that my dataset is having a valid jsonl format 
with open(ashu_datapath, 'r') as f:
    for line in f:
        try:
            data = json.loads(line)
            dataset.append(data)
        except json.JSONDecodeError as e:
            print(f"Invalid JSONL format: {e}")
            break

# check basic info 
# length of dataset 
if len(dataset) > 10 :
  print("number of examples we have in dataset is ",len(dataset))
  print("we can use this data for fine tuning")
else : 
  print("we need more data for fine tuning OR minimum 10 samples as per GPT")
