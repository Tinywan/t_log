这是一个简单的python日志包

环境
```
python > 3.5
```

安装
```
pip install t_log
```

如何使用
```python
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

## 打包

#### 生成包

* 安装 `setuptools`并 `wheel` 安装了最新版本
    ```
    python3 -m pip install --user --upgrade setuptools wheel
    ``` 
* 现在从 `setup.py` 位于的同一目录运行此命令 
    ```
    python3 setup.py sdist bdist_wheel
    ```
* 以上命令应输出大量文本，一旦完成，应在dist目录中生成两个文件
    ```
    dist/
    example_pkg-0.0.1-py3-none-any.whl
    example_pkg-0.0.1.tar.gz
    ```
该`tar.gz`文件是源存档，而该`.whl`文件是构建的分发。较新的pip版本优先安装构建的发行版，但如果需要，将回退到源代码存档。您应该始终上传源存档并为项目兼容的平台提供构建的存档。在这种情况下，我们的示例包在任何平台上都与Python兼容，因此只需要一个构建的发行版。   

#### 发布包 

使用twine上传分发包。 你需要安装Twine：
```
python3 -m pip install --user --upgrade twine
```
> 如果是Windows 清配置环境变量，重新打开 

重新打包
```
python3 setup.py sdist bdist_wheel
```

运行Twine上传所有存档dist

```
PS D:\Git\t_log> twine upload  dist/*
```
系统将提示您输入使用Test PyPI注册的用户名和密码。命令完成后，您应该看到与此类似的输出
```
Enter your username: Tinywan
Enter your password:
Uploading distributions to https://upload.pypi.org/legacy/
Uploading t_log-0.51-py3-none-any.whl
 76%|██████████████████████████████████████████████████████████████████████████
100%|██████████████████████████████████████████████████████████████████████████
█████████████████████████████████████| 10.5k/10.5k [00:03<00:00, 3.31kB/s]
Uploading t_log-0.51.tar.gz
100%|██████████████████████████████████████████████████████████████████████████
█████████████████████████████████████| 9.50k/9.50k [00:01<00:00, 9.24kB/s]
```
>注意:如果您收到错误消息，则需要为您的包选择一个唯一的名称。一个不错的选择 。更新参数 ，删除文件夹，然后 重新生成存档。`The user '[your username]' isn't allowed to upload to project 'example-pkg'example_pkg_your_usernamenamesetup.pydist`

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

## 使用Docker+Jenkins自动构建部署
