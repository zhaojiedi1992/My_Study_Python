环境准备
====================================================================

mac安装python
----------------------------------------------

.. code-block:: bash 

    brew install python3


环境配置
----------------------------------------------

.. code-block:: bash 

    # 安装虚拟环境
    python3 -m venv venv 
    # 激活虚拟环境
    source ./venv/bin/activate
    # 安装ipython
    pip install ipython 

python解释器
----------------------------------------------

python解释器是用来解释.py文件的， 根据实现语言主流的有

- Cpython: 主流 c写的
- Jpython: java 写的
- IronPython: .net 写的

.. note:: cpython这个是解释器自身是c写的， 我们还是写的python文件，只是使用这个解释器来解释代码。
    

