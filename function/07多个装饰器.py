import time

current_userinfo = {'user': None}


def timmer(func): #func=最原始的index指向的内存地址
    def wrapper2(*args, **kwargs):
        print('wrapper2.....')
        start=time.time()
        res=func(*args,**kwargs) # func=最原始的index指向的内存地址
        stop=time.time()
        print('run time is %s' %(stop - start))
        return res
    return wrapper2


def outter(func): # func=wrapper2
    def wrapper1(*args,**kwargs):
        print('wrapper1.....')
        if current_userinfo['user']:
            return func(*args,**kwargs)
        user=input('please input you username: ').strip()
        pwd=input('please input you password: ').strip()
        if user == 'egon' and pwd == '123':
            print('login successfull')
            # 保存登录状态
            current_userinfo['user']=user
            res=func(*args,**kwargs) # func=wrapper2
            return res
        else:
            print('user or password err')
    return wrapper1
