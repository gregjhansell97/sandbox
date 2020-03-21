import inspect


class Wrapper:
    def __init__(self, obj):
        self.obj = obj
    def __getattribute__(self, item):
        obj = super().__getattribute__("obj")
        return getattr(obj, item)



class A:
    def run(self):
        print("WRAPPED IT BOI")
    async def stop(self):
        print("stopped")

a = A()

w = Wrapper(a)


w.run()

print(inspect.iscoroutinefunction(a.stop))
print(inspect.iscoroutinefunction(a.run))
