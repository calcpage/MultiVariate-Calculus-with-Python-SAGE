#MrG 2018.0608 NCC09 More Partial Derivatives (for Least Squares see UMC08)
#1) Minimize z=f(x,y)=x^2-2*x*y+3*y^2+2*x-2*y
show("#1) Minimize z=f(x,y)=x^2-2*x*y+3*y^2+2*x-2*y")
f(x,y)=x^2-2*x*y+3*y^2+2*x-2*y;show("f(x,y)=",f(x,y))
fx(x,y)=diff(f(x,y),x);show("fx(x,y)=",fx(x,y))
fy(x,y)=diff(f(x,y),y);show("fy(x,y)=",fy(x,y))
show(solve([diff(f(x,y),x)==0,diff(f(x,y),y)==0],(x,y)))
show("f(-1,0)=",f(-1,0))
p1=point([-1,0,f(-1,0)],color='red')
p2=plot3d(f(x,y),(x,-2,0),(y,-1,1))
show(p1+p2)

