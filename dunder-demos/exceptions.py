import inspect


try:
    raise ValueError("there is something wrong")
except Exception as e: 
    print(e)
    print(e.__class__)
