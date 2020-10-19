import sys  
import math  
	  
def f(xe):  
	 #y = xe * xe * xe + 4 * xe * xe - 10  
	 y = xe - math.tan(xe)  
	 return y  
	  
	  
a = 4  
b = 4.6  
e = 1e-6  # 误差要求  
i = 0  # 迭代次数计数  
N = 100 #最多迭代次数  	  

if f(a) * f(b) >= 0:  
	 print("此区间内无根")  
	 sys.exit()  
while i < N:  
    x = (a + b) / 2.0  
	    #num.append(x)  
    print(x)  
    if f(x) == 0:  
        print("方程的解为:%f" % b)  
        sys.exit()  
    elif (f(x) * f(a)) >= 0:  
        a = x  
    elif (f(x) * f(a)) < 0:  
        b = x  
    if abs(b - a) < e:  
        print("方程的解为:%f" % b)  
        print('最多迭代次数为:%d' % i)  
        sys.exit()  
    else:  
        i = i + 1  

