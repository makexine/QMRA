import re
import json
txt_file='medium_instr_goal.txt'
json_file='medium_instr_goal.jsonl'
with open(txt_file, 'r', encoding="utf-8") as f:
    data_set = f.read().strip()
sections = re.split(r'\n\s*\n', data_set)[:]

json_data=[]
for k,line in enumerate(sections):
    data={}
    a=line.split("\n")
    data['id']=k
    data['question']=a[0][13:]
    data['answer']=a[1][6:]
    json_data.append(data)

with open(json_file, 'w', encoding="utf-8") as f:
    for ex in json_data:
        json.dump(ex, f, ensure_ascii=False)
        f.write("\n")
print(f"Saved results to {json_file}")
