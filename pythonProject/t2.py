# n=['s','d',1,200,'b','bb',2,50,'c','cc',4,50,'d','dd',600,70]
# # l = n[3::4]
# # print(max(l))
#
#
# def FindMaxChapterByPage(self):
#     # n = List_of_chapter
#     self.n = ['s', 'd', 1, 200, 'b', 'bb', 2, 50, 'c', 'cc', 4, 50, 'd', 'dd', 600, 70]
#     l = self.n[3::4]
#     print(max(l))
# FindMaxChapterByPage()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    n=['s','d',1,200,'b','bb',2,50,'c','cc',4,50,'d','dd',600,70]
    l=n[3::4]
    print(max(l))

p1 = Person("John", 36)
p1.myfunc()
