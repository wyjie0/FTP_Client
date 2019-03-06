from core.socket_client import MySocketClient
import struct
import json

class Auth:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            obj = object.__new__(cls)
            cls.__instance = obj
        return cls.__instance

    def __init__(self):
        self.socket = MySocketClient()
        self.username = None

    def login(self):
        username = input('username: ')
        password = input('password: ')
        #确保发送的东西都不为空
        if username.strip() and password.strip():
            self.socket.mysend({'username':username,'password':password,
                            'operation':'login'})
        ret = self.socket.sk.recv(1024)#登录成功的结果
        return ret

    def register(self):
        username = input('username: ')
        password1 = input('password: ')
        password2 = input('password: ')
        if username.strip() and password1.strip() and password1==password2:
            self.socket.mysend({'username': username, 'password': password1,
                            'operation':'register'})
        ret = self.socket.sk.recv(1024)#注册成功的结果
        return ret