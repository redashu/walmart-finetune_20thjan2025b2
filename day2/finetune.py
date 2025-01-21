# importing all required modules
from openai import OpenAI
import json
from collections import defaultdict
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

# create instance of OpenAI
# data format validation 
# Format error checks
format_errors = defaultdict(int)

for ex in dataset:
    if not isinstance(ex, dict):
        format_errors["data_type"] += 1
        continue
        
    messages = ex.get("messages", None)
    if not messages:
        format_errors["missing_messages_list"] += 1
        continue
        
    for message in messages:
        if "role" not in message or "content" not in message:
            format_errors["message_missing_key"] += 1
        
        if any(k not in ("role", "content", "name", "function_call", "weight") for k in message):
            format_errors["message_unrecognized_key"] += 1
        
        if message.get("role", None) not in ("system", "user", "assistant", "function"):
            format_errors["unrecognized_role"] += 1
            
        content = message.get("content", None)
        function_call = message.get("function_call", None)
        
        if (not content and not function_call) or not isinstance(content, str):
            format_errors["missing_content"] += 1
    
    if not any(message.get("role", None) == "assistant" for message in messages):
        format_errors["example_missing_assistant_message"] += 1

if format_errors:
    print("Found errors:")
    for k, v in format_errors.items():
        print(f"{k}: {v}")
else:
    print("No errors found")