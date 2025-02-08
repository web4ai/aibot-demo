class Memory:
    def __init__(self):
        self.memory_store = []

    def store_interaction(self, user_input, agent_response):
        interaction = {
            'user_input': user_input,
            'agent_response': agent_response
        }
        self.memory_store.append(interaction)

    def retrieve_memory(self):
        return self.memory_store

    def clear_memory(self):
        self.memory_store = []