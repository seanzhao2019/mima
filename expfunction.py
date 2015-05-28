author__ = 'zhao'
from optparse import OptionParser
from scipy.stats import *
import math
import xlsxwriter
import random
import numpy as np
from pylab import *

usage = "usage: %prog [options] arg1 [options] arg2"
parser = OptionParser(usage=usage)
parser.add_option("-r","--rounds",action="store", type="int", dest="rounds",default = None)
parser.add_option("-m","--mean",action="store", type="float", dest="mean",default = None)
parser.add_option("-p","--pro",action="store", type="float", dest="pros",default = None)
(options, args) = parser.parse_args()

if options.rounds is not None:
     rounds=options.rounds
else:
     print "you need input number !"

if options.mean is not None:
    mean =options.mean
else:
    print "you need input number !"

if options.pros is not None:
      pro =options.pros
else:
    print "you need input number !"


def expd(lamda,size):
   return np.random.exponential(lamda,size)    

lamdamean=mean*pro
#print lamdamean
x1_list=list()
x2_list=list()
y1_list=list()
y2_list=list()
x3_list=list()
y3_list=list()

def p():
    return random.random()

def expntl(lamda):
    return -lamda*math.log(p())

def geometric(pro,number):
    return geom.rvs(pro,size=number)

def x1_fun(pro,rounds,lamda):
    num_sum=list()
    num_sum=geometric(pro,rounds)
    print np.mean(num_sum)
    print num_sum
    y_list=list()
    for n in num_sum:
        y=0
        x=list()
        x=expon.rvs(loc=0,scale=1.0/lamda,size=n)
#        print x
        for i in x:
            y+=i
#        print y
        y_list.append(y)
#    print y_list
    return y_list



def x2_fun(pro,rounds,lamda):
    num_sum=list()
    num_sum=geometric(pro,rounds)
    print np.mean(num_sum)
    print num_sum
    y_list=list()
    
    for n in num_sum:
        x=list()
        for i in range(0,n): 
           y=0
           x.append(expntl(1.0/lamda))
#           print x
           for j in x:
                 y+=j
#           print y    
        y_list.append(y)
#    print y_list
    return y_list


def x3_fun(pro,rounds,lamda):
     num_sum=list()
     num_sum=geometric(pro,rounds)
     print np.mean(num_sum)
     print num_sum
     y_list=list()
     for n in num_sum:
        x=list()
        y=0
        x=expd(1.0/lamda,n)
#        print x
        for j in x:
            y+=j
#        print y
        y_list.append(y)
#     print y_list
     return y_list

   
x1_list=x3_fun(pro,options.rounds,mean)
x2_list=sorted(x1_list)
#print x1_list
print "mean:%g" % np.mean(x1_list)

measure1=np.linspace(0,math.ceil(max(x1_list)),128)
        
rate1_list=list()
for i in measure1:
    counts=0
    for j in x2_list:
        
        if j<i: 
            counts+=1
        else:
            counts=counts
#    print counts    
    rate1_list.append((1.0*counts)/options.rounds)

x3_list=expon.rvs(loc=0,scale=1.0/lamdamean,size=options.rounds)
print "mean_x3=%s" % np.mean(x3_list)
rate2_list=list()
measure2=np.linspace(0,math.ceil(max(x3_list)),128)
#print x3_list
for i in measure2:
    counts=0
    for j in x3_list:
        if j<i:
            counts+=1
        else:
            counts=counts

    rate2_list.append((1.0*counts)/options.rounds)

workbook = xlsxwriter.Workbook('expo1.xlsx')
worksheet1=workbook.add_worksheet('sheet1')
heading =['x1','rate','y3']
worksheet1.write_row('A1',heading)
worksheet1.write_column('A2',sorted(x2_list))
worksheet1.write_column('B2',sorted(rate1_list))
worksheet1.write_column('C2',sorted(rate2_list))
worksheet1.write_column('D2',sorted(x3_list))
workbook.close()

A=math.ceil(max(x1_list))
B=math.ceil(max(x3_list))

figure(1,figsize=(10,8),dpi=100)
plt.plot(measure1,rate1_list,color="blue",linewidth=2.5,linestyle="-")
plt.plot(measure2,rate2_list,color="red",linewidth=2.5,linestyle="--")
plt.title("Exponential Distribution of both of them")# give plot a title
plt.xlabel("x axis")# make axis labels
plt.ylabel("y axis")
yticks(np.linspace(0,1,5,endpoint=True))
xticks(np.linspace(0,B,11,endpoint=True))

savefig("exercice_1.png",dpi=72)

ax1=plt.subplot(2,1,1)
ax2=plt.subplot(2,1,2)

plt.sca(ax1)
plt.plot(measure1,rate1_list,color="blue",linewidth=2.5,linestyle="-")
yticks(np.linspace(0,1,5,endpoint=True))
xticks(np.linspace(0,B,11,endpoint=True))
plt.title("Exponential Distribution of simulation")# give plot a title
#plt.xlabel("x axis")#
plt.ylabel("y axis")


plt.sca(ax2)
plt.plot(measure2,rate2_list,color="red",linewidth=2.5,linestyle="--")
yticks(np.linspace(0,1,5,endpoint=True))
xticks(np.linspace(0,B,11,endpoint=True))
plt.title("Exponential Distribution of analysis")# give plot a title
plt.xlabel("x axis")# make axis labels
plt.ylabel("y axis")

savefig("exercice_2.png",dpi=72)
show()

