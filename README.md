# Example Package

This is a simple log package. You can use

安装
```
pip install t_log
```

如何使用
```
#!/usr/bin/python3

from t_log import logger

log = logger.logger()

log.critical("这是一个 critical 级别的问题！")
log.error("这是一个 error 级别的问题！")
log.warning("这是一个 warning 级别的问题！")
log.info("这是一个 info 级别的问题！")
log.debug("这是一个 debug 级别的问题！")
```

#### 教程  
官方文档 ：https://packaging.python.org/tutorials/packaging-projects/#uploading-your-project-to-pypi
```
twine : 无法将“twine”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。
```
> 配置环境变量 `C:\Users\tinyw\AppData\Roaming\Python\Python37\Scripts`

https://pypi.org/manage/account/
```
HTTPError: 403 Client Error: Invalid or non-existent authentication information. for url: https://test.pypi.org/legacy/
```

```
UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 197: illegal multibyte sequence
```
* 解决办法1：`FILE_OBJECT= open('order.log','r', encoding='UTF-8')`
* 解决办法2：`FILE_OBJECT= open('order.log','rb')`

使用twine上传分发包。 你需要安装Twine：
```
python3 -m pip install --user --upgrade twine
```
> 如果是Windows 清配置环境变量，重新打开 

重新打包
```
python3 setup.py sdist bdist_wheel
```
上传并完成发布
使用 twine
```
twine upload  dist/*
```

包发布完成后，其他人只需要使用pip就可以安装你的包文件。比如
```
pip install package-name
```

包发布完成后，其他人只需要使用pip就可以安装你的包文件。比如
```
pip install package-name --upgrade
```

#### 如何使用
* 安装
```
pip install t_log
```

* 升级包
```
pip install --upgrade  t_log 
```

* 卸载包
```
pip uninstall t_log
```

* 搜索
```
pip search t_log
```


* 升级pip本身
```
pip install --upgrade pip
```

可能遇到的错误
