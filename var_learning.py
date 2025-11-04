# 变量的类型、定义、赋值
num_1 = 1
num_2 = 2.0
num_3 = 1 + 5j
num_4 = "ture"
num_5 = False

print ("num_1: ", num_1, "type: ", type(num_1))
print ("num_2: ", num_2, "type: ", type(num_2))
print ("num_3: ", num_3, "type: ", type(num_3))
print ("num_4: ", num_4, "type: ", type(num_4))
print ("num_5: ", num_5, "type: ", type(num_5))

# 变量的地址、相等性
num_6 = 1
num_7 = 1
print ("num_6: ", num_6, "type: ", type(num_6), "address: ", id(num_6))
print ("num_7: ", num_7, "type: ", type(num_7), "address: ", id(num_7))
print ("num_6 is num_7: ", num_6 is num_7)
print ("num_6 == num_7: ", num_6 == num_7)

num_7 = 2
print ("num_7: ", num_7, "type: ", type(num_7), "address: ", id(num_7))
print ("num_6 is num_7: ", num_6 is num_7)
print ("num_6 == num_7: ", num_6 == num_7)

# 变量的生命周期
num_8 = 1
print ("num_8: ", num_8, "type: ", type(num_8), "address: ", id(num_8))
del num_8
#print ("num_8: ", num_8, "type: ", type(num_8), "address: ", id(num_8)) # 这里会报错，因为num_8已经不在作用域内

# 变量的运算
# 1. 整数计算
num_9 = 1 + 2 - 3 * 4 
print ("num_9: ", num_9, "type: ", type(num_9))

num_10 = 10 / 5
print ("num_10: ", num_10, "type: ", type(num_10))

num_11 = 10 // 5
print ("num_11: ", num_11, "type: ", type(num_11))

num_12 = 10 / 4 
print ("num_12: ", num_12, "type: ", type(num_12))

num_13 = 10 // 4
print ("num_13: ", num_13, "type: ", type(num_13))

num_14 = 10 % 4
print ("num_14: ", num_14, "type: ", type(num_14))

num_15 = 10 ** 2
print ("num_15: ", num_15, "type: ", type(num_15))

num_16 = 9 ** 0.5
print ("num_16: ", num_16, "type: ", type(num_16))

num_17 = 1 ** -2
print ("num_17: ", num_17, "type: ", type(num_17))

# 2. 浮点数计算
num_18 = 1.0 + 2.0 - 3.0 * 4.0
print ("num_18: ", num_18, "type: ", type(num_18))

num_19 = 10.0 / 2.0
print ("num_19: ", num_19, "type: ", type(num_19))

num_20 = 10.0 // 3.0
print ("num_20: ", num_20, "type: ", type(num_20))

num_21 = 10.0 % 4.5
print ("num_21: ", num_21, "type: ", type(num_21))

# 3. 复数计算

# 4. 字符串计算
str_1 = "Hello"
str_2 = "World"
str_3 = str_1 + " " + str_2
print ("str_3: ", str_3, "type: ", type(str_3))
str_3 = str_3 * 2
print ("str_3: ", str_3, "type: ", type(str_3))
str_3 = str_3.upper()
print ("str_3: ", str_3, "type: ", type(str_3))
str_3 = str_3.lower()
print ("str_3: ", str_3, "type: ", type(str_3))
str_3 = str_3.capitalize()
print ("str_3: ", str_3, "type: ", type(str_3))

