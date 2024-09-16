import sys
sys.path.append("..")
import torch
import json
import matplotlib.pyplot as plt
import zhipuai



def get_ctxs_em(file_path):
    ctxs=[]
    query=[]
    with open(file_path, "r") as fin:
        for k, example in enumerate(fin):
            example = json.loads(example)
            cts=[]
            for ct in example["ctxs"]:
                if "id" in ct:
                    cts.append(ct)
            ctxs.append(cts)
            query.append(example["question"])
    return ctxs,query

def get_llm_chatglm(evi,query):
    # your api key
    #print("llm!")
    zhipuai.api_key = "1b63a16cb13959ca1abf3a3fededa2a2.IYPOsV0KXyuXyle7"
    ins='Pretend that you are a language learning assistant. Are the following statements similar with the question? Just Say True if they are; otherwise just say False. Only output one word.'
    prompt=ins+'\n'+evi+'\n'+query
    response = zhipuai.model_api.invoke(
            model="chatglm_turbo",
            prompt=[{"role": "user", "content": prompt}],
            top_p=0.7,
            temperature=0.9,
        )
    return response['data']['choices'][0]['content']
def get_llm_chatglm_0(evi,query): #思维链表达VMD
    # your api key
    #print("llm!")
    zhipuai.api_key = "36d848bfbccdd993f40352f4e48bf43c.VRyq7foZfDFDE29t"
    ins_0='You are a cautious language assistant.'
    ins_1='###Here are some language rules:\n'
    rule_1='If the two sentences can be identified as similar, then the subjects, verbs and objects of two sentences are similar. Be especially mindful of verb phrases that appear similar but actually have opposite meanings which make sentences dissimilar. '
    rule_2= 'If the two sentences can be identified as similar, then the adverbials and attributives of two sentences are similar.'
    ins_3 = '###Are the following statements similar with the question? Just Say True if they are; otherwise just say False. Only output one word.'
    #ins_2=rule_1+'\n'+rule_2
    ins_2=rule_1
    prompt=ins_0+'\n'+ins_1+'\n'+ins_2+'\n\n'+ins_3+'\n'+evi+'\n'+query

    response = zhipuai.model_api.invoke(
            model="chatglm_turbo",
            prompt=[{"role": "user", "content": prompt}],
            top_p=0.7,
            temperature=0.9,
        )
    return response['data']['choices'][0]['content']

def context_relation(t_context_result,f_context_result):
    r=[]
    for idx in t_context_result['id']:
        for idy in f_context_result['id']:
            r.append((idx,idy))
    return r

def get_enquery(file_path):
    ctxs,query=get_ctxs_em(file_path)
    unsim_s=[]
    error_d=[]
    for i in range(len(ctxs)):
        t_context_result={"id":[],"result":[]}
        f_context_result={"id":[],"result":[]}
        evidences = ["[{}] ".format(i+1) + ctx["title"]+"\n" + ctx["text"] for i, ctx in enumerate(ctxs[i])]
        q=query[i]
        #for j in range(10):
        for j in range(len(ctxs[i])):
            try:
                r=get_llm_chatglm_0(evidences[j],q)
            except:
                error_d.append((i,j))
                continue
            if "True" in r:
                t_context_result['result'].append(r)
                t_context_result['id'].append(int(ctxs[i][j]['id']))
            else:
                f_context_result['result'].append(r)
                f_context_result['id'].append(int(ctxs[i][j]['id']))
        unsim=context_relation(t_context_result,f_context_result)
        print(unsim)
        unsim_s.append(unsim)
    return unsim_s,error_d

def f_main(file_path,rel_path):
    relation_c,error_d = get_enquery(file_path)
    print(len(relation_c))
    json_data = json.dumps(relation_c)
    json_data_1 = json.dumps(error_d)
    with open(rel_path, "w") as file:
        file.write(json_data)


if __name__=='__main__':
    file_path = "../robot_retr_result/medium_instr_goal.jsonl"
    relation_c, error_d = get_enquery(file_path)
    print(len(relation_c))
    json_data = json.dumps(relation_c)
    json_data_1 = json.dumps(error_d)
    with open("relation_context/L2/relation_context_medium.json", "w") as file:
        file.write(json_data)
    #with open("relation_context/L2/relation_context_popqa_error.json", "w") as file:
        #file.write(json_data_1)

"""

if __name__=='__main__':
    r=[[(1,2),(3,4)],[(5,6),(7,8)]]
    json_data=json.dumps(r)
    with open("11.json","w") as file:
        file.write(json_data)
"""