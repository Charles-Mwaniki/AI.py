import matplotlib.pyplot as plt

def myplot(min,max,step,fun1,fun2):
	plt.ion() # make it interactive
	plt.xlabel("The x axis")
	plt.ylabel("The y axis")
	plt.xscale('linear') # Makes a 'log' or 'linear' scale
	xvalues = range(min,max,step)
	plt.plot(xvalues,[fun1(x) for x in xvalues],
	label="The first fun")
	plt.plot(xvalues,[fun2(x) for x in xvalues], linestyle='--',color='k',
	label=fun2.__doc__) # use the doc string of the function
	plt.legend(loc="upper right") # display the legend

def slin(x):
	"""y=2x+7"""
	return 2*x+7
def sqfun(x):
	"""y=(x-40)ˆ2/10-20"""
	return (x-40)**2/10-20

#
#
#
#
#
#
#
#
#
#
Try the following:
from pythonDemo import myplot, slin, sqfun
import matplotlib.pyplot as plt
myplot(0,100,1,slin,sqfun)
plt.legend(loc="best")
import math
plt.plot([41+40*math.cos(th/10) for th in range(50)],
[100+100*math.sin(th/10) for th in range(50)])
plt.text(40,100,"ellipse?")
plt.xscale('log')
