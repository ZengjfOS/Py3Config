# Py3Config
使用Python3默认配置解析器解析配置文件，采用单例模式创建多文件可访问全局对象。

## 文件结构

```
  .
  ├── config.conf             # 配置文件
  ├── Configures.py           # 配置文件解析
  ├── LocalConfig.py          # 配置文件中本地配置类
  └── RemoteConfig.py         # 配置文件中远程配置类
```

## 测试

* 测试代码

```
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
