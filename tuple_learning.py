# tuple 的定义
# 不可修改

# tuple 的创建
tuple_1 = (1, 1.0, 1+5j, True, "tuple", (1,2,3), [1,2,3, (1,2)])
print("tuple_1: ", tuple_1, "type: ", type(tuple_1))
tuple_2 = 1, 2, 3
print("tuple_2: ", tuple_2, "type: ", type(tuple_2))
str_1 = "Hello"
tuple_3 = tuple(str_1)
print("tuple_3: ", tuple_3, "type: ", type(tuple_3))
list_1 = [1, 2, 3]
tuple_4 = tuple(list_1)
print("tuple_4: ", tuple_4, "type: ", type(tuple_4))
dict_1 = {1 : 5, "123" : "456", 2.0 : [1, 2, 3]}
tuple_5 = tuple(dict_1)
print("tuple_5: ", tuple_5, "type: ", type(tuple_5))
tuple_6 = tuple()
print("tuple_6: ", tuple_6, "type: ", type(tuple_6))

# 访问元素
print("tuple_1[0]: ", tuple_1[0], type(tuple_1[0]))
print("tuple_1[1]: ", tuple_1[1], type(tuple_1[1]))
print("tuple_1[2 : 4]: ", tuple_1[2 : 4], type(tuple_1[2 : 4]))

# 删除
del tuple_1