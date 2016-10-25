#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2016 - zengjf <zengjf42@163.com>

# 保存对本地设置的一些配置参数
class LocalConfig(object):

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, ip):
        self._ip = ip

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, debug):
        self._debug = debug

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def passwd(self):
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        self._passwd = passwd

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        self._pressure = pressure

    @property
    def pm2dot5(self):
        return self._pm2dot5

    @pm2dot5.setter
    def pm2dot5(self, pm2dot5):
        self._pm2dot5 = pm2dot5
