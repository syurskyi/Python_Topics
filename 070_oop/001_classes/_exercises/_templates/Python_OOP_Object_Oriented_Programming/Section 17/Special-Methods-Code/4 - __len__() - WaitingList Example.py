class WaitingList:

    def __init__(self):
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)

    def __len__(self):
        return len(self.clients)
