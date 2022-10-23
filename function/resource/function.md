# 函数

## 一、函数

### 1.1 什么是函数

函数就是具备某一功能的工具

- 函数的使用必须遵循先定义、后调用的原则

- 事先准备工具的过程即函数的定义
- 拿来就用即函数的调用

**分类**

- 内置的函数
- 自定义函数

### 1.2 为何要用函数

1. 程序的组织结构不清晰、可读性差
2. 日积月累冗余代码过多
3. 程序的可扩展性极差

### 1.3 使用

#### 1.3.1 定义函数

1. 语法

   ```
   def 函数名(参数1,参数2,参数3,...):
       """
       文档注释
       """
       code1
       code2
       code3
       ...
       return 返回值
   ```

2. 定义函数阶段发生哪些事：只检测语法，不执行代码

   ```python
   def foo():  # foo = 函数的内存地址
       print('first')
       print('second')
       print('hello')
       print('third')
   
   
   # 调用阶段
   foo()
   print(foo)
   foo = 10
   foo()   # 出错
   ```

   **示范一**

   ```python
   def bar():
       print("from bar")
   
   
   def foo():
       print('from foo')
       bar()
   
   
   foo()
   ```

   **示范二**

   ```python
   # 定义阶段
   def foo():
       print('from foo')
       bar()
   
   
   def bar():
       print("from bar")
   
   
   # 调用阶段
   foo()
   
   ```

   **示范三**

   ```python
   # 定义阶段
   def foo():
       print('from foo')
       bar()
   
   
   # 调用阶段
   foo()
   
   
   def bar():
       print('from bar')
   ```

3. 定义函数的三种形式

   - 无参函数

     ```python
     def func1():
         print('hello1')
         print('hello2')
         print('hello3')
     
     
     func1()
     ```

   - 有参函数

     ```python
     def func2(x, y):
         # x = 1
         # y = 3
         if x > y:
             print(x)
         else:
             print(y)
     
     
     func2(1, 2)
     func2(2, 3)
     func2(3, 4)
     ```

   - 空函数

     ```python
     def get():
         pass
     
     
     def put():
         pass
     ```

#### 1.3.2 调用函数

1. 语法

   **函数名()**

2. 调用函数会发生什么事

   - 根据函数名找到函数的内存地址
   - 函数的内存地址加括号可以触发函数体代码的运行

3. 调用函数的三种方式

   **语句**

   ```python
   def f1():
       print('from 1')
   
    
   f1()
   ```

   **表达式形式**

   ```python
   def max2(x, y):
       if x > y:
           return x
       else:
           return y
       pass
   
   
   res = max(1, 2) * 10
   print(res)
   ```

   **当作参数传给其他函数**

   ```python
   def max2(x, y):
       if x > y:
           return x
       else:
           return y
       pass
   
   
   res = max2(max2(1, 2), 3)
   print(res)
   ```

## 二、函数返回值

### 2.1 介绍

1. 什么是函数的返回值

   函数的返回值是函数体代码运行的一个成果。

2. 什么时候用函数的返回值

3. 如何用

### 2.2 return值

1. 返回值没有类型限制

2. 返回值没有个数限制

   - 逗号分隔多个值：返回一个元组

     ```python
     def foo():
         x = 10
         y = 5
         return x, y
     
     
     a = foo()
     print(type(a), a)
     ```

   - 一个值：返回一个值

     ```python
     def foo():
         x = 10
         return x
     
     
     a = foo()
     print(type(a), a)
     ```

   - 没有return：默认返回一个None

     ```python
     def foo():
         return
     
     
     a = foo()
     print(type(a), a)
     ```

### 2.3 return是结束函数的标志

- 函数内可以有多个return，但只要执行一次，整个函数就立即结束，并且将return后的值当作本次调用的结果返回。

  ```python
  def f1():
      print(1)
      return 'aaa'
  	print(2)	# 出错
      return 'bbb'	# 出错
  
  
  print(f1())
  ```

  

## 三、函数的参数

### 3.1 形参和实参

函数的参数分为两大类：形参与实参

- 形参：指的是在定义函数时，括号指定的参数,本质就是变量名
- 实参：指的是在调用函数时，括号内传入的值，本质就是值

只有在调用函数时才会在函数体内发生实参（值）与形参（变量名）的绑定关系，该绑定关系只在调用函数时临时生效，在调用函数结束后就解除绑定

```python
def foo(x, y):   # x和y是实参
    print(x)
    print(y)


a = 1
b = 2
foo(a, b)   # a和b是实参
# foo(1, 2)
```

### 3.2 位置参数

- 位置形参：在定义函数时，按照从左到右的顺序依次定义的形参称之为位置形参

  **注意：**但凡是按照位置定义的形参，在调用函数时必须其传值，多一个不行少一个也不行

- 位置实参: 在调用函数时，按照从左到右的顺序依次传入的值

  **注意：**在传值是按照顺序与形参一一对应

```python
def foo(x, y, z):
    print(x, y, z)


# foo(1, 2)
# foo(1, 2, 3, 4)
foo(1, 2, 3)
foo(3, 2, 1)
```

### 3.3 关键字参数

在调用函数时，按照key=value的形式定义的实参，称之为关键字实参

注意：

- 在传值时可以完全打乱顺序，但仍然能指名道姓地为指定的参数传值
- 可以在调用函数时，混合使用位置实参与关键字实参，但是位置实参必须跟在关键字实参左边，并且不能为一个形参重复传值

```python
def register(name, sex, age):
    print(name)
    print(sex)
    print(age)


# 位置形参
# register('Walker', 'male', 18)
# register('male', 'Walker', 18)

# 关键字参数
# register('Walker', 'male', 18)
# register(name='Walker', sex='male', age=18)

# positional argument follows keyword argument
# 混合使用位置实参必须跟在关键字实参后面（左边）
# register('Walker', 'male', 18)
# register(name='Walker', 'male', age=18)   # error

# 不能为一个形参重复传值
# register('male', name='Walker', age=18) # error

register('Walker', age=18, sex='male')	# correct

```

### 3.4 默认参数

在定义函数时，就已经为某些参数绑定值，称之为默认参数

注意：

1. 在定义阶段就已经有值，意味在调用阶段可以不用为其传值
2. 默认形参必须放到位置形参的后面
3. 默认形参的值只在定义阶段生效一次，在函数定义之后发生的改动无效
4. 默认形参的值通常应该是不可变类型

**默认形参vs位置形参**

默认形参：大多数情况值都一样

位置形参：大多情况值都是不一样的

**示例1**

```python
def foo(x, y, z=3):
    print(x, y, z)


foo(1, 2)
foo(1, 2, 4)
```

**示例2**

```python
def register(name, age, sex='female'):
    print("name：%s, age：%d, sex：%s" % (name, age, sex))


register("Jerry", 38)
register("Tom", 48)
register("Alex", 18, 'male')
```

**示例3**

```python
m = 10


def foo(x, y, z=m):
    print('x: %s' % x)
    print('y: %s' % y)
    print('z: %s' % z)


m = 1111
foo(1, 2)
```

**示例4**



**示例1**

```

# eg4:
def foo(name, hobby, store=[]):
    l.append(hobby)
    print('%s 的爱好是 %s' % (name, store))


foo('egon', 'read')
foo('alex', '吹牛逼')
foo('lxx', '腰子汤')


# eg5:
def foo(name, hobby, store=None):
    if store is None:
        store = []
    store.append(hobby)
    print('%s 的爱好是 %s' % (name, store))


store1 = []
foo('egon', 'read', store1)     # store1 =['read']
foo('egon', 'music', store1)    # store1 = ['read','music']
foo('egon', ' 吟诗', store1)
foo('alex', '吹牛逼')
foo('Jerry', '腰子汤')

"""

# 5. 可变长度的参数
"""
```

### 3.5 可变长度参数



### 3.6 命名关键字参数



### 3.7 常用形式



















