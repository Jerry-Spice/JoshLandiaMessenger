from server import *
from client import *
import tkinter as tk

servers = [Server("0000", "Server1")]
TESTCLIENT1 = Client("0","Jspice", servers)
TESTCLIENT2 = Client("1", "Ymom", servers)

TESTCLIENT1.connect("0000")
TESTCLIENT2.connect("0000")


print("booting up servers...")
for server in servers:
    for client in server.clients:
        client.CreateGUI()
print("up and running")
while True:
    for server in servers:
        for client in server.clients:
            client.updateGUI()
