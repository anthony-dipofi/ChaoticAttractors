import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

def VDP_osc(init_x,init_y,p,speed,steps):
	
	xs = np.zeros((steps))
	ys = np.zeros((steps))
	xs[0] = init_x
	ys[0] = init_y
	
	for i in range(1,steps):
		x = xs[i-1]
		y = ys[i-1]
		dx = y
		dy = p*y*(1-x**2) - x
		xs[i] = x+speed*dx
		ys[i] = y+speed*dy
		
	pl.plot(xs,ys)
	pl.show()	
	
def Westerhoff(init,a,b,c,d,m,F,steps):
	xs = np.arange(steps)
	ss = np.zeros((steps))
	ss[0] = init
	
	for i in range(1,steps):
		s = ss[i-1]
		v = F-s
		DM = m*v
		DB = -b*(v/(1+d*v**2))
		DC = c*((d*v**3)/(1+d*v**2))
		ss[i] = s + a*(DM + DB +DC)
	
	pl.plot(xs,ss)
	pl.show()
	Westerhoff(init,a,b,c,d,m,F,steps)
	
def Logistic_map(init,p,steps):
	xs = np.arange(steps)
	ys = np.zeros((steps))
	ys[0] = init
	
	for i in range(1,steps):
		y = ys[i-1]
		ys[i] = p*y*(1-y)
	
	pl.ylim(0.0,1.0)	
	pl.plot(xs,ys)
	pl.show()
	
def Tent_map(init,p,steps):
	xs = np.arange(steps)
	ys = np.zeros((steps))
	ys[0] = init
	
	for i in range(1,steps):
		y = ys[i-1]
		if (y < 0.5 and y >=0.0):
			ys[i] = p*y
		elif (y < 1.0 and y >=0.5):
			ys[i] = p*(1-y)
	
	pl.ylim(0.0,1.0)	
	pl.plot(xs,ys)
	pl.show()

def Skew_Tent_map(init,b,steps):
	xs = np.arange(steps)
	ys = np.zeros((steps))
	ys[0] = init
	
	for i in range(1,steps):
		y = ys[i-1]
		if (y <= 1.0 and y >= 0.0):
			ys[i] = np.exp(b)*y
		elif (y > 1.0 and y <=(1+np.exp(-0.5*b))):
			ys[i] = -1*np.exp(1.5*b)*y + (np.exp(b) + np.exp(1.5*b))
		elif (y>(1+np.exp(-0.5*b))):
			ys[i] = np.exp(b)*y - (np.exp(0.5*b)+np.exp(b))
		
	pl.plot(xs,ys)
	pl.show()
	
def Skew_Tent_map_reseed(init,b,seed_funct,seed_step,steps):
	xs = np.arange(steps)
	ys = np.zeros((steps))
	ss = np.zeros((steps))
	zs = seed_funct(xs)
	seedxs = []
	seedys = []
	sym = ""
	ys[0] = init
	
	for i in range(1,steps):
		y = ys[i-1]
		if (i % seed_step ==0):
			ys[i] = seed_funct(i)
			seedxs.append([i])
			seedys.append([ys[i]])
		elif (y <= 1.0 and y >= 0.0):
			ys[i] = np.exp(b)*y
			sym += "A"
		elif (y > 1.0 and y <=(1+np.exp(-0.5*b))):
			ys[i] = -1*np.exp(1.5*b)*y + (np.exp(b) + np.exp(1.5*b))
			sym += "B"
		elif (y>(1+np.exp(-0.5*b))):
			ys[i] = np.exp(b)*y - (np.exp(0.5*b)+np.exp(b))
			sym += "C"
		if(ys[i]>=0.5):
			ss[i] = 1.0
	
	print(sym)
	pl.plot(xs,ys)
	#pl.plot(xs,zs)
	pl.plot(xs,ss)
	pl.stem(seedxs,seedys,linefmt='r')
	pl.show()

#Rossler_attractor((0.1,0.1,0.1), 0.35, 0.5, 12, 0.01, 15000)
def Rossler_attractor(init,a,b,c,speed,steps):
	xs = np.zeros((steps))
	ys = np.zeros((steps))
	zs = np.zeros((steps))
	xs[0] = init[0]
	ys[0] = init[1]
	zs[0] = init[2]
	
	for i in range(1,steps):
		x = xs[i-1]
		y = ys[i-1]
		z = zs[i-1]
		dx = -y-z
		dy = x+a*y
		dz = b+z*(x-c)
		xs[i] = x+speed*dx
		ys[i] = y+speed*dy
		zs[i] = z+speed*dz
		
	fig = pl.figure()
	ax = Axes3D(fig)
	ax.plot(xs,ys,zs)
	pl.show()	
	
def Chua_attractor(init,a,b,c,speed,steps):
	xs = np.zeros((steps))
	ys = np.zeros((steps))
	zs = np.zeros((steps))
	xs[0] = init[0]
	ys[0] = init[1]
	zs[0] = init[2]
	
	for i in range(1,steps):
		x = xs[i-1]
		y = ys[i-1]
		z = zs[i-1]
		dx = a*(y-x)
		dy = x*(c-a) - x*z + y*c
		dz = x*y-b*z
		xs[i] = x+speed*dx
		ys[i] = y+speed*dy
		zs[i] = z+speed*dz
		
	fig = pl.figure()
	ax = Axes3D(fig)
	ax.plot(xs,ys,zs)
	pl.show()	

def Chua_circuit_attractor(init, a, b, m, speed, steps):
	xs = np.zeros((steps))
	ys = np.zeros((steps))
	zs = np.zeros((steps))
	xs[0] = init[0]
	ys[0] = init[1]
	zs[0] = init[2]
	def g(x):
		if(x <= -1):
			return m[1]*(x + 1) - m[0]
		elif(x > -1 and x < 1):
			return m[0]*x
		elif(x >= -1):
			return m[1]*(x - 1) + m[0]
	
	for i in range(1,steps):
		x = xs[i-1]
		y = ys[i-1]
		z = zs[i-1]
		dx = a*(y-g(x))
		dy = x - y - z
		dz = -b*y
		xs[i] = x+speed*dx
		ys[i] = y+speed*dy
		zs[i] = z+speed*dz
		
	fig = pl.figure()
	ax = Axes3D(fig)
	ax.plot(xs,ys,zs)
	pl.show()

def Lorenz_attractor(init, sigma, rho, beta, speed, steps):
	o = sigma
	p = rho
	b = beta
	xs = np.zeros((steps))
	ys = np.zeros((steps))
	zs = np.zeros((steps))
	xs[0] = init[0]
	ys[0] = init[1]
	zs[0] = init[2]
	
	for i in range(1,steps):
		x = xs[i-1]
		y = ys[i-1]
		z = zs[i-1]
		dx = o*(y-x)
		dy = x*(p-z)-y
		dz = x*y-b*z
		xs[i] = x+speed*dx
		ys[i] = y+speed*dy
		zs[i] = z+speed*dz
		
	fig = pl.figure()
	ax = Axes3D(fig)
	ax.plot(xs,ys,zs)
	pl.show()	
	

#RabFab_attractor((-1,0,0.5), 1.1, 0.87, 0.001, 150000)
def RabFab_attractor(init,a,g,speed,steps):
	
	xs = np.zeros((steps))
	ys = np.zeros((steps))
	zs = np.zeros((steps))
	xs[0] = init[0]
	ys[0] = init[1]
	zs[0] = init[2]
	
	for i in range(1,steps):
		x = xs[i-1]
		y = ys[i-1]
		z = zs[i-1]
		dx = y*(z - 1 + x*x) + g*x
		dy = x*(3*z + 1 - x*x) + g*y
		dz = -2*z*(a + x*y)
		xs[i] = x+speed*dx
		ys[i] = y+speed*dy
		zs[i] = z+speed*dz
		
	fig = pl.figure()
	ax = Axes3D(fig)
	ax.plot(xs,ys,zs)
	pl.show()	

def GingerBread_map(init,steps):
	
	xs = np.zeros((steps))
	ys = np.zeros((steps))
	xs[0] = init[0]
	ys[0] = init[1]
	
	for i in range(1,steps):
		x = xs[i-1]
		y = ys[i-1]
		xs[i] = 1 - y + np.abs(x)
		ys[i] = x
		
	pl.plot(xs,ys)
	pl.show()

