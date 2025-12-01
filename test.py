d_list = [(x, y) for x in range(5) for y in range(4)]
# d_list列表包含20个元素
print(d_list)

# a为元组生成器，遍历后原生撑起对象将不复存在
a = (x for x in range(1,10))
for i in a:
    print(i,end=' ')
print(tuple(a))

#全局函数
def outdef ():
    name = "所在函数中定义的 name 变量"
    #局部函数
    def indef():
        nonlocal name
        print(name)
        #修改name变量的值
        name = "局部函数中定义的 name 变量"
        print(name)
        return name
    return indef()
#调用全局函数
outdef()

class CLanguage:
    @staticmethod
    def info(name,add):
        print(name,add)

#使用类名直接调用静态方法
CLanguage.info("C语言中文网","http://c.biancheng.net")
#使用类对象调用静态方法
clang = CLanguage()
clang.info("Python教程","http://c.biancheng.net/python")