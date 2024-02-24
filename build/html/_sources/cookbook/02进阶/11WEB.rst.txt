WEB编程
====================================================================

作为客户端与HTTP服务交互
----------------------------------------------
通常使用 urllib.request 模块就够了.当然也是可以使用 requests 库的。



.. code-block:: python 

   from urllib import request, parse

   # Base URL being accessed
   url = 'http://httpbin.org/get'

   # Dictionary of query parameters (if any)
   parms = {
      'name1' : 'value1',
      'name2' : 'value2'
   }

   # Encode the query string
   querystring = parse.urlencode(parms)

   # Make a GET request and read the response
   u = request.urlopen(url+'?' + querystring)
   resp = u.read()

创建TCP服务器
----------------------------------------------

.. literalinclude:: ../../code/cookbook/11.tcp.server.py
   :encoding: utf-8
   :language: python

创建UDP服务器
----------------------------------------------

.. literalinclude:: ../../code/cookbook/12.udp.server.py
   :encoding: utf-8
   :language: python

通过CIDR地址生成对应的IP地址集
----------------------------------------------

.. code-block:: python 

   In [7]: import ipaddress

   In [8]: net = ipaddress.ip_network('123.45.67.64/27')

   In [9]: net[0]
   Out[9]: IPv4Address('123.45.67.64')

   In [10]: net[10]
   Out[10]: IPv4Address('123.45.67.74')

通过XML-RPC实现简单的远程调用
----------------------------------------------

.. literalinclude:: ../../code/cookbook/12.udp.server.py
   :encoding: utf-8
   :language: python
