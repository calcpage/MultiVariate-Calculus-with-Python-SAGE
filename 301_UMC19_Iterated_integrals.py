#MrG 2018.0628 UMC19 Iterated Integrals
#1) Find the area in the xy-plane bounded by f(x)=sin(x) and g(x)=cos(x) from x=pi/4 to x=5*pi/4
show("#1) Find the area in the xy-plane bounded by f(x)=sin(x) and g(x)=cos(x) from x=pi/4 to x=5*pi/4")
var('y')
show(integral(1,y,cos(x),sin(x)))
show(integral(sin(x)-cos(x),x,pi/4,5*pi/4))
show(integral(integral(1,y,cos(x),sin(x)),x,pi/4,5*pi/4))
show("")

#2) What is the area in the xy-plane: integral(integral(1,x,y^2,4),y,0,2)
show("#2) What is the area in the xy-plane: integral(integral(1,x,y^2,4),y,0,2)")
show(integral(integral(1,x,y^2,4),y,0,2))
show("area bounded by 0<=y<=2 and y^2<=x<=4 ==> x=y^2 or y=sqrt(x)")
show("")

#3a) Evaluate integral(integral(e^(-y^2),y,x,2),x,0,2)
show("#3a) Evaluate integral(integral(e^(-y^2),y,x,2),x,0,2)")
show(integral(integral(e^(-y^2),y,x,2),x,0,2))
show(integral(integral(e^(-y^2),y,x,2),x,0,2).n())
show("")

#3b) Evaluate integral(integral(e^(-y^2),y,x,2),x,0,2)
show("#3b) Evaluate integral(integral(e^(-y^2),y,x,2),x,0,2)")
show(integral(integral(e^(-y^2),x,0,y),y,0,2))
show(integral(integral(e^(-y^2),x,0,y),y,0,2).n())
show("")
