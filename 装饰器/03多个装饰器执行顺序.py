import time

current_userinfo = {'user': None}


def timer(func):   # func = 最原始的index指向的内存地址
    def wrapper2(*args, **kwargs):
        print('wrapper2.....')
        start = time.time()
        res = func(*args, **kwargs)   # func=最原始的index指向的内存地址
        stop = time.time()
        print('run time is %s' % (stop - start))
        return res
    return wrapper2


def outer(func):    # func=wrapper2
    def wrapper1(*args, **kwargs):
        print('wrapper1.....')
        if current_userinfo['user']:
            return func(*args, **kwargs)
        user = input('please input you username: ').strip()
        pwd = input('please input you password: ').strip()
        if user == 'egon' and pwd == '123':
            print('login successful!!!')
            # 保存登录状态
            current_userinfo['user'] = user
            res = func(*args, **kwargs)   # func=wrapper2
            return res
        else:
            print('user or password err')
    return wrapper1


# 解释语法的时候应该自下而上
# 执行的时候是自上而下
# 可以连续写多个装饰器，处于最顶层的装饰器先执行
@timer  # index = timer(index) ==> timer(wrapper1)
@outer  # index = outer(最原始的index) # index = wrapper1
def index():
    print("Welcome to index page!!!")
    time.sleep(3)


index()     # index ==> wrapper2


# 以上实现不了我的功能，所以顺序有关系
@outer
@timer
def index():
    print("Welcome to index page!!!")
    time.sleep(3)




