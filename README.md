# Py3Config
使用Python3默认配置解析器解析配置文件，采用单例模式创建多文件可访问全局对象。

## 文件结构

```
.
├── configure
│   ├── Configures.py
│   ├── __init__.py
│   ├── LocalConfig.py
│   └── RemoteConfig.py
├── config.conf
├── main.py
└── run.log

```

## 测试

* 测试代码

```
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # Copyright (c) 2016 - zengjf <zengjf42@163.com>
    
    from configure.Configures import *
    
    if __name__ == '__main__':
    
        print(Configures())
        print(Configures())
        print(configures)
```

* 输出信息：

```
    < __main__.Configures object at 0x7f7404fb3240 >
    < __main__.Configures object at 0x7f7404fb3240 >
    < __main__.Configures object at 0x7f7404fb3240 >
```
