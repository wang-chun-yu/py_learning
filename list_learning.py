# 列表的定义
# 可由：整数、浮点数、复数、布尔值、字符串、列表、字典、元组、集合组成
list_1 = [1, "1.0", 1 + 5j, True, "list", [1,2,3], {1:2, "3":4}, (1,2,3), {1,2,3}]
print ("list_1: ", list_1, "type: ", type(list_1))

print ("list_1[0]: ", list_1[0], "type: ", type(list_1[0]))
print ("list_1[1]: ", list_1[1], "type: ", type(list_1[1]))
print ("list_1[2]: ", list_1[2], "type: ", type(list_1[2]))
print ("list_1[3]: ", list_1[3], "type: ", type(list_1[3]))
print ("list_1[4]: ", list_1[4], "type: ", type(list_1[4]))
print ("list_1[5]: ", list_1[5], "type: ", type(list_1[5]))

print ("list_1[-1]: ", list_1[-1], "type: ", type(list_1[-1]))
print ("list_1[-2]: ", list_1[-2], "type: ", type(list_1[-2]))
print ("list_1[-3]: ", list_1[-3], "type: ", type(list_1[-3]))
print ("list_1[-4]: ", list_1[-4], "type: ", type(list_1[-4]))
print ("list_1[-5]: ", list_1[-5], "type: ", type(list_1[-5]))
print ("list_1[-6]: ", list_1[-6], "type: ", type(list_1[-6]))

# 列表添加元素
list_1.append([4,5,6])
list_1.extend([7,8,9])
list_1.insert(0,[10,11,12])
print("list_1: ", list_1)

# 列表删除元素
del list_1[0]
print("list_1: ", list_1)

del list_1[0 : 2]
print("list_1: ", list_1)

del list_1[0 : 5 : 2]
print("list_1: ", list_1)

list_1.pop
print("pop list_1: ", list_1)

list_1.remove([1,2,3])
print("remove list_1: ", list_1)

list_1.clear()
print("clear list_1: ", list_1)

# 列表访问元素
list_1 = [1,2,3,4,5,6,7,8,9,10]
print("list_1[0 : 10]", list_1[0 : 10]);
print("list_1[0 : 5 : 2]", list_1[0 : 5 : 2]);
print("list_1[-10 : -1]", list_1[-10 : -1]);
print("list_1[-10 : 0]", list_1[-10 : 0]);
print("list_1[-1 : -10]", list_1[-1 : -10]);

# 列表查找元素
print("list_1.index(1): ", list_1.index(1));
print("list_1.index(5, 0, 5): ", list_1.index(5, 0, 5));
# print("list_1.index(5, 0, 5): ", list_1.index(5, 0, 4));
print("list_1.count(1): ", list_1.count(1));