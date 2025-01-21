# importing all required modules
from openai import OpenAI
import json

# location of data 
ashu_datapath = "/content/ashudataset.jsonl"
# verify that my dataset is having a valid jsonl format 
with open(ashu_datapath, 'r') as f:
    for line in f:
        try:
            json.loads(line)
        except json.JSONDecodeError as e:
            print(f"Invalid JSONL format: {e}")
            break

