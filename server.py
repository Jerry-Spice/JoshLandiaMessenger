class Server(object):
    def __init__(self, id, displayname):
        self.id = id
        self.name = displayname
        self.clients = []
        self.chat = []
    def getClients(self):
        return self.clients
    def getId(self):
        return self.id
    def changeId(self, newId):
        self.id = newId
    def changeName(self, newName):
        self.name = newName
    def getChat(self):
        return self.chat
    def getMostRecentChat(self):
        return self.chat[-1]
    def receiveMessage(self, authorName, message):
        self.chat.append(authorName+": "+message)
        print(self.chat)
    def displayChat(self):
        msg = "-----"+self.name+"-----\n"
        messageBackLog = len(self.chat)-10
        if messageBackLog < 0:
            messageBackLog = 0
        for i in range(messageBackLog,len(self.chat),1):
            msg += self.chat[i] +"\n"
        return msg
