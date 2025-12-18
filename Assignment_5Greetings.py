# Write a decorator greet that prints Hello! before executing a function. eg: Hello! My name is Alice

def greet(func):
    def wrapper(*args,**kwargs):
        print('Hello!')
        func(*args,**kwargs)
    return wrapper

@greet
def my_name(name):
    print(f'My name is {name}')

my_name('Alice')