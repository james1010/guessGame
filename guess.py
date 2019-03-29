#!/usr/local/bin/python3
 
import tkinter as tk
import random
import math
from tkinter import messagebox

# 需要猜的目标数字
gameGUESS = 1
guessCount = 0

def guessNum(guessNum):
	'判断输入是否匹配'
	try:
		guess = int(guessNum)
	except ValueError:
		var.set('输入格式错误，请输入纯数字') 
	global guessCount
	guessCount = guessCount + 1
	if guess == gameGUESS:
		result = "您猜了%d次,猜对了~~答案是%d\n"%(guessCount,gameGUESS)
		var.set(result)
		showAgain(result)
	elif guess > gameGUESS :
		print("猜大了")
		var.set('输入：%d 猜大了'%guess) 
		inputfiled.set('')
	else:
		print("猜小了")
		inputfiled.set('')
		var.set('输入：%d 猜小了'%guess)  


def insert_point():
	'捕获输入数字'
	var = e.get()
	print("输入的数字是:%s"%var)
	guessNum(var)

def initGameGUESS():
	'初始化目标数字'
	global gameGUESS
	global guessCount
	guessCount = 0
	gameGUESS = random.randint(1,100)

def showAgain(str):
	g = messagebox.askquestion(title="恭喜您",message=str+"\n继续玩吗?")
	if g == 'yes':
		inputfiled.set('')
		initGameGUESS()
	else:
		window.destroy()

# 主窗口
window = tk.Tk()
window.title('猜数字')
window.geometry('400x600')


#  标题文本
l = tk.Label(window, 
    text='猜大小游戏，数字在1~100之间',    # 标签的文字
    bg='#ff0220',     # 背景颜色
    font=('Arial', 20),     # 字体和字体大小
    width=30, height=4  # 标签长宽
    )
l.pack()    # 固定窗口位置

# 初始化目标数字
initGameGUESS()

# 初始化输入框
inputfiled = tk.StringVar()
e = tk.Entry(window,font=('Arial', 20),cursor='arrow',textvariable=inputfiled)
e.pack()

b1 = tk.Button(window,text="猜一猜",width=40,height=8,activeforeground='green',command=insert_point)
b1.pack()

var = tk.StringVar()    # 这时文字变量储存器
var.set("结果显示：")
result = tk.Label(window, 
    textvariable=var,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='blue',fg="white",font=('Arial', 30), width=100, height=8)
result.pack() 
 
exitButton = tk.Button(window,text="退出",fg='#50f099',width=20, height=10,command=window.destroy)
exitButton.pack()

window.mainloop()