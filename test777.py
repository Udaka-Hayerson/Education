#
# class Point:
#     def __init__(self, weight_lenght_height = [10, 10, 10]):
#         self.weight_lenght_height = weight_lenght_height
#
#
#     def reLoad(self, weight_lenght_height, aaa = 10, bbb = 20, ccc = 30):
#         weight_lenght_height[0] += aaa
#         weight_lenght_height[1] += bbb
#         weight_lenght_height[2] += ccc
#         tup = tuple(weight_lenght_height)
#         return tup
#
#
# a = int(input('weight = '))
# b = int(input('lenght = '))
# c = int(input('height = '))
#
# aaa = int(input('REweight = '))
# bbb = int(input('Relenght = '))
# ccc = int(input('REheight = '))
#
# coords1 = Point()
# coords2 = Point([c, b, a])
# coords3 = Point([c, a, b])
# coords40 = Point([100, 200, 300])
#
#
# tuple_coords1 = coords1.reLoad(coords1.weight_lenght_height)
# tuple_coords2 = coords2.reLoad(coords2.weight_lenght_height, ccc, bbb, aaa)
# tuple_coords3 = coords3.reLoad(coords3.weight_lenght_height, ccc, aaa, bbb)
# tuple_coords40 = coords40.reLoad(coords40.weight_lenght_height, aaa + 1000, bbb + 2000, ccc + 3000)
#
# print(tuple_coords1, type(tuple_coords1))
# print(tuple_coords2, type(tuple_coords2))
# print(tuple_coords3, type(tuple_coords3))
# print(tuple_coords40, type(tuple_coords40))
#
# x = True
# while x:
#     value =  int(input('please enter your number '))
#     if not value % 7:
#         print('This number is a multiple of seven')
#         x = False
#     else:
#         print('This number is NOT a multiple of seven')
#         yes_no = input('Press \"Y\" if you want continue , or\"N\" if you want break search ')
#         if yes_no.lower() == 'y':
#             continue
#         else:
#             break
# else:
#     print('you found the required number')
# print('End')
#
# class Cat:
#
#     def __init__(self, name, breed = 'dvorovoy', age = 13, color = 'dirty white'):
#         self.name = name
#         self.breed = breed
#         self.age = age
#         self.color = color
#
#
#
# mursic = Cat('Mursic',)
# manan = getattr(mursic, 'name')
# mana = getattr(mursic, 'breed')
# man = getattr(mursic, 'age')
# ma = getattr(mursic, 'color')
# print(manan, mana, man, ma, sep='\n')
#
# from datetime import datetime as dt
#
# class Player:
#
#     __LVL, __HEALTH = 1, 100
#     __slots__ = ['__lvl', '__health', '__born']
#
#     def __init__(self):
#         __lvl = Player.__LVL
#         __health = Player.__HEALTH
#         __born = dt.now()
#
#     def get_lvl(self):
#         return self.__lvl
#
#     def set_lvl(self, numeric):
#         self.__lvl += numeric
#
#
# x = Player()
# print(x.get_lvl())
#
#
# class Animal:
#     # !! Your home task
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print('Hello I\'m - ', self.name)
#
# class Dog(Animal):
#     def __init__(self, name, ear = 2):
#         super(Dog, self).__init__(name)
#         self.ear = ear
#
#     def baww(self):
#         print('baw baw baw')
#
# class Fish(Animal):
#     def __init__(self, name, tail):
#         super(Fish, self).__init__(name)
#         self.tail = tail
#
#     def boolbool(self):
#         print('Bool bool')
#
#
#
#
# nemo = Fish('Nemo', 2.5) # Nemo_001
# nemo.boolbool()
# nemo.speak()
#
# sharic = Dog('ShariC', 4) # Sharic_001
# sharic.baww()
# sharic.speak()
#
#
# class Animal:
#     # !! Your home task
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print('Hello I\'m - ', self.name)
#
# class Dog(Animal):
#     def __init__(self, name, ear = 2):
#         super(Dog, self).__init__(name)
#         self.ear = ear
#
#     def baww(self):
#         s = ''
#         if self.ear > 1:
#             s = 'tails'
#         else:
#             s = 'tail'
#         print(f'{self.name} have a {self.ear} {s}')
#
# class Fish(Animal):
#     def __init__(self, name, tail):
#         super(Fish, self).__init__(name)
#         self.tail = tail
#
#     def boolbool(self):
#         s = ''
#         if self.tail > 1:
#             s = 'tails'
#         else:
#             s = 'tail'
#
#         print(f'{self.name} has {self.tail} {s}')
#
#
#
#
# nemo = Fish('Nemo', 1) # Nemo
# nemo.boolbool()
# nemo.speak()
#
# sharic = Dog('Sharic', 1) # Sharic
# sharic.baww()
# sharic.speak()
#
# def mul_two(a: int, b: int) -> int :
#     return a * b
#
# def mul_three(a, b, c):
#     return a * b * c
# print(mul_two(30,20))
# print(mul_three(2, 3, 5))
# ###
# ###
# ###
# ###
# ###
# def first_word(text: str) -> str:
#     result = text.split()
#     return result[0]
#
#
# print("Example:")
# print(first_word("Hello world"))
# print(first_word("world Hello"))
# print(first_word("Hello world world world world"))
#
# def is_acceptable_password(password: str) -> bool:
#     if len(password) > 6:
#         return True
#     else:
#         return False
#     # return len(password) > 6
#
# print(is_acceptable_password('short'))
# print(is_acceptable_password('muchlonger'))
# print(is_acceptable_password('ashort'))
# print(is_acceptable_password('ashortgyg'))
# print(is_acceptable_password('ash'))
# print(is_acceptable_password('ashjhfjffh'))
#
# def number_length(a):
#     count = 0
#     a = str(a)
#     for x in a:
#         count += 1
#     return count
#     #return len(str(a))
#
# print("Example:")
# print(number_length(10) ,number_length(1010), number_length(0), number_length(44444), sep='---')
#
# def end_zeros(num: int) -> int:
#     num = str(num)
#     flag = 0
#     for i in num[::-1]:
#         i = int(i)
#         if not i:
#             flag += 1
#             if len(num) == 1:
#                 return flag
#         else:
#             return flag
#
#
# print(end_zeros(100000), end_zeros(10000), end_zeros(1000), end_zeros(100), end_zeros(0), end_zeros(1),
#       sep=' and ', end=' Shatle Misiooon - Start!')
#
#
# def remove_all_before(items, border):
#     if not border in items:
#         return items
#     if items == []:
#         return items
#     if items[0] == border:
#         return items
#     cnt = 0
#     for i in items:
#         if i == border:
#             return items[cnt:]
#         cnt += 1
#
#
#
# print("Example:")
# print(list(remove_all_before([1, 2, 3, 4, 5], 3)),
#       list(remove_all_before([1, 1, 2, 2, 3, 3], 2)),
#       list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)),
#       list(remove_all_before([1, 1, 5, 6, 7], 2)),
#       list(remove_all_before([], 0)),
#       list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)), sep= '\n')
#
# str_00 = 'abcdabcdab'
# str_01 = 'abcdabcda'
# str_02 = 'abcdabcd'
# str_03 = 'abcdabc'
# str_04 = 'abcdab'
# str_05 = 'abcda'
# str_06 = 'abcd'
# str_07 = 'fur'
# def split_pairs(a):
#     l = []
#     for i in range(0,len(a)):
#         if a == '':
#             break
#         if len(a) == 1:
#             l.append(a + '_')
#             break
#         x = a[0:2]
#         l.append(x)
#         a = a[2: len(a)]
#     return l
#
# print(split_pairs(str_00))
# print(split_pairs(str_01))
# print(split_pairs(str_02))
# print(split_pairs(str_03))
# print(split_pairs(str_04))
# print(split_pairs(str_05))
# print(split_pairs(str_06))
# print(split_pairs(str_07))
#
# str_00 = '000000007'
# str_01 = '0000006'
# str_02 = '000005'
# str_03 = '00004'
# str_04 = '0003'
# str_05 = '002'
# str_06 = '01'
# str_07 = '1'
# def beginning_zeros(number):
#     count = 0
#     for i in number:
#         if int(i) == 0:
#             count += 1
#         else:
#             break
#     return count
#
# print(beginning_zeros(str_00))
# print(beginning_zeros(str_01))
# print(beginning_zeros(str_02))
# print(beginning_zeros(str_03))
# print(beginning_zeros(str_04))
# print(beginning_zeros(str_05))
# print(beginning_zeros(str_06))
# print(beginning_zeros(str_07))
#
#
# def nearest_value(values: set, one: int) -> int:
#     judge = 0
#     referee = 0
#     result = 0
#     for i in values:  # one магнит --- i ближайшее (но меньшее)
#         if i - one == 0:
#             return i
#         if one - i < 0:
#             judge = (one - i) * -1
#         elif one - i > 0:
#             judge = one - i
#
#         if judge < referee or referee == 0:
#             referee = judge
#             if not one - referee in values:
#                 result = i
#             else:
#                 result = one - referee
#     return result
#
# print(nearest_value({4, 7, 10, 11, 12, 17}, 9)) #== 10
# print(nearest_value({4, 7, 10, 11, 12, 17}, 8)) #== 7
# print(nearest_value({4, 8, 10, 11, 12, 17}, 9)) #== 8
# print(nearest_value({4, 9, 10, 11, 12, 17}, 9)) #== 9
# print(nearest_value({4, 7, 10, 11, 12, 17}, 0)) #== 4
# print(nearest_value({4, 7, 10, 11, 12, 17}, 100)) #== 17
# print(nearest_value({5, 10, 8, 12, 89, 100}, 7))   #==8
# print(nearest_value({-1, 2, 3}, 0))   #==-1
# print(nearest_value({0, -2}, -1))  #==-2
#
# def sum_numbers(text: str) -> int:
#     list_str = text.split()
#     fin = 0
#     for x in list_str:
#         if x.isdigit():
#             fin += int(x)
#     return fin
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(sum_numbers('hi'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert sum_numbers('hi') == 0
#     assert sum_numbers('who is 1st here') == 0
#     assert sum_numbers('my numbers is 2') == 2
#     assert sum_numbers('This picture is an oil on canvas '
# 'painting by Danish artist Anna '
# 'Petersen between 1845 and 1910 year') == 3755
#     assert sum_numbers('5 plus 6 is') == 11
#     assert sum_numbers('') == 0
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#
# def checkio(array) -> int:
#     count = 0
#     result = 0
#     if not array:
#         return 0
#     for i in array:
#         if count % 2 == 0 or count == 0:
#             result += i
#         count += 1
#     result *= array[len(array) - 1]
#     return result
#
#
# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     print('Example:')
#     print(checkio([0, 1, 2, 3, 4, 5]))
#     print(checkio([1, 2]))
#     print(checkio([6]))
#
#     assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
#     assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
#     assert checkio([6]) == 36, "(6)*6=36"
#     assert checkio([]) == 0, "An empty array = 0"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
#
# def checkio(words: str) -> bool:
#     li_st = words.split()
#     cnt = 0
#     for s in li_st:
#         if s.isalpha():
#             cnt += 1
#             if cnt >= 3:
#                 return True
#
#         else:
#             cnt = 0
#     return False
#
#
# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     print('Example:')
#     print(checkio("Hello World hello"))
#
#     assert checkio("Hello World hello") == True, "Hello"
#     assert checkio("He is 123 man") == False, "123 man"
#     assert checkio("1 2 3 4") == False, "Digits"
#     assert checkio("bla bla bla bla") == True, "Bla Bla"
#     assert checkio("Hi") == False, "Hi"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
#
#
# def left_join(phrases: tuple) -> str:
#     r = ''
#     phrases = list(phrases)
#     for i in phrases:
#         if 'right' in i:
#             r += i.replace('right', 'left')
#             r += ','
#         else:
#             r += (i + ',')
#     return r[:len(r)-1]
#
#
# if __name__ == "__main__":
#     print("Example:")
#     print(left_join(("left", "right", "left", "stop")))
#
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert (
#         left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
#     ), "All to left"
#     assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
#     assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
#     assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
#
#
#
# def first_word(text: str) -> str:
#     str_x = ''
#     count = 0
#     for x in text:
#         count += 1
#         if text.isalpha():
#             return text
#         if x.isalpha() or '\'' and x != '.' and x != ' ':
#             str_x += x
#             if count == len(text): #count = 4  len = 4
#                 return str_x
#             elif not text[count].isalpha():
#                 if text[count] != '\'':
#                     return str_x
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(first_word("Hello world"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert first_word("Hello world") == "Hello"
#     assert first_word(" a word ") == "a"
#     assert first_word("don't touch it") == "don't"
#     assert first_word("greetings, friends") == "greetings"
#     assert first_word("... and so on ...") == "and"
#     assert first_word("hi") == "hi"
#     assert first_word("Hello.World") == "Hello"
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#
#
# import datetime as dt
#
# def days_diff(a, b):
#     count = 0
#     one, two, three = a[0], a[1], a[2]
#     four, five, six = b[0], b[1], b[2]
#     start_date = dt.datetime(one, two, three)
#     end_date = dt.datetime(four, five, six)
#     if start_date == end_date:
#         return  0
#     total_days = (end_date - start_date).days
#     for x in range(total_days):
#         count += 1
#     if count == 0:
#         for x in range(total_days - 1, -1):
#             count += 1
#     return count
#
# # print(days_diff((1982, 4, 19), (1982, 4, 22)))
# # print(days_diff((2014, 1, 1), (2018, 8, 27)))
# # print(days_diff((2001, 12, 1), (2001, 11, 1)))
#
# if __name__ == "__main__":
#     print("Example:")
#     print(days_diff((1982, 4, 19), (1982, 4, 22)))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
#     assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
#     assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
#     print("Coding complete? Click 'Check' to earn cool rewards!")