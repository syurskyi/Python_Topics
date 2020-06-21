class WaitingList:

    def __init__(self):
        self.clients = clients

    def add_client(self, client):
        self.clients.append(client)

    def __getitem__(self, position):
        if self.clients:
            return self.clients[position]
        else:
            print("The waiting list is empty")
