# # class Mynumber:
# #     Number = "Natural"
# #     def __init__(self,value):
# #         self.value = value
# #     def print_value(self):
# #         print(self.value)
# # obj1 = Mynumber([1,2,3,4,5,5,6])
# # obj1.print_value()
# #
# #
# #
# # s = "test"
# # count = 0
# # for i in s:
# #     if "t" in  i:
# #         count+=1
# # print(count)
#
# #
# # # Syntax Error (Error)
# # print("Hello world"  # Missing closing parenthesis
#
# # ZeroDivisionError (Exception)
# # n = 10
# # res = n / 0
#
# # try:
# #     a = 10
# #     b = 0
# #     res = a / b
# # except ZeroDivisionError  as e:
# #     print("we cannot divied by zero :" ,e)
# # try:
# #     a = 10
# #     b = 20
# #     assert  a == b
# # except AttributeError :
# #     print("a is not equal to b")
# a = 5
# b = int("sachin")
# print(a *b) # NameError
from os import remove

# d1 = { "name": "Prajjwal", 1: "Python", (1, 2): [1,2,4] }
# d2 = {2:"Java"}
# print(d1 | d2)
# d1.update(d2)
# print(d1)

# numbers = [10,20,30,40]
# del numbers[1:3]
# print(numbers)

# def fun():
#     try:
#         return  1
#     finally:
#         return 2
# print(fun())
# greet ="hello"
# name = "world"
# msg = greet.upper() +" "+ name.capitalize()
# print(msg)

# with open("test.txt","r") as file:
#     content = file.read()
#     print(content)
#     file.close()
#
# with open("test.txt","r") as file:
#     content = file.read()
#     print(content)
#     file.close()

# with open("test.txt","w") as file:
#     file.write("This is new line")
#     file.close()
#
# with open("test.txt","a") as file:
#     file.write("This is append line")
#     file.close()
#
# with open("test.txt", "r") as file:
#     content = file.read()
#     print(content)
#     file.close()


# num = [1,2,3,4,5]
# even = []
# for i in num:
#     if i % 2 == 0:
#         even.append(i)
# print(list(even))


# sq = map(lambda x : x*2 ,num)
# print(list(sq))

# d = [{ "name": "Prajjwal", 1: "Python", (1, 2): [1,2,4] }, {2:"Java",5 : "Python"}]
# print(d[1][5])

# num = [1,2,3,4,5]
# even = list(filter(lambda x : x%2 == 0, num))
# print(even)
#
# import requests
#
# response = requests.get("https//:google.com")
# assert response.status_code == 200

# s = "This is name of God"
# rem_spc = s.replace(" ", "")
# rev = rem_spc[::-1]
#
# print(s)
# print(rem_spc)
# print(rev)

# r = lambda q: q*2
# s = lambda q: q*3
# x =2
# x =r(x)
# x = s(x)
# x = r(x)
# print(x)

a = 12.5
b = 2
print(a//b)







