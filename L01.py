import numpy as np

# 缺失值


def chazhi1(x,y,test_x):
    array_x=np.array(x)#向量化
    array_y=np.array(y)
    #矩阵分向量
    n=len(x)
    X=[]
    for ii in range(n):
        l=array_x**(ii)
        X.append(l)
    #完整矩阵
    X=np.array(X).T
    #求待定系数
    A=np.dot(np.linalg.inv(X),array_y)

    # test_x=1.5 #缺失值
    xx=[]
    for jj in range(n):
        k=test_x**jj
        xx.append(k)
    xx=np.array(xx)
    return np.dot(xx,A)#结果


def larg(x, y, test_x):
    n = len(x)
    L = 0
    for i in range(n):
        li = 1
        for j in range(n):
            if i != j:
                li *= (test_x - x[j]) / (x[i] - x[j])
        L += li * y[i]
    return L



x=[1.0,2,3,4]
y=[1,2,3,4]
test_x=1.5 #缺失值
# res=chazhi1(x,y,test_x)
res=larg(x,y,test_x)
# print(res)


#数值积分 梯形公式
n=len(x)
I=0
for ii in range(n-1):
    I+=(y[ii]+y[ii+1])*(x[ii+1]-x[ii])/2

# print(I)


#时长计算 相似三角形
T=0
for kk in range(n-1):
    if max(y[kk],y[kk+1]) < test_x:
        t=0
    elif min(y[kk],y[kk+1]) > test_x:
        t=x[kk+1]-x[kk]
    else:
        t=(max(y[kk],y[kk+1])-test_x)/abs(y[kk]-y[kk+1])*abs(x[kk+1]-x[kk])

    T += t
print(T)