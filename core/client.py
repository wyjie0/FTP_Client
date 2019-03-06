#一开启程序并不是就马上连接服务端，而是显示菜单
from core.auth_client import Auth

def main():
    auth_obj = None
    start_l = [('登录','login'),('注册','register'),('退出','exit')]
    for index, item in enumerate(start_l,1):
        print(index, item[0])
    while True:
        try:
            num = int(input('>>>'))
            func_str = start_l[num-1][1]
        except:
            print('您输入的信息有误！')
            #获取到字符串类型的方法名：login,register,quit
        if hasattr(Auth,func_str):#兼顾登录和注册方法
            auth_obj = Auth()
            func = getattr(auth_obj,func_str)
            ret = func()
            if ret: break#如果有返回值，即登录成功
        elif auth_obj:
            auth_obj.socket.sk.close()
            exit()
        else:
            exit()
