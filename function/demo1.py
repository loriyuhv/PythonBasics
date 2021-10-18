def foo(name, sex, age):
    if sex == "male":
        print("%s is %s, he is %d" % (name, sex, age))
    else:
        print("%s is %s, she is %d" % (name, sex, age))


foo(name="Walker", sex="male", age=20)
