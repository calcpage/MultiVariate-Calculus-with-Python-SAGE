#MrG 2018.0523 NCC06 More Parametrics!
#1) What's A Position Vector?
show("#1) What's A Position Vector?")
var('t')
x(t)=t-sin(t);show("x(t)=",x(t))
y(t)=1-cos(t);show("y(t)=",y(t))
s=vector([x(t),y(t)]);show("s=",s)
show("")

#2) What's A Velocity Vector?
show("#2) What's A Velocity Vector?")
xp(t)=diff(x(t),t);show("xp(t)=",xp(t))
yp(t)=diff(y(t),t);show("yp(t)=",yp(t))
v=vector([xp(t),yp(t)]);show("v=",v)
show("")

#3) What's An Acceleration Vector?
show("#3) What's An Acceleration Vector?")
xpp(t)=diff(xp(t),t);show("xpp(t)=",xpp(t))
ypp(t)=diff(yp(t),t);show("ypp(t)=",ypp(t))
a=vector([xpp(t),ypp(t)]);show("a=",a)
