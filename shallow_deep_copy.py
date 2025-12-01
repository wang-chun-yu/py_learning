# 深拷贝、浅拷贝
# 深拷贝
import copy
list_1 = [1, 2, 3, 4, 5]
list_1.append(list_1)

print(list_1)
print(list_1[5])
print("list_1 id: ", id(list_1))
print("list_1[5] id: ", id(list_1[5]))

list_2 = copy.deepcopy(list_1)
print(list_2)
print(list_2[5])
print("list_2 id: ", id(list_2))
print("list_2[5] id: ", id(list_2[5]))