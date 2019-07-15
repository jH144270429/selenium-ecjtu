from selenium import webdriver
import time
import tkinter
from tkinter import *


print("欢迎进入selenium模拟登录系统！！！")
window = tkinter.Tk()
lbl1 = tkinter.Label(window,text='用户名：')
lbl1.grid(row=0, column=0, padx=10, sticky=SW)
ent1 = tkinter.Entry(window,width=20)
ent1.grid(row=0, column=1, padx=10, sticky=E)
lbl2 = tkinter.Label(window, text='密码：')
lbl2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
ent2 = tkinter.Entry(window, width=20, show='*')
ent2.grid(row=1, column=1, padx=10, sticky=E)


def login():
    username = ent1.get()#获取登录框里面的内容
    password = ent2.get()#获取密码框里面的内容
    #username = '2017***********'
    #password = '******'
    driver = webdriver.Chrome(executable_path=r'D:\py\chromedriver.exe')  # 使用selenium代理打开页面
    try:
        driver.maximize_window()
        driver.get('http://cas.ecjtu.edu.cn/cas/login?service=http%3A%2F%2Fportal.ecjtu.edu.cn%2Fdcp%2Findex.jsp')
        time.sleep(1)
        # 自动输入用户
        #print('输入用户名....')
        driver.find_element_by_id('username').clear()  # 清除输入框中默认的内容
        driver.find_element_by_id('username').send_keys(username) #将username中账号传过来
        time.sleep(1)
        # 模拟自动输入密码
        #print('输入密码....')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys(password)
        time.sleep(1)
        # 模拟自动点击登陆按钮
        driver.find_element_by_xpath('//*[@id="login_form"]/span/input').click()#查找登录按钮
        time.sleep(1)
        #print(driver.current_url)
       #print(driver.page_source)
        print('登陆成功.')
        #time.sleep(10)
        #driver.close()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="depart"]/span[2]').click()  # 点击
    except Exception as e:
        print('登陆失败'+ e)
        print("请检查是否账号密码输入错误！！！")


def destroy():
        window.destroy()#关闭窗口

def main():
    print("退出系统！！！")

btn1 = tkinter.Button(window, text='登录', command=login)
btn1.grid(row=2, column=0, padx=10, pady=5, sticky=NE)#登录按钮及其参数
btn2 = tkinter.Button(window, text='取消', command=destroy)
btn2.grid(row=2, column=1, padx=10, pady=5, sticky=NW)#取消按钮及其参数
window.mainloop()#窗口显示

if __name__ == '__main__':
    main()
