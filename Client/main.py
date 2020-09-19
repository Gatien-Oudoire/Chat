#coding:utf-8
import socket 

host = input("Entrez l'adresse du serveur voulu \n")

if host == "":
    host = "127.0.0.1"
elif host == "0":
    host = "192.168.1.140"
elif host == "gatien":
    host = "gatien-oudoire.ddns.net"

port, host = (6010, host)

try:
    print("Tentative de connexion sur -> " + host) 
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port))
    print("La connexion a réussie \n")
    print("Il est conseillé de décliner son identité dans le premier message")
    while True:
        data = input("Entrez votre message \n")
        if data != "":
            data = data.encode("utf8")
            socket.sendall(data)




except ConnectionRefusedError:
    print("La connexion a été refusée \nLe serveur est peut être éteint ?")

except ConnectionAbortedError:
    print("La connexion n a pas eu lieu")

except:
    print("La connexion a échouée")


finally:
    print("Merci d'avoir utilisé le programme créé par @Gatien-Oudoire")
    socket.close()