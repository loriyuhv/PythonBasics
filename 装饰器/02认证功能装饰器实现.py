import time

current_userinfo = {"username": None}


def outer(func):
    def inner(*args, **kwargs):
        if current_userinfo["username"]:
            res = func(*args, **kwargs)
            return res
        else:
            username = input("Please input your username：").strip()
            password = input("Please input your password：").strip()
            if username == "Jerry" and password == "12345":
                print("login successful!!!")
                # 保存登录状态
                current_userinfo["username"] = username
                res = func(*args, **kwargs)
                return res
            else:
                print("username or password error!")
    return inner


@outer  # index = outer(index)
def index():
    print("Welcome to index page!!!")
    time.sleep(3)


@outer  # home = outer(home)
def home(name):
    print("Welcome %s" % name)
    time.sleep(2)
    return 123


index()
home("Jerry")
