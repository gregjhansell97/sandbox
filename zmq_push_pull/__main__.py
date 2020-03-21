from multiprocessing import Process
import os 
import zmq
import time


def subscriber(pub_sub_addr):
    context = zmq.Context()
    sub_socket = context.socket(zmq.SUB)
    sub_socket.connect(pub_sub_addr)
    # forgot to subscribe
    sub_socket.setsockopt(zmq.SUBSCRIBE, b"")
    try:
        while True:
            item = sub_socket.recv_pyobj()
            if item == None:
                return
            else:
                print(f"Subscriber {os.getpid()}: {item}")
    except KeyboardInterrupt:
        pass


def publisher(pull_addr, pub_addr): 
    context = zmq.Context()
    # pull
    pull_socket = context.socket(zmq.PULL)
    pull_socket.bind(pull_addr)
    # push
    pub_socket = context.socket(zmq.PUB)
    pub_socket.bind(pub_addr)

    try:
        while True:
            item = pull_socket.recv_pyobj()
            if item == None:
                break
            else:
                print(f"Publishing: {item}")
                pub_socket.send_pyobj(item)
    except KeyboardInterrupt:
        pass
    pub_socket.send_pyobj(None)

if __name__ == "__main__":
    context = zmq.Context()
    fan_in_addr = "ipc://./.push_pull.ipc"
    pub_sub_addr = "ipc://./.pub_sub.ipc"
    # start all sub scoekts before the PUB
    subs = [Process(target=subscriber, args=(pub_sub_addr,)) for _ in range(4)]
    for s in subs:
        s.start()

    p = Process(target=publisher, args=(fan_in_addr, pub_sub_addr))
    p.start()


    push_socket = context.socket(zmq.PUSH)
    push_socket.connect(fan_in_addr)
    try:
        while True:
            time.sleep(0.2)
            cmd = input(">>> ")
            if cmd == "exit":
                break
            push_socket.send_pyobj(cmd)
    except KeyboardInterrupt:
        pass
    push_socket.send_pyobj(None)
    p.join()
    for s in subs:
        s.join()
