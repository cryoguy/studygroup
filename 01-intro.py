#!/usr/bin/env python
# coding: utf-8

# Python 入门基础
# ================
# 
# # Backgrounnd (背景)
# ## Factoids
# 1. NOT 蟒蛇
# 
# <img src="images/python_logo.jpg" width="60px" />
# 
# 
#    **Not Python (蟒蛇)**，而是英国喜剧片的名字　- Monty Python’s Flying Circus。
# 1. Interpreted Language (REPL)
# 
#     解释型语言（Interpreted language）vs 編譯語言（Compiled language）
#     
# 1. Python 3 is not back compatible with Python 2. **Use Python 3**
# 1. Object-Oriented
# 1. the ZEN of python
# 
# ## Python之禅 by Tim Peters
# 
#     Perl之禅: 不止一种方法去做一件事（There's more than one way to do it，TMTOWTDI或TIMTOWTDI，发音为“Tim Toady”).

# In[1]:


import this


# Python之禅 by Tim Peters
#  
# 优美胜于丑陋（Python 以编写优美的代码为目标）
# 明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
# 简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
# 复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
# 扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
# 间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
# 可读性很重要（优美的代码是可读的）
# 即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
#  
# 不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
#  
# 当存在多种可能，不要尝试去猜测
# 而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
# 虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）
#  
# 做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
#  
# 如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
#  
# 命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
# 

# # My way of learning computing
# 
# 1. Big picture first
# 2. Project oriented - research and learn as needed.
# 3. Kids Mindset
#     - curiosity driven
#     - never afraid of mistakes 
#     - no need to fully understand everything at once
# 4. Practice makes perfect - just like any language
#     read or write some code everyday!
# 5. Stand on the shoulder of the giants
# 6. No need to reinvent the wheels

# # Python 安装及相关知识

# # 安装
# 
# ## 部件 (Components)
# 1. Python (语言环境）
# 2. IDE - Many Options　（编码器）
#     Spyder, PyCharm, VS Code, IntelliJ IDEA etc.
# 3. Package management system (软件包管理器)
#     Python自带 (builtin): pip
#     Third-Party:  conda,  Anaconda
# 4. Packages (软件包)
#     Almost anything needed!
# 5. Jupyter lab or Notebook （笔记本） 
# 
# ## 最佳（简）方法：
# [anaconda](https://www.anaconda.com/)
# 
# Anaconda安装以上5项 (第3项：Spyder; 第4项常见软件包)！

# # Other Related Knowledge　（其他相关知识）
# ## Tools
# ### Spyder
#     IDE (Intergrated Development Environment)
# ### Jupyter
#     cheatsheet
# #### Shortcut Key (快捷键)
#     a 在现在的单元后加单元(cell)  -after
#     b 在现在的单元前加单元(cell)  -before
#     d d 去除当前单元
#     Ctrl-Shift-- 从当前分为新的单元
#     shift-Enter  运行当前单元代码
#     Shift-M : 合并下一单元
#     y : to code
#     m : to markdown
#     r : to raw
#     
# ## HTML and Markdown
# 
# **Markup vs Markdown**
# 
# cheat sheet
# 

# ## General Computer Language Basics
#    
# ###  Difference between bit and byte:
# 
#     bit = Binary Digit
# 
# <div>
# <img src="images/bytes.png" width="500px"/>
# </div>
# 
# ------------------------------
# |Bit 	|      Byte          |
# |-------|--------------------|
# |Bit is single binary value either 0 or 1.    |  A byte is eight bits. |
# | Example: 0 or 1	            |     Example: 01011010 |
# |It is denoted by b	|   It is denoted by B.  |
# |It has only two possible values either 0 or 1.	|      It has 2^8 (256) possible values ranging from 00000000 (0) to 11111111 (255). |
# |Network engineers describe network speeds in bits per second abbreviated as bps.  Example: 256 Kbps, 20 Mbps, 100 Mbps etc...       |	Used to measure data storage in Bytes and transmission in Bytes per second abbreviated as Bps
# Example: CD holds 700 MB, hard drive holds 500 GB etc.. |
# |1024 bits = 1 Kilo bits (Kb)  | 1 Byte = 8 bits |
# |1024 Kb = 1 Mega bits (Mb)    | 1024 Bytes = 1 Kilo Bytes (KB)  |
# |1024 Mb = 1 Giga bits (Gb)    | 1024 KB = 1 Mega Bytes (MB)    | 
# |1024 Gb = 1 Terra bits (Tb)   | 1024 MB = 1 Giga Bytes (GB)  |
# |                              | 1024 GB = 1 Terra Bytes (TB)     |

# ### 二进制和十进制的转换

# In[17]:


# 256
2*(10**2)+5*(10**1)+6*(10**0)
# 256.1
# 2*(10**2)+5*(10**1)+6*(10**0)+1*(10**(-1))


# <div>
# <img src="images/python-math-image-exercise-31.svg" width="600px"/>
# </div>

# In[7]:


# convert decimal to binary
bin(10)


# In[18]:


# convert binary to decimal  1111111
b_num = list(input("Input a binary number: "))
value = 0

for i in range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)


# ### ASCII (American Standard Code for Information Interchange)
# 
# <div>
# <img src="images/asciifull.jpg" width="800px" />
# </div>

# ### 阴阳八卦　－　题外话
# 
# <div>
# <img src="images/14924796533086_2019-01-17_17-19-48.jpg" width="600px" />
# </div>

# # 计算机语言的组成部件
# 1. Comment （备注语句）
# 
#     """
#     anything inside is comments
#     """
#     
#     \# or anything after #
# 1. Variable types (变量类型）
# 1. Data array　（数据组）
# 1. Expression and operators　（语法，表达等）
# 1. Function　（功能函数）
# 1. Loop and Flow (if, for, while)　（循环路线）
# 1. Class and Object with dot (.)　　（类，物体（目标））
# 
#     attribute and method()  
#   

# # Namespaces (命名空间)

# In[3]:


## Namespace
# dir('name')
import math
print(math.pi)
math.sqrt(5)


# ## Numpy

# In[19]:


import numpy as np
np.sqrt(2)
# sqrt(2) # error
arr1d = np.array([1,2,3])
print("1D array ", arr1d.shape, "array: \n", arr1d)
# 2D array
arr2d1 = np.array([[1,2,5], [2,4,6]])
print("2D array: ", arr2d1)
# 3D array
arr2d2 = np.array([[1,2,5], [2,4,6],[10,20,40]])
print("3D array ", arr2d1.shape, "array: \n", arr2d1)
# 3D array
arr3d = np.zeros((2, 4, 3))
print("3D array Dimension ", arr3d.shape, "array: \n", arr3d)
# nD array
arrnd = np.empty((2, 4, 3, 5))
print("nD array Dimension ", arrnd.shape, "array: \n", arrnd)


# ## Image array
# <img src="images/image2array.jpg" width="600px" />

# In[2]:


import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

np.random.seed(1)
n = 20
l = 256
im = np.zeros((l, l))
points = l*np.random.random((2, n**2))
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
im = ndimage.gaussian_filter(im, sigma=l/(4.*n))

mask = (im > im.mean()).astype(np.float)


img = mask + 0.3*np.random.randn(*mask.shape)

binary_img = img > 0.5

# Remove small white regions
open_img = ndimage.binary_opening(binary_img)
# Remove small black hole
close_img = ndimage.binary_closing(open_img)

plt.figure(figsize=(12, 3))

l = 128

plt.subplot(141)
plt.imshow(binary_img[:l, :l], cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(142)
plt.imshow(open_img[:l, :l], cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(143)
plt.imshow(close_img[:l, :l], cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(144)
plt.imshow(mask[:l, :l], cmap=plt.cm.gray)
plt.contour(close_img[:l, :l], [0.5], linewidths=2, colors='r')
plt.axis('off')

plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0, right=1)

plt.show()


# ## Pandas
# 

# ## OpenCV

# In[1]:


import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():and
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()


# In[ ]:




