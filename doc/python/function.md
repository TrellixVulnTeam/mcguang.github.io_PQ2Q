## how to use function

#coding:utf-8  

`>>> collections.Counter('abcda') 
--> Counter({'a':2, 'c':1, 'b':1, 'd':1}) #use hashmap to calculate numbers of characters in a string

>>> sorted('dcba')
--> ['a', 'b', 'c', 'd'] # sorted a string

>>> letters = collections.defaultdict(int) # key --> value dictionary
>>> letters['a'] = 4 
>>> letters['a']
--> 4

>>> [False] * 5 # a good way to create repeat array
--> [False, False, False, False, False]

>>> 'the sky is blue'.split() # split a string to list ,default splict by ' '.
--> ['the', 'sky', 'is', 'blue']

>>>arr = [1,2,3] # array to string
>>>str = ','.join(str(i) for i in b)

>>> "".join('abcd')
--> 'abcd'

>>> " ".join(['blue','is','sky','the']) # string list to string
--> 'blue is sky the'

>>> A = 'abcd'
>>> A[::-1]  # [::-1] means reverse in python
--> 'dcba' 

>> id(3) # 查看每个对象的内存地址，即身份
-->29573416

>> 9.8 ** -7.2 # means pow(9.8, -7.2)
7.297468937055047e-08

>>> from __future__ import division # In python 2, 5/2 = 2. but in python 3, 5/2 = 2.5
>>> 5 / 2
2.5 

>>> divmod(5, 3) # 除了使用%求余数，还有内建函数divmod()——返回的是商和余数。
(1, 2)

>>> round(1.23377878,3) # 要实现四舍五入，很简单，就是内建函数：round()
1.234

>>> import math
>>> dir(math) # method in model math
['__doc__', '__file__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

>>> str(123) # number to string
'123'

>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter'] # enumerate function
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]


>>> lang = "study python"
>>> lang.index("p") # find index in string
6

>>> chr(97) # ascii number --> character 
'a'
>>> ord('a') # character --> ascii number
97

>>> "I like {0} and {1}".format("python", "canglaoshi")
'I like python and canglaoshi'

>>> "I like {0:10} and {1:>15}".format("python", "canglaoshi")
'I like python     and      canglaoshi'

>>> "I like {0:^10} and {1:^15}".format("python", "canglaoshi")
'I like   python   and   canglaoshi   '

>>> "I like {0:.2} and {1:^10.4}".format("python", "canglaoshi")
'I like py and    cang   '

>>> "I like {lang} and {name}".format(lang="python", name="canglaoshi")
'I like python and canglaoshi'

>>> "She is {0:4d} years old and the breast is {1:6.2f}cm".format(28, 90.1415926)
'She is   28 years old and the breast is  90.14cm'

>>> data = {"name":"Canglaoshi", "age":28}
>>> "{name} is {age}".format( **data) 
'Canglaoshi is 28'

>>> "python".isalpha()    #字符串全是字母，应该返回True
True
>>> "2python".isalpha()    #字符串含非字母，返回False
False	

>>> S = " hello "
>>> S.strip()：去掉字符串的左右空格
>>> S.lstrip()：去掉字符串的左边空格
>>> S.rstrip()：去掉字符串的右边空格

>>> a = 'Hao are you.'
>>> a = a.replace(" ","_")
>>> print a
Hao_are_you.

>>> repr([1,2,3]) #针对输入的任何对象返回一个字符串
'[1, 2, 3]'
>>> repr(1)
'1'
>>> repr({"lang":"python"})
"{'lang': 'python'}"

