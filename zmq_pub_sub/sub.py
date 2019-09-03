
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:5556")

socket.setsockopt_string(zmq.SUBSCRIBE, "")


poller = zmq.Poller()
poller.register(socket, zmq.POLLIN)

while True:
    for s, e in poller.poll(1000):
        data = s.recv_string()
        print(data)
