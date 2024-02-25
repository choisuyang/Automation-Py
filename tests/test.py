def decorator(func):
    def wrapper(*args, **kwargs):
        print('Hello')
        return func(*args, **kwargs)
    return wrapper

@decorator
def introduce(name):
    print(f"My name is {name}")

introduce('mike')