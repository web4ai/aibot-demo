import openai


class AI_Agent:
    def __init__(self, api_key, memory, rag):
        self.api_key = api_key
        self.memory = memory
        self.rag = rag

    def generate_response(self, user_input):
        context = self.rag.retrieve(user_input)
        response = self.call_openai_api(user_input, context)
        self.memory.store_interaction(user_input, response)
        return response

    def call_openai_api(self, user_input, context):
        openai.api_key = self.api_key
        prompt = f"{context}\nUser: {user_input}\nAI:"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']

    def get_memory(self):
        return self.memory.retrieve_all()
