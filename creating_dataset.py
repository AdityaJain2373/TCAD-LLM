from modifying_prompts import modified_prompt
from modifying_sprocess import get_data
import json

dataset_list = []

tt = [1,5,5,2,12]
modified_codes = []
for j in range(5):
    t2 = tt[:]
    hehehaha = []
    for i in range(1,101):
        t2[j] = i
        value = get_data(*t2)
        hehehaha.append(value)
    modified_codes.extend(hehehaha)

for prompt,code in zip(modified_prompt,modified_codes):

    formatted_instance = f"<s>[INST] {prompt} [/INST] {code} </s>"

    dataset_list.append(formatted_instance)

print(len(dataset_list))


def parse_instance(instance):
    
    parts = instance.split("[/INST]")
    prompt = parts[0].replace("<s>[INST]", "").strip() if len(parts) > 0 else ""
    code = parts[1].strip() if len(parts) > 1 else ""
    return {"prompt": prompt, "code": code}

structured_dataset = [parse_instance(instance) for instance in dataset_list]

with open('dataset.json', 'w') as file:
    json.dump(structured_dataset, file, indent=4)

print("Dataset saved successfully!")
