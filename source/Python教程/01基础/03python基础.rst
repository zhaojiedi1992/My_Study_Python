Python基础
====================================================================

数据类型
----------------------------------------------
- 整型
- 浮点
- 字符串
- 布尔 
- 空值


变量
----------------------------------------------

- 常量 
- 变量


字符编码
----------------------------------------------

- anscii: 8位作为一1B来表示一个字母
- unicode: 所有语言都编码进来。
- utf-8: 可变长编码, 字母使用1B存储， 汉字通常是3个位

python3 中，字符串使用的是unicode编码的， 是支持所有语言的。


转化
----------------------------------------------

.. code-block:: python 

   In [1]: '中文'.encode("utf-8")
   Out[1]: b'\xe4\xb8\xad\xe6\x96\x87'
   In [3]: b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8")
   Out[3]: '中文'


len函数
----------------------------------------------
对于str类型来说len计算的是字符数， 对于bytes类型来说len计算的是bytes数。


强制编码
----------------------------------------------
.. code-block:: python 

   #!/usr/bin/env python3
   # -*- coding: utf-8 -*-


字符串格式化
----------------------------------------------

.. code-block:: python 
      
      In [4]: print('%2d-%02d' % (3, 1))
   3-01

   In [5]:  'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
   Out[5]: 'Hello, 小明, 成绩提升了 17.1%'

   In [10]: print(f'show  {b} is {a:.2f}')
   show  abc is 1.00

list
----------------------------------------------

.. code-block:: python3

   In [12]: students=["zhao","qian","sun","li"]

   In [13]: students
   Out[13]: ['zhao', 'qian', 'sun', 'li']

   In [14]: students.append("zhou")

   In [15]: students
   Out[15]: ['zhao', 'qian', 'sun', 'li', 'zhou']

   In [16]: students.pop()
   Out[16]: 'zhou'

   In [17]: students
   Out[17]: ['zhao', 'qian', 'sun', 'li']

   In [18]: students[-1]="demo"

   In [19]: students
   Out[19]: ['zhao', 'qian', 'sun', 'demo']

   In [21]: students
   Out[21]: ['first', 'zhao', 'qian', 'sun', 'demo']


tuple
----------------------------------------------
因为tuple不可变，所以代码更安全

.. code-block:: python3

   In [22]: students = ("zhao","qian","sun")

   In [23]: students
   Out[23]: ('zhao', 'qian', 'sun')



if
----------------------------------------------

.. literalinclude:: ../../code/02.03.if.py
   :encoding: utf-8
   :language: python


match
----------------------------------------------
这个match类似其他语言的switch

.. literalinclude:: ../../code/02.03.match.py
   :encoding: utf-8
   :language: python

循环
----------------------------------------------

.. literalinclude:: ../../code/02.03.for.py
   :encoding: utf-8
   :language: python


dict
----------------------------------------------
高效的查找速度， 


set
----------------------------------------------
方便去重