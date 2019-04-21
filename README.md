爬虫项目框架
===============================
面向对象的设计，主要用来学习和交流，轻量级的小框架，上手很容易

目录结构
-------------------
```
config		            包含所有的数据库配置文件
    db_config.py            主配制文件
    db_config_dev.py        开发环境配制文件
    db_config_test.py       测试环境配制文件
    db_config_pro.py        生产环境配制文件
data 		            包含所有的默认数据
    mysql_data.sql 	    mysql库中表的默认结构和数据
scr 		            包含当前项目的主要应用程序文件
    xiaoshuo.py 	    小说爬虫简单示例
    ...		            所有其它业务逻辑的爬虫程序都放在这里
tools			    包含所有的工具
    db_mysql.py             mysql数据库的操作类
    function.py 	            常用函数的操作类
library.txt 		    环境依赖的库
test_db.py 		    测试数据库的连接文件
```

环境搭建说明
-------------------
```
安装python环境：
    参考文档 https://www.runoob.com/python/python-install.html
    建议安装 **python3.7.2** 版本
    数据库 **Mysql5.6.40**

安装程序依赖库：
    pip install -r library.txt

在mysql数据库中创建你的数据库，比如：db_data
    把 data/mysql_data.sql 中的表测试表导入到 mysql 中 db_data 数据库里
```
常见问题
-------------------
```
Q: 安装过程中遇到模块不存在怎么办？
A: 使用命令 pip install 缺少的模块名

Q: 安装后如何确认安装是否成功？
A: 在项目根目录下执行 **python test_db.py** 如果看到 **Congratulations!**表示安装成功。

Q: 如何执行我的项目文件？
A: 在项目根目录执行 **python main.py**

Q: 使用过程中遇到化佷长时间都解决不了的问题怎么办？
A: 加QQ号：153600916 和我讨论
```


