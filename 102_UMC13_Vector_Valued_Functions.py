#MrG 2018.0614 UMC13 Vector Valued Functions
#1) Find 1st & 2nd derivatives of a helical path: r(t)=<cos(t), sin(t), 2*t>
show("#1) Find 1st & 2nd derivatives of a helical path: r(t)=<cos(t), sin(t), 2*t>")
var('t')
r=vector([cos(t), sin(t), 2*t]);show("r(t)=",r)
v=diff(r,t);show("v(t)=",v)
a=diff(v,t);show("a(t)=",a)
show("")

#2a) Let u(t)=<1/t, -1, ln(t)>, v(t)=<t^2, -2*t, 1>. Find derivative of the dot product directly
show("#2a) Let u(t)=<1/t, -1, ln(t)>, v(t)=<t^2, -2*t, 1>. Find derivative of the dot product directly")
u=vector([1/t, -1, ln(t)]);show("u(t)=",u)
v=vector([t^2, -2*t, 1]);show("v(t)=",v)
w=u.dot_product(v);show("u(t)v(t)=",w)
show("[u(t)v(t)]'=", diff(w,t))
show("")

#2b) Find derivative of the dot product by product rule: [uv]'=uv'+vu'
show("#2b) Find derivative of the dot product by product rule: [uv]'=uv'+vu'")
a=u.dot_product(diff(v,t));show("a=",a)
b=v.dot_product(diff(u,t));show("b=",b)
show("[u(t)v(t)]'=", a+b)
show("")

#3) Find the arc length of one turn of a helical path: r(t)=<4*cos(t), 4*sin(t), 3*t>
show("#3) Find the arc length of one turn of a helical path: r(t)=<4*cos(t), 4*sin(t), 3*t>")
var('t')
r=vector([4*cos(t), 4*sin(t), 3*t]);show("r(t)=",r)
v=diff(r,t);show("v(t)=",v)
show("speed =", abs(v))
show("arc length = ", integral(abs(v),t,0,2*pi))
show("")
