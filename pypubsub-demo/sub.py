
import time

from pubsub import pub

# create a listener
def on_publish(arg1, arg2=None):
    print(f"received: {arg1}, arg2={arg2})")

if __name__ == "__main__":
    pub.subscribe(on_publish, "rootTopic")
    while True:
        time.sleep(10)
        pass
