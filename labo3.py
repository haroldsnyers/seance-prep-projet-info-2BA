from random import randint
import threading as th
import socket

# Exo1
s = socket.socket()
s.connect(('www.ecam.be', 80))

sent = s.send("GET / HTTP/1.0\n\n".encode())
print(sent)

sent1 = s.send("GET /shit HTTP/1.0\n\n".encode())
print(sent1)

data = s.recv(512).decode()
print(data)
print("")

# Exo2
# See repository project-Server_chat

# Exo3
# ...

# Exo 4
results = {}
lock = th.Lock()


def compute():
    i = 1
    result = []
    while i <= 1000:
        lock.acquire()
        i += 1
        result.append(randint(1, 6))
        lock.release()
    print(result)
    print("la moyenne est: ", sum(result)/len(result))
    return result


thread = th.Thread(target = compute)
thread . start()
thread . join()  # Attendre la fin du thread

print('Thread ', thread .name, 'terminé ')
