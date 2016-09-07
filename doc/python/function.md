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


