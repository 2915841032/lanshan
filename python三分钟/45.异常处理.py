# -*- coding: utf-8 -*-
# @File : 45.异常处理.py
# @Author : 阿波
# @Time : 2023/9/9 20:32
# @Software: PyCharm

# some_exceptions = [ValueError, TypeError, IndexError,IOError,WindowsError, None]
some_exceptions = [ValueError]

for choice in some_exceptions:
    try:
        print(f"抛出 {choice}")
        if choice:
            raise choice("有错误")
        else:
            print("顺利完成，没有异常")
    except ValueError as e:
        print("有一个ValueError")
        print(e)
    except TypeError:
        print("有一个TypeError")
        print(TypeError)
    except Exception as e:
        print(f"最后捕获其他异常: {e.__class__.__name__}")
    else:
        print("else里面的代码只有在没有异常的时候才执行！")
    finally:
        print("finally里的代码不管有没有异常都执行！")


try:
    x = int(input("请输入一个整数："))
    if x < 0:
        raise ValueError("输入的整数不能为负数")
    elif x == 0:
        raise ZeroDivisionError("输入的整数不能为零")
    else:
        result = 10 / x
        print("结果为:", result)
except ValueError as ve:
    print("捕获到值错误异常:", str(ve))
except ZeroDivisionError as ze:
    print("捕获到零除错误异常:", str(ze))
except Exception as e:
    print("捕获到其他异常:", str(e))