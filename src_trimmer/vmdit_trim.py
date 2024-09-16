import json

def read_rel(file_path):
    relation=[]
    with open(file_path, "r", encoding='utf-8') as fin:
        for k,example in enumerate(fin):
            example = json.loads(example)
            for x in example:
                for y in x:
                    relation.append(y)
    #print(len(relation))
    return relation

def read_evi(file_path):
    ids=[]
    ctxs=[]
    query=[]
    with open(file_path, "r", encoding='utf-8') as fin:
        for k, example in enumerate(fin):
            example = json.loads(example)
            ctxs.append(example["ctxs"])
            query.append(example["question"])
            ids.append([int(x['id']) for x in example['ctxs']])
    return ids,ctxs,query

def get_context(rel_path,file_path):
    rel=read_rel(rel_path)
    #print(rel)
    all_ids,all_ctxs,query=read_evi(file_path)
    result=[]
    for x in range(len(all_ctxs)):
        ids=all_ids[x]
        del_id=[]
        l=len(ids)
        for i in range(l):
            idx=ids[i]
            for j in range(i+1,l):
                idy=ids[j]
                if [idx,idy] in rel:
                    del_id.append(idy)
        #print("del",del_id)
        evidence=[]
        for ct in all_ctxs[x][:30]:
            if int(ct['id']) not in del_id:
                ct= ct["title"] + "\n" + ct["text"]
                evidence.append(ct)
        print("l evi:",len(evidence))
        data_line={}
        data_line['id']=x
        data_line['question']=query[x]
        data_line['ctxs']=evidence
        result.append(data_line)
    return result



if __name__=='__main__':
    rel_path = "relation_context/L2/relation_context_medium.json"
    #file_path= "retr_result/L2/medium_instr_goal.jsonl"
    file_path = "../robot_retr_result/hard_instr_goal.jsonl"
    trimed_path="trimmed_evidences/L2/trimmed_evidences_hard.jsonl"
    pro_c=get_context(rel_path,file_path)
    with open(trimed_path, "w", encoding='utf-8') as file:
        for example in pro_c:
            file.write(json.dumps(example) + '\n')


