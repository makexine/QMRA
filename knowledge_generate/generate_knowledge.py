from robot.LLM.llms.gpt3 import LLMGPT3


output_file='knowledge_medium_100.txt'
input_file='prompt_knowledge_medium.txt'

with open(input_file, "r", encoding="utf-8") as f:
    prompt=f.read().strip()

llm = LLMGPT3()
messages = [{"role": "user", "content": prompt}]
answer = llm.request(message=messages)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(answer)