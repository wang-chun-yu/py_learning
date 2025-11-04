# 字典定义
'''
1. 键值对的形式
2. 键唯一、不可修改类型
'''
# 字典创建
# 1. 使用{}创建
dict_1 = {"name" : "张三", "age" : 18 , 123: "456", 2.0 : [123]}
print("dict_1: ", dict_1, "type: ", type(dict_1))
dict_2 = {}
print("dict_2: ", dict_2, "type: ", type(dict_2))
# 2. 使用fromkeys()创建
dict_3 = dict.fromkeys(["name", "age", "gender"], None)
print("dict_3: ", dict_3, "type: ", type(dict_3))
# 3. 使用dict()创建
dict_4 = dict(str1=1, str2=2.0, str3="123")
print("dict_4: ", dict_4, "type: ", type(dict_4))
demo = [("name", "张三"), ("age", 18)]
demo = (("name", "张三"), ("age", 18))
demo = [("name", "张三"), ["age", 18]]
demo = (("name", "张三"), ["age", 18])
dict_5 = dict(demo)
print("dict_5: ", dict_5, "type: ", type(dict_5))

# 字典访问
print("dict_1[\"name\"]: ", dict_1["name"])
print("dict_1.get(\"age\"): ", dict_1.get("age"))
print("dict_1.get(\"gender\"): ", dict_1.get("gender", "该键不存在"))

# 字典添加/修改元素
dict_1["gender"] = "男"
print("dict_1: ", dict_1, "type: ", type(dict_1))
dict_1["gender"] = "女"
print("dict_1: ", dict_1, "type: ", type(dict_1))

# 字典删除元素
del dict_1["gender"]
print("dict_1: ", dict_1, "type: ", type(dict_1))

dict_1.pop("gender")
print("dict_1: ", dict_1, "type: ", type(dict_1))
dict_1.pop("gender", "该键不存在")
print("dict_1: ", dict_1, "type: ", type(dict_1))

dict_1.popitem()
print("dict_1: ", dict_1, "type: ", type(dict_1))

# keys values items
print("dict_1.keys()", dict_1.keys(), "type: ", type(dict_1.keys()))
print("dict_1.values()", dict_1.values(), "type: ", type(dict_1.values()))
print("dict_1.items()", dict_1.items(), "type: ", type(dict_1.items()))

# keys values items转化为列表
keys_list = list(dict_1.keys())
values_list = list(dict_1.values())
items_list = list(dict_1.items())
print("keys_list: ", keys_list, "type: ", type(keys_list))
print("values_list: ", values_list, "type: ", type(values_list))
print("items_list: ", items_list, "type: ", type(items_list))

# 字典遍历
for key in dict_1.keys():
    print("key: ", key)
for value in dict_1.values():
    print("value: ", value)
for key, value in dict_1.items():
    print("key: ", key, "value: ", value)

# copy 深拷贝、浅拷贝
dict_6 = { "a" : 1, "b" : 2, "c" : [1 , 2, 3]}

# 删除字典
del dict_1
# print("dict_1: ", dict_1)