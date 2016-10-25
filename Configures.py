#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2016 - zengjf <zengjf42@163.com>

from LocalConfig import LocalConfig
from RemoteConfig import RemoteConfig

import configparser

# 初始化配置
class Configures(object):

    # 使用单例模式来生成统一的对象
    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, "_inst"):

            # 单例对象
            cls._inst = super(Configures, cls).__new__(cls)

            # 生成两个内部对象
            cls.localConfig = LocalConfig()
            cls.remoteConfig = RemoteConfig()

            # 配置并解析配置文件
            config = configparser.ConfigParser()
            config.read("config.conf")

            # 获取远程网络参数
            remoteTag = "remote"
            cls.remoteConfig.ip = config.get(remoteTag, "IP")
            cls.remoteConfig.port = config.getint(remoteTag, "Port")
            cls.remoteConfig.user = config.get(remoteTag, "User")
            cls.remoteConfig.passwd = config.get(remoteTag, "Passwd")

            # 获取本地配置参数
            localTag = "localhost"
            cls.localConfig.ip = config.get(localTag, "IP")
            cls.localConfig.port = config.getint(localTag, "Port")
            cls.localConfig.debug = config.getboolean(localTag, 'Debug')
            cls.localConfig.user = config.get(localTag, "User")
            cls.localConfig.passwd = config.get(localTag, "Passwd")
            cls.localConfig.temperature = config.get(localTag, "Temperature")
            cls.localConfig.pressure = config.get(localTag, "Pressure")
            cls.localConfig.pm2dot5 = config.get(localTag, "PM2dot5")

            # 获取移除了:号的MAC地址
            cls.macAddr = "00:11:22:33:44:55"# getMac().replace(":", "")

            # 根据是否输出调试信息来决定是否输出配置信息
            if cls.localConfig.debug :

                print("[Debug configure data]:")
                print("\tlocalhost Debug: %s" % cls.localConfig.debug)

                print("[Remote configure data]:")
                print("\tremote IP: %s" % cls.remoteConfig.ip)
                print("\tremote Port: %d" % cls.remoteConfig.port)
                print("\tremote User: %s" % cls.remoteConfig.user)
                print("\tremote Passwd: %s" % cls.remoteConfig.passwd)

                print("[Local configure data]:")
                print("\tlocalhost IP: %s" % cls.localConfig.ip)
                print("\tlocalhost Port: %d" % cls.localConfig.port)
                print("\tlocalhost User: %s" % cls.localConfig.user)
                print("\tlocalhost Passwd: %s" % cls.localConfig.passwd)
                print("\tlocalhost Temperature: %s" % cls.localConfig.temperature)
                print("\tlocalhost Pressure: %s" % cls.localConfig.pressure)
                print("\tlocalhost PM2dot5: %s" % cls.localConfig.pm2dot5)

        return cls._inst

configures = Configures()

if __name__ == '__main__':

    # 输出信息：
    #     < __main__.Configures object at 0x7f7404fb3240 >
    #     < __main__.Configures object at 0x7f7404fb3240 >
    #     < __main__.Configures object at 0x7f7404fb3240 >
    print(Configures())
    print(Configures())
    print(configures)
