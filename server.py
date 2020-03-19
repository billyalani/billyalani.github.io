import socket
import pickle
import os
from threading import Thread
import sys
import time

 
information_for_players = [[100,510,100,False,100,5,0,False,0,0,False,10,False,False,0,0,False,False,False,0,10],[1200,510,200,False,100,5,1,False,0,0,False,10,False,False,0,0,False,False,False,0,10]]
                          # 0   1   2     3    4  5 6   7   8 9  10  11   12   13  14 15  16E    17   18 19 20
                          #information_for_players[ID][10]: isJump
                          #information_for_players[ID][11]: joumpcount
                          #information_for_players[ID][16]: isColide
                          #information_for_players[ID][19]: count
                          #information_for_player[ID][20]: ammo
def crea_server(indirizzo):
    lista_users = list()
    index = 0
    s = socket.socket()
    s.bind(indirizzo)
    s.listen(5)
    print (f"Server Creato {indirizzo[0]}")
    while len(lista_users) < 2:
        lista_users.append(0)
        lista_users[index] , address = s.accept()
        print (f"Si e connesso il {len(lista_users)}")
        lista_users[len(lista_users)-1].send(pickle.dumps(len(lista_users)-1)) #invia ID
        index += 1
    for ID in range(2):
        lista_users[ID].send(pickle.dumps(True))

    time.sleep(2)

    for i in range(len(lista_users)):
        lista_users[i].send(pickle.dumps(information_for_players))
    while True:
        try:
            for i in range(len(lista_users)):
                information_for_player = pickle.loads(lista_users[i].recv(5120))
                information_for_players[i] = information_for_player
            for i in range(len(lista_users)):
                lista_users[i].send(pickle.dumps(information_for_players))
            print(f"Sfera  X = {information_for_players[0][0]} Y = {information_for_players[0][1]}")
        except:
            for i in range(len(lista_users)):
                lista_users[i].close()
            s.close()
            crea_server(("192.168.1.9" , 15000))


    
crea_server(("192.168.1.9" , 15000))
