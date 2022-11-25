import zmq
from interpreter import Interpreter

context = zmq.Context()
socket1 = context.socket(zmq.REP)
socket1.bind("tcp://*:1489")

while True:
    message = socket1.recv().decode("utf-8")
    if message[:4] == "dict":
        interp = Interpreter()
        msgSend = interp.eval(message[5:])
        socket1.send(str(msgSend).encode())
    elif message[:4] == "tree":
        interp = Interpreter()
        msgSend = interp.returnTree(message[5:])
        tree = ""
        for i in msgSend:
            tree += str(i)
        socket1.send(tree.encode())
    else:
        socket1.send(b"Error")

