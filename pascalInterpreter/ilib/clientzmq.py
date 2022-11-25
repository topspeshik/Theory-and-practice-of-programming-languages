import zmq

context = zmq.Context()

print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:1489")

#dict BEGIN...
#tree BEGIN..

socket.send(b"dict BEGIN x:= 2 + 3 * (2 + 3); y:= 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1)); END.")
message = socket.recv()
print(message)

socket.send(b"dict BEGIN END.")
message = socket.recv()
print(message)

socket.send(b"tree BEGIN y:=5; END.")
message = socket.recv()
print(message)

socket.send(b"tee BEGIN y:=5; END.")
message = socket.recv()
print(message)

