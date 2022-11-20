import matplotlib.pyplot as plt
import socket
import numpy as np


def recvall(sock, n):
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return
        data.extend(packet)
    return data


host = "84.237.21.36"
port = 5152
packet_size = 40002

plt.ion()
plt.figure()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    beat = b'nope'
    count = 0
    while count != 10:
        sock.send(b'get')
        bts = recvall(sock, packet_size)

        rows, cols = bts[:2]

        im = np.frombuffer(bts[2:rows * cols + 2], dtype="uint8").reshape(rows, cols)


        pos12 = []

        for i in range(len(im) - 1):
            for j in range(len(im) - 1):
                if im[i - 1][j - 1] <  im[i][j] and im[i - 1][j + 1] <  im[i][j] and im[i - 1][j] <  im[i][j] and im[i][j - 1] <  im[i][j] and \
                        im[i + 1][j] <  im[i][j] and im[i][j + 1] <  im[i][j] and im[i - 1][j + 1] <  im[i][j] and im[i + 1][j - 1] <  im[i][j]:
                    pos12.append([i,j])

        print(pos12)

        if len(pos12) > 1:
            distance = round(((pos12[0][0] - pos12[1][0]) ** 2 + (pos12[0][1] - pos12[1][1]) ** 2) ** 0.5, 1)
        else:
            distance = 0.0

        plt.clf()
        plt.imshow(im)
        plt.pause(1)

        sock.send(str(distance).encode())
        beat = sock.recv(20)

        if beat == b'yep':
            count += 1


        print("Beat", beat)
        print("Count", count)
