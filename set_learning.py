# set的定义
# 只能存储不可修改变量 无序 变量唯一
# set的创建
set_1 = {1, 2, 3, 4, 5}
print("set_1: ", set_1, "type: ", type(set_1))
set_2 = set()
print("set_2: ", set_2, "type: ", type(set_2))
set_3 = set([1, 2, 3, 4, 5])
print("set_3: ", set_3, "type: ", type(set_3))
set_4 = set((1, 2, 3, 4, 5))
print("set_4: ", set_4, "type: ", type(set_4))
set_5 = set({"a": 1, "b": 2, "c": 3})
print("set_5: ", set_5, "type: ", type(set_5))

# 添加元素
set_1.add(6)
print("set_1: ", set_1)
# set_1.add([7, 8, 9]) # 报错，因为列表是可变类型

# 删除元素
set_1.remove(6)
print("set_1: ", set_1)
set_1.discard(6)
print("set_1: ", set_1)

# 集合运算
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
print("set_1 & set_2: ", set_1 & set_2)
print("set_1 | set_2: ", set_1 | set_2)
print("set_1 - set_2: ", set_1 - set_2)
print("set_1 ^ set_2: ", set_1 ^ set_2)

# 访问元素
for ele in set_1:
    print("ele: ", ele)