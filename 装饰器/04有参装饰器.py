import time

current_userinfo = {"user": None}


def auth(engine='file'):
    def outer(func):
        def wrapper(*args, **kwargs):
            if engine == "file":
                if current_userinfo['user']:
                    return func(*args, **kwargs)
                username = input('Please input yor username:')
                pwd = input("Please input your password:")
                if username == 'Jerry' and pwd == '123':
                    print("login successful!")
                    # 保存登录状态
                    current_userinfo['user'] = username
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("user or password error")
            elif engine == 'mysql':
                print("mysql的认证机制。")
            else:
                print("不支持该engine")

        return wrapper
    return outer


# x = auth(engine='file')  # x = outer
# @x  # @outer #  # index = outer(最原始的index) # index = wrapper
@auth(engine='file')
def index():
    print("welcome to index page")
    time.sleep(3)


@auth(engine='ldap')
def home(name):
    print('welecom %s ' % name)
    time.sleep(2)
    return 123


index()
home('loriyuhv')
