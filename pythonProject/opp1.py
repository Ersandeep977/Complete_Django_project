# class test:
#     def __init__(self):
#         print("constructor calling....")
# t1=test()
# t2=test()
# t3=test()
# t4=test()

# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
# S1 = Student(1,2,3)
# S2 = Student(1,2,3)
# print(S1)
# print(S2)

# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
# S1 = Student(1,2,3)
# print(S1)
# Student(7,8,9)

# class Test:
#     def m1(self):
#         print('method execution....')
# t=Test()
# t.m1()

# class Test:
#     def __init__(self):
#         print('constuctor ......',id(self))
# t=Test()
# t.__init__()
# t.__init__()
# t.__init__()
# t.__init__()

# class Test:
#     def __init__(self):
#         print('no-arg constructor..')
#
#     def __int__(self,x):
#         print('one-arg constructor..')
# t=Test()

# class Test():
#     def __init__(self,name):
#         self.name=name
# class Demo:
#     def __init__(self,name):
#         self.name=name
# t=Test('sunny')
# d=Demo('Sachin')
# t.__init__('Bunny')
# d.__init__('Dravid')

# class Hello:
#     print('hello')
# Hello()
# Hello()

# class Test:
#     @classmethod
#     def m1(cls):
#         print(id(cls))
#
#     @classmethod
#     def m2(cls):
#         print(id(Test))
# print(id(Test))
# Test.m1()
# Test.m2()