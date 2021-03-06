#MrG 2018.0614 UMC15 Gradients
#1) Given the unit vector u=<cos(pi/3),sin(pi/3)> find the directionl derivative of f(x,y)=4-x^2-y^2/4 at (1,2)
show("#1) Given the unit vector u=<cos(pi/3),sin(pi/3)> find the directionl derivative of f(x,y)=4-x^2-y^2/4 at (1,2)")
var('y')
f=4-x^2-y^2/4;show("f(x,y)=",f)
fx(x,y)=diff(f,x);show("fx(x,y)=",fx(x,y));show("fx(1,2)=",fx(1,2))
fy(x,y)=diff(f,y);show("fy(x,y)=",fy(x,y));show("fy(1,2)=",fy(1,2))
u=vector([cos(pi/3),sin(pi/3)]);show("u=",u)
v=vector([fx(1,2),fy(1,2)]);show("v=",v)
show("directional derivative=",u.dot_product(v))
show("")

#2) Find the gradient of f(x,y)=y*log(x)+x*y^2 at (1,2) normal to level curve of f
show("#2) Find the gradient of f(x,y)=y*log(x)+x*y^2 at (1,2) normal to level curve of f")
f(x,y)=y*log(x)+x*y^2;show("f(x,y)=",f(x,y));show("f(1,2)=",f(1,2)) 
show("level curve y=",solve(f(x,y)==4,y))
fx(x,y)=diff(f(x,y),x);show("fx(x,y)=",fx(x,y))
fy(x,y)=diff(f(x,y),y);show("fy(x,y)=",fy(x,y))
show("grad(x,y)=",vector([fx(x,y),fy(x,y)]))
show("grad(1,2)=",vector([fx(1,2),fy(1,2)])) 
show("")

#3) Find the gradient of f(x,y,z)=x^2+y^2-4*z at (2,-1,1) orthogonal to level surface of f
show("#3) Find the gradient of f(x,y,z)=x^2+y^2-4*z at (2,-1,1) orthogonal to level surface of f")
f(x,y,z)=x^2+y^2-4*z;show("f(x,y,z)=",f(x,y,z));show("f(2,-1,1)=",f(2,-1,1)) 
show("level surface z=",solve(f(x,y,z)==1,z))
fx(x,y,z)=diff(f(x,y,z),x);show("fx(x,y,z)=",fx(x,y,z))
fy(x,y,z)=diff(f(x,y,z),y);show("fy(x,y,z)=",fy(x,y,z))
fz(x,y,z)=diff(f(x,y,z),z);show("fz(x,y,z)=",fz(x,y,z))
show("grad(x,y,z)=",vector([fx(x,y,z),fy(x,y,z),fz(x,y,z)]))
show("grad(2,-1,1)=",vector([fx(2,-1,1),fy(2,-1,1),fz(2,-1,1)]))
