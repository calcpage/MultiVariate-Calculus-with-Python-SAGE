#MrG 2018.0629 NCC13 LaGrange Multipliers
#1) Find point closest to origin for the curve xy=3
#1) Minimize f(x,y)=sqrt(x^2+y^2) subject to the constraint g(x,y): x*y=3 (when are level curves tangent to each other?)
#1) Minimize f(x,y)=sqrt(x^2+y^2) subject to the constraint g(x,y): x*y=3 (when are gradient vectors to level curves parallel to each other?)
show("#1) Minimize f(x,y)=sqrt(x^2+y^2) subject to the constraint g(x,y): x*y=3")
var('y,l')
f=x^2+y^2;show("f=",f)
fx=diff(f,x);show("fx=",fx)
fy=diff(f,y);show("fy=",fy)
g=x*y-3;show("g=",g)
gx=diff(g,x);show("gx=",gx)
gy=diff(g,y);show("gy=",gy)
show(solve([fx==l*gx,fy==l*gy,g==0],(x,y,l)))
