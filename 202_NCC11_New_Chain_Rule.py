#MrG 2018.0629 NCC11 New Chain Rule
#1) Let f=x^2*y+z, df=fx*dx+fy*dy+fz*dz and df/dt given x=t, y=e^t and z=sin(t)
show("#1) Let f=x^2*y+z, df=fx*dx+fy*dy+fz*dz and df/dt given x=t, y=e^t and z=sin(t)")
var('x,y,z,t')
f(x,y,z)=x^2*y+z;show("f(x,y,z)=",f)
fx=diff(f(x,y,z),x);show("fx=",fx)
fy=diff(f(x,y,z),y);show("fy=",fy)
fz=diff(f(x,y,z),z);show("fz=",fz)
x(t)=t;show("x(t)=",x(t))
y(t)=e^t;show("y(t)=",y(t))
z(t)=sin(t);show("z(t)=",z(t))
xp(t)=diff(x,t);show("x'(t)=",xp(t))
yp(t)=diff(y,t);show("y'(t)=",yp(t))
zp(t)=diff(z,t);show("z'(t)=",zp(t))
show("df=fx*dx+fy*dy+fz*dz")
show("df/dt=fx*dx/dt+fy*dy/dt+fz*dz/dt")
show("df/dt=2*t*e^t*1+t^2*e^t+1*cos(t)")
show("")

#2) Prove The Product Rule: (u*v)'=u*v'+v*u'
show("#2) Prove The Product Rule: (u*v)'=u*v'+v*u'")
show("Let u=u(t), v=v(t), f=u*v")
show("df=fu*du+fv*dv")
show("df=v*du+u*dv")
show("df/dt=v*du/dt+u*dv/dt")
show("(u*v)'=v*u'+u*v'")
show("")

#3) Prove The Quotient Rule: (u/v)'=(v*u'-u*v')/v^2
show("#3) Prove The Quotient Rule: (u/v)'=(v*u'-u*v')/v^2")
show("Let u=u(t), v=v(t), f=u/v")
show("df=fu*du+fv*dv")
show("df=(1/v)*du+(-u/v^2)*dv")
show("df=(v/v^2)*du-(u/v^2)*dv")
show("df=(v*du-u*dv)/v^2")
show("df/dt=(v*du/dt-u*dv/dt)/v^2")
show("(u/v)'=(v*u'-u*v')/v^2")



