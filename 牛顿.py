
import math  
import sys  
	  
import numpy as np  
from scipy.misc import derivative  
	  
	  
def f(xe):  
    y = xe - math.tan(xe)  
    #y = xe ** 3 + 4 * xe ** 2 - 10  
    return y  
	  
	  
def df(xe):  
    #dy = (math.e ** xe) + xe * (math.e ** xe)  
    dy = derivative(f, xe, dx = 1e-6)  
    #dy = 1 - (1.0 / math.cos(xe))* (1.0 / math.cos(xe))  
    return dy  
	  
x = 4.6  # x的值在0.5附近  
k = 0    # 迭代次数计数  
e = 1e-6  # 误差要求  
N = 100       # 最大迭代次数  
	  
	#print(df(x))  
	#sys.exit()  
	  
while k < N:  
    if df(x) == 0:  
        print("初始值错误")  
        sys.exit()  
    x1 = x - f(x) / df(x)  
    print(x1)  
    if abs(x1 - x) < e:  
        print("方程的解为:%f" % x1)  
        print('最大迭代次数为:%d' % k)  
        #print(k)  
        sys.exit()  
    else:
        print("my son han er za")
        k = k + 1  
        x = x1  
