#MrG 2018.0528 UMC05 Differentiablility and the Chain Rule
#1) Heat Index aka Real Feel aka Apparent Temperature
show("#1) Heat Index aka Real Feel aka Apparent Temperature")
var('t,h')
A(t,h)=0.885*t-22.4*h+1.2*t*h-0.544;show("A(t,h)=",A(t,h));show("A(30,0.8)=",A(30,0.8));show("A(30.5,0.75)=",A(30.5,0.75))
At(h)=diff(A(t,h),t);show("At(h)=",At(h))
Ah(t)=diff(A(t,h),h);show("Ah(t)=",Ah(t))
show("dA=",At(0.8)*0.5+Ah(30)*-0.05)
show("A+dA=",A(30,0.8)+At(0.8)*0.5+Ah(30)*-0.05)
show("")

#2) w(x,y)=x^2*y-y^2, x=sin(t), y=e^t, find dw/dt by Chain Rule
show("#2) w(x,y)=x^2*y-y^2, x=sin(t), y=e^t, find dw/dt by Chain Rule")
var('y')
w(x,y)=x^2*y-y^2;show("w(x,y)=",w(x,y))
wx(x,y)=diff(w(x,y),x);show("wx(x,y)=",wx(x,y))
wy(x,y)=diff(w(x,y),y);show("wy(x,y)=",wy(x,y))
x(t)=sin(t);show("x(t)=",x(t))
xp(t)=diff(x(t),t);show("xp(t)=",xp(t))
y(t)=e^t;show("y(t)=",y(t))
yp(t)=diff(y(t),t);show("yp(t)=",yp(t))
show("dw/dt=",wx(x,y)*xp(t)+wy(x,y)*yp(t))
