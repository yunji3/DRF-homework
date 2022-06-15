#  1. args, kwargs를 사용하는 예제 코드 짜보기

def myFun(*args):
    print('args:', args)
    for arg in args:
        print(arg)


myFun('Hello', 'World')

myFun('Hello', 'World', 'Python', '!!!')


def myFun(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"key = {key}, value = {value}")

    print('arg1:', kwargs['arg1'])
    print('arg2:', kwargs['arg2'])
    print('arg3:', kwargs['arg3'])


myFun(arg1='Hello', arg2='World', arg3='Python')
