
import time

from pubsub import pub

def demo():
    print("publishing results")
    pub.sendMessage("rootTopic", arg1=123, arg2={"a": "abc"})

if __name__ == "__main__":
    while True:
        time.sleep(1)
        demo()
