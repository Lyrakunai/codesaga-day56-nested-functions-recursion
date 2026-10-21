
# Day 56 — Nested Functions, nonlocal & Recursion

# 1. Nested Functions
def outer():
    message = "Hello from inner function"

    def inner():
        print(message)

    inner()


outer()


# 2. nonlocal Keyword
def create_counter():
    count = 0

    def update():
        nonlocal count
        count += 1
        return count

    return update


counter = create_counter()
print(counter())
print(counter())


# 3. Recursive Function
def calculate(n):
    if n == 0:
        return 2

    return n + calculate(n - 1)


print(calculate(3))  # 8
