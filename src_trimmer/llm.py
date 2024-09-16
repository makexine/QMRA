import json
import zhipuai




def get_llm_chatglm_1():
    # your api key
    #print("llm!")
    zhipuai.api_key = "1b63a16cb13959ca1abf3a3fededa2a2.IYPOsV0KXyuXyle7"
    ins_0='You are a cautious language assistant.'
    ins_1='Divide the sentences into the form of subject, verb, and object, and present the following sentence in the form of (subject, verb, object). Pay attention to verb phrases.'
    sen_1='He turn on the radio.'
    sen_2 = 'He turn off the radio.'
    ins_2= 'Determine whether sentences can be identified as similar based on the extracted triples. Only if the elements in triples are similar, the sentences can be told as similar. Be especially mindful of verb phrases that appear similar but actually have opposite meanings which make sentences are actually dissimilar. The answer can only be a yes or no.'
    example=['####Triple:(I, turn on, radio) (I, turn off, radio)\n###Answer: no',
             '####Triple:(I, turn on, radio) (I, turn on, radio)\n###Answer: yes',
             '####Triple:(I, turn up, radio) (I, turn down, radio)\n###Answer: no']
    ex='Here are some examples.\nExample:'+'\n'.join(example)
    prompt=ins_0+'\n'+ins_1+'\n'+sen_1+'\n'+sen_2+'\n'+ex+'\n'+ins_2

    response = zhipuai.model_api.invoke(
            model="chatglm_turbo",
            prompt=[{"role": "user", "content": prompt}],
            top_p=0.7,
            temperature=0.9,
        )
    return response['data']['choices'][0]['content']

def get_llm_chatglm_2(): #思维链表达VMD
    # your api key
    #print("llm!")
    zhipuai.api_key = "1b63a16cb13959ca1abf3a3fededa2a2.IYPOsV0KXyuXyle7"
    ins_0='You are a cautious language assistant.'
    ins_1='Here are some language rules:\n Only if the subjects, verbs and objects of two sentences are similar, then the two sentences can be identified as similar. Be especially mindful of verb phrases that appear similar but actually have opposite meanings which make sentences dissimilar. '
    ins_2= 'Determine whether the meaning of sentences can be identified as similar according to the language rules. The answer can only be True or False.  Only output one word.'
    sen_1 = 'He come in.'
    sen_2 = 'He come out.'

    prompt=ins_0+'\n'+ins_1+'\n'+ins_2+'\n'+sen_1+'\n'+sen_2

    response = zhipuai.model_api.invoke(
            model="chatglm_turbo",
            prompt=[{"role": "user", "content": prompt}],
            top_p=0.7,
            temperature=0.9,
        )
    return response['data']['choices'][0]['content']

def get_llm_chatglm_3(): #dot代替
    # your api key
    #print("llm!")
    zhipuai.api_key = "1b63a16cb13959ca1abf3a3fededa2a2.IYPOsV0KXyuXyle7"
    ins_0='You are a cautious language assistant.'
    ins_1='###Here are some language rules:\n If the two sentences can be identified as similar, then the subjects, verbs and objects of two sentences are similar. Be especially mindful of verb phrases that appear similar but actually have opposite meanings which make sentences dissimilar. '
    ins_2 = 'If the two sentences can be identified as similar, then the adverbials and attributives of two sentences are similar.'
    ins_3 = '###Are the following statements similar with the question? Just Say True if they are; otherwise just say False. Only output one word.'

    sen_1 = 'He come out at five.'
    sen_2 = 'He come out at six.'

    prompt=ins_0+'\n'+ins_1+'\n'+ins_2+'\n\n'+ins_3+'\n'+sen_1+'\n'+sen_2

    response = zhipuai.model_api.invoke(
            model="chatglm_turbo",
            prompt=[{"role": "user", "content": prompt}],
            top_p=0.7,
            temperature=0.9,
        )
    return response['data']['choices'][0]['content']


if __name__=='__main__':
    print(get_llm_chatglm_3())


