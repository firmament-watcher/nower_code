# coding=utf-8
def log(func):
    '''
    * 无名字参数
    ** 有名字参数
    '''
    def wrapper(*args, **kvargs):
        print 'before calling ', func.__name__
        print 'args', args, 'kvargs', kvargs
        func(*args, **kvargs)
        print 'end calling ',func.__name__
    return wrapper

@log
def hello(name,age):
    print 'hello', name, age

if __name__ == '__main__':
    hello(name= 'nowcoder', age='2')