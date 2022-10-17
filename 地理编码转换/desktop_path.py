# -*- coding: utf-8 -*-
'''
获取当前电脑的桌面路径
'''

import winreg

def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')#利用系统的链表
    return winreg.QueryValueEx(key, "Desktop")[0]  # 返回的是Unicode类型数据

Desktop_path = str(get_desktop())  # Unicode转化为str
print(Desktop_path)

# if __name__=='__main__':
#     Desktop_path = str(get_desktop())#Unicode转化为str
#     print(Desktop_path)


