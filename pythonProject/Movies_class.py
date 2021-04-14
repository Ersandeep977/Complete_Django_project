class Movie:
    ''' Movies class developed by Sandeep for Python Demo Purpose'''
    def __init__(self,title,hero,heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print('Movie Name:-',self.title)
        print('hero Name:-',self.hero)
        print('heroine:-',self.heroine)

list_of_Movies=[]
while True:
    titel=input('enter Movies Name: ')
    hero=input('enter Hero Name: ')
    heroine=input('enter Heroine Name: ')
    m=Movie(titel,hero,heroine)
    list_of_Movies.append(m)
    print('Movies add the list suceesfully')
    option=input('Do you want to add one movie [Yes|No]: ')
    if option.lower() == 'no':
        break
print('#'*40)
print('All MOvies Information....')
print('#'*40)
for movie in list_of_Movies:
    movie.info()