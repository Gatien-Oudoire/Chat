#coding:utf-8
import socket
import threading

#------------------------------------------------------------------------------------------------
class ThreadPourCLient(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    
    def run(self):
        data = self.conn.recv(1024)
        data = data.decode("utf8")
        data = adress[0]+": "+data
        print(data)

#------------------------------------------------------------------------------------------------
host, port = ('', 6010)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))

print("Le serveur démarre ...")

while True:
    socket.listen(5)
    conn, adress = socket.accept()
    print(adress[0] + " c'est connecté")
    
    monThread = ThreadPourCLient(conn)
    monThread.start()

conn.close()
socket.close()