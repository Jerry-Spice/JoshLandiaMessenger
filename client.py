import tkinter as tk
class Client(object):
    def __init__(self, id, displayname, servers):
        self.id = id
        self.name = displayname
        self.server = None
        self.servers = servers
        self.root = tk.Tk()
    def connect(self, connectionId):
        if self.server == None:
            for i in range(len(self.servers)):
                if self.servers[i].id == connectionId:
                    self.servers[i].clients.append(self)
                    self.server = self.servers[i]
    def sendMessage(self, message):
        if self.server == None:
            return -1 # not connected to a server
        self.server.receiveMessage(self.name, message)

    def sendMessageGUI(self):
        message = self.chatInput.get()
        self.chatInput.delete(0,'end')
        self.sendMessage(message)

    def CreateGUI(self):
        #window properties
        self.root.title("JL Messenger - "+self.name)
        self.root.geometry("400x400")
        #creating the elements
        chatValue = self.server.displayChat()
        self.chat = tk.Label(self.root, text=chatValue)
        self.chatInput = tk.Entry(self.root)
        self.chatSubmit = tk.Button(self.root, text="Send", command=self.sendMessageGUI)

        #packing the elements
        self.chat.pack()
        self.chatInput.pack()
        self.chatSubmit.pack()
        #main loop


    def updateGUI(self):
        self.chat.configure(text=self.server.displayChat())
        self.root.update()
