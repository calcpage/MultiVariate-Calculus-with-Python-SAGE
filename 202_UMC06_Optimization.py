#MrG 2018.0606 UMC06 Optimization
#1) Optimize f(x,y)=2*x+4*y-x^2-y^2
show("Optimize f(x,y)=2*x+4*y-x^2-y^2")
f(x,y)=2*x+4*y-x^2-y^2;show("f(x,y)=",f(x,y))
fx(x,y)=diff(f(x,y),x);show("fx(x,y)=",fx(x,y))
fy(x,y)=diff(f(x,y),y);show("fy(x,y)=",fy(x,y))
show("fx(x,y)==0",solve(fx(x,y)==0,x))
show("fy(x,y)==0",solve(fy(x,y)==0,y))
p1=plot3d(f(x,y),(x,0,4),(y,0,4))
p2=point([1,2,5],color='red')
#show(p1+p2)
show("")

#2) Apply 2nd Partials Test to question #1: d>0, fxx<0 ==> max! 
show("#2) Apply 2nd Partials Test to question #1: d>0, fxx<0 ==> max!")
fxx(x,y)=diff(fx(x,y),x);show("fxx(x,y)=",fxx(x,y))
fyy(x,y)=diff(fy(x,y),y);show("fyy(x,y)=",fyy(x,y))
fxy(x,y)=diff(fx(x,y),y);show("fxy(x,y)=",fxy(x,y))
fyx(x,y)=diff(fy(x,y),x);show("fyx(x,y)=",fyx(x,y))
d=fxx(x,y)*fyy(x,y)-fxy(x,y)*fyx(x,y);show("d=",d)
show("")

#3) Maximize volume of open aquarium where base costs $3/ft^2 and the sides cost $2/ft^2. You only have $1296 to build it!
show("Maximize volume of open aquarium where base costs $3/ft^2 and the sides cost $2/ft^2. You only have $1296 to build it!")
var('z')
c=3*x*y+4*y*z+4*x*z;show("c=",c)
show(solve(1296==3*x*y+4*y*z+4*x*z,z)[0].rhs())
v=x*y*solve(1296==3*x*y+4*y*z+4*x*z,z)[0].rhs();show("v=",v)
vx=diff(v,x);show("vx=",vx.simplify_rational())
vy=diff(v,y);show("vy=",vy.simplify_rational())
#print(vx.simplify_rational())
#print(vy.simplify_rational())
show(solve([-3/4*(2*x*y^3 + (x^2 - 432)*y^2)==0,-3/4*(2*x^3*y + x^2*y^2 - 432*x^2)==0],(x,y)))
show(solve(1296==3*12*12+4*12*z+4*12*z,z))
