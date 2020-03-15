import multiprocessing
from multiprocessing import Queue, Process
import time


def listen(input_q): 
    output_qs = []
    try:
        while True:
            item = input_q.get()
            if item == None:
                return
            elif isinstance(item, multiprocessing.queues.Queue):
                print("ADDING NEW OUTPUT QUEUE")
                output_qs.append(item)
            else:
                print("#"*50)
                print(item)
                print("#"*50)
                for q in output_qs:
                    q.put(item)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    input_q = Queue()
    output_qs = []
    p = Process(target=listen, args=(input_q, ))
    p.start()
    try:
        while True:
            time.sleep(0.2)
            for q in output_qs:
                if q.empty():
                    continue
                print(f"{q}: {q.get()}")
            cmd = input(">>> ")
            if cmd == "exit":
                break
            elif cmd == "add":
                output_qs.append(Queue())
                input_q.put(output_qs[-1])
            input_q.put(cmd)
    except KeyboardInterrupt:
        pass
    print("")
    input_q.put(None)
    p.join()
