import traceback
import time
ALL_GRAMMAR_HERE = (
    "for else",
    "函数注解",
    "with",
    "yield",
    "decorator",
    "super",
    "property",
    "kwargs and args",
    "lambda",
    "classmethod",
    "* and =",
    "int with _",
    "class in def",
    "slots in class",
    "assert",
    "raise",
    "nonlocal",
    "...",
    "iter")


print("for ... else ... : ")
for i in range(110):
    if i == 5:
        break
else:
    print("1.without break")

for i in range(1, 10):
    if i == 15:
        break
else:
    print("2.without break")
print()

print("annotation: def add(num1:int,num2:int)->int:")


def add(num1: int, num2: int) -> int:
    return num1 + num2
print(add.__annotations__)
print(add(1,2))
add.__annotations__["num1"] = str
add.__annotations__["num2"] = str
add.__annotations__["return"] = str
print(add.__annotations__)
print(add("hello ", "world"))


print()

print("with : ")


class With():
    def __enter__(self):
        print("enter!")
        return self

    def operate(self, name, bug):
        print("operate " + name + "!" + bug)

    def __exit__(self, exc_type, exc_value, traceback):
        print("exc_type : " + str(exc_type))
        print("exc_value : " + str(exc_value))
        print("traceback : " + str(traceback))
        print("exit!")
        return True


bug = 1
with With() as opr:
    opr.operate("nick", bug)
print()

print("yield : ")


def yield_test():
    for i in range(10):
        yield i


def normal_test():
    num_list = []
    for i in range(10):
        num_list.append(i)
    return num_list


yield_nums = yield_test()
print(yield_nums)
for num in yield_nums:
    print(num)
while True:
    try:
        print(yield_nums.__next__())
        print(next(yield_nums))
    except StopIteration as e:
        print(e)
        break

print("decorator : ")


def do():
    def real_decorator(function):
        def wrapped(*args, **kwargs):
            result = function(*args, **kwargs)
            print("l am a decorator!")
            return result
        return wrapped
    return real_decorator


@do()
def hello():
    print("Hello World!")


hello()


def time_c(func):
    def wrapper(*args, **kwargs):
        #start = time.perf_counter()
        start = time.time()
        func(*args, **kwargs)
        #elapsed = (time.perf_counter() - start)
        elapsed = (time.time() - start)
        print("{} : Time used: {}".format(func.__name__, elapsed))
    return wrapper


@time_c
def sleep_test():
    time.sleep(2)


print("yield and send")


def yield_send():
    print("please tell me what you want to say")
    while True:
        words = yield
        print("l receive your words : " + str(words))


send_test = yield_send()
next(send_test)
send_test.send("hello")

print("with no super : ")


class me:
    def hello(self):
        print("Hello,everyone!")


class my_friend(me):
    def hello(self):
        me.hello(self)
        print("l am his friend")


my_friend().hello()
print()

print("with super : ")


class my_friend_with_super(me):
    def hello(self):
        # super(my_friend_with_super,self).hello()
        super().hello()
        print("l am his friend")


my_friend_with_super().hello()
print()


class Tea:
    def __init__(self, things):
        self.things = things

    def __repr__(self):
        return self.things

    @classmethod
    def need(cls):
        return cls(["sugar", "pearl", "water"])


class PearlTea(Tea):
    @classmethod
    def need(cls):
        needed = super().need().things
        needed += ["pearl"] * 2
        return needed


mytea = Tea.need()
mypearltea = PearlTea.need()
print(mytea.things)
print(mypearltea)
print()

print("property : ")


class property_test:
    def __init__(self, height, weight):
        self.w = weight
        self.h = height

    def __repr__(self):
        return f"{self.__class__.__name__}({self.weight},{self.height})"

    @property
    def weight(self):
        return self.w

    @weight.setter
    def weight(self, new_weight):
        self.w = new_weight

    @property
    def height(self):
        return self.h

    @height.setter
    def height(self, new_height):
        self.h = new_height


you = property_test(50, 170)
print(you.weight, you.height)
you.weight = 55
print(you)
you.height = 175
print(you)
print()

print("kwargs and args")


def kwargs_args(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)


kwargs_args("nick", "foo", "bar", sex="male")

nums = [i**2 for i in range(10)]
dict_nums = {i: i**2 for i in range(10)}
print(nums)
print(dict_nums)

print("lambda : ")


lambda_add = lambda a, b:a + b

print(lambda_add(1, 4))


first, second, *third = 1, 2, 3, 4
print(first, second, third)
first, *second, third = 1, 2, 3, 4
print(first, second, third)

print("num_use_ :　")
num_use_ = 1_000_000_500
print(num_use_)


def add_more_nums(x):
    class AddNum(int):
        def __call__(self, x):
            return AddNum(self.numerator + x)
    return AddNum(x)


print(add_more_nums(1)(2)(3)(4))



def assert_hello(name: str):
    assert len(name) > 1, "your name is too short!"
    print("hello,", name)


assert_hello("nick")
try:
    assert_hello("a")
except Exception as e:
    print(e)


class ExitBye(Exception):
    pass


try:
    print(1 / 0)
except Exception as e:
    try:
        raise ExitBye("have an error with raise") from e
    except Exception as e:
        traceback.print_exc()


def counter_nonlocal():
    count = 0

    def count_add():
        nonlocal count
        count += 1
        return count
    return count_add


def counter_test():
    num = counter_nonlocal()
    print(num())
    print(num())


counter_test()

print(type(...))


def ellipsis_test():
    ...



from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
	if n < 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)
	
class Fibonacci:
	def __init__(self, a, origin=False, reverse=False):
		self.a = a
		self.origin = origin
		self.reverse = reverse
	def __iter__(self):
		return self
 
	def __next__(self):
		x = self.a
		if self.reverse:
			self.a -= 1
		else:
			self.a += 1
		x = fibonacci(x)
		if self.origin:
			return (self.a, x)
		else:
			return x

fibon = Fibonacci(50, origin=True, reverse=True)
iterfibon = iter(fibon)

for i in range(10):
	print(next(iterfibon))
