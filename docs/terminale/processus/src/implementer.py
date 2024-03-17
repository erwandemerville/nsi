import threading
compteur = 0

def incr():
    global compteur
    for c in range(1000000):
        v = compteur
        compteur = v + 1

t1 = threading.Thread(target=incr)
t2 = threading.Thread(target=incr)
t3 = threading.Thread(target=incr)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("valeur finale", compteur)