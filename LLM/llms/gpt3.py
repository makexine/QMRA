import os

from openai import OpenAI


class LLMGPT3():
    def __init__(self):
        self.client = OpenAI(
            base_url="" , api_key="" 
        )

    def request(self, message):  # question
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            #model="gpt-4o",
            #model="claude-3-5-sonnet-20240620",
            messages=message,
        )

        return completion.choices[0].message.content

    def embedding(self, question):
        embeddings = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=question
        )

        return embeddings

    def list_models(self):
        response = self.client.models.list()
        return response.data

    def list_embedding_models(self):
        models = self.list_models()
        embedding_models = [model.id for model in models if "embedding" in model.id]
        return embedding_models


if __name__ == '__main__':
    llm = LLMGPT3()
    embedding_models = llm.list_embedding_models()
    print("Available embedding models:")
    for model in embedding_models:
        print(model)

    #models = llm.list_models()
    #for model in models:
        #print(model.id)

    question="who are you,gpt?"
    messages = [{"role": "user", "content":question}]
    # print(messages)
    answer = llm.request(message=messages)
    # # answer = llm.embedding(question="who are you,gpt?")
    print(answer)
