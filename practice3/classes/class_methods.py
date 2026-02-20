# 1
class MathUtils:
    @classmethod
    def add(cls, a, b):
        return a + b

print(MathUtils.add(3, 4))
# 2
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

Counter.increment()
print(Counter.count)
# 3
class Factory:
    @classmethod
    def create_default(cls):
        return cls()

obj = Factory()
print(type(obj))
# 4
class Temperature:
    @classmethod
    def celsius_to_fahrenheit(cls, c):
        return (c * 9/5) + 32

print(Temperature.celsius_to_fahrenheit(0))
# 5
class Logger:
    logs = []

    @classmethod
    def add_log(cls, message):
        cls.logs.append(message)

Logger.add_log("Start")
print(Logger.logs)