#MrG 2018.0630 UMC22 Mass & Density
#1) Find the mass of a triangular lamina with vertices (0,0), (0,3), (2,3) and variable density function rho(x,y)=2*x+y
show("#1) Find the mass of a triangular lamina with vertices (0,0), (0,3), (2,3) and variable density function rho(x,y)=2*x+y")
var('y')
show(integral(integral(2*x+y,x,0,2*y/3),y,0,3))
show("")

#2a) Find the mass of the lamina corresponding to the parabolic region 0<=y<=4-x^2 if rho(x,y)=1
show("#2a) Find the mass of the parabolic region 0<=y<=4-x^2 if rho(x,y)=1")
m=integral(integral(1,y,0,4-x^2),x,-2,2);show("m=",m)
show("")

#2b) Find the center of mass of the lamina corresponding to the parabolic region 0<=y<=4-x^2 if rho(x,y)=1
show("#2b) Find the center of mass of the lamina corresponding to the parabolic region 0<=y<=4-x^2 if rho(x,y)=1")
Mx=integral(integral(y,y,0,4-x^2),x,-2,2);show("Mx=",Mx);show("xbar=",0, " by symmetry");show("ybar=",Mx/m)
show("")

#2c) Confirm xbar=0
show("#2c) Confirm xbar=0")
My=integral(integral(x,y,0,4-x^2),x,-2,2);show("My=",My);show("xbar=",My/m)

