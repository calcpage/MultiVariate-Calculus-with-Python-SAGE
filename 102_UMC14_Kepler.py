#MrG 2018.0614 UMC14 Kepler's Laws
#1) Planets move in a plane
#1a) Show that the cross product of a vector with itself is zero
show("#1a) Show that the cross product of a vector with itself is zero")
var('t')
u=vector([cos(t), sin(t), 2*t]);show("u x u=",u.cross_product(u))
show("")

#1b) Show that parallel vectors also have a zero cross product
#1b) namely F=ma=(-GMm/r^2)r so the vectors a and r are parallel: r x r" = r x a = 0
#1b) therefore [rxr']'=r'xr'+rxr"=0 so rxr'=constant, say vector L orthogonal to the plane of the orbit
show("#1b) Show that parallel vectors also have a zero cross product")
v=2*u;show("2*u=",v)
show("u x v=",u.cross_product(v))
show("")

#2) The vector r from the sun to the planet sweeps out equal areas in equal times
show("#2) The vector r from the sun to the planet sweeps out equal areas in equal times")
r=vector([3*cos(t), 3*sin(t),0]);show("r=",r)
v=diff(r,t);show("v=r'=",v)
c=r.cross_product(v);show("rxr'=",c)
#2a) rxr'=r^2 dtheta/dt k= L a constant vector, then abs(rxr')=abs(L)=r^2 dtheta/dt
#2a) Area=0.5integral(r^2,theta,alpha,beta)=0.5integral(r^2 dtheta/dt,t,t1,t2)=0.5abs(L)(t1-t0)
#2a) Therefore, for the time interval [t0,t1], the area swept out is a constant based on abs(L).
show("")

#3) Show, empirically, that a^3=p^2 for Mercury (a=mean distance to the sun, p=period of orbit)
show("#3) Show, empirically, that a^3=p^2 for Mercury (a=mean distance to the sun, p=period of orbit)")
a=0.3871 #au
p=0.2408 #years
show("a=",a);show("a^3=",a^3)
show("p=",p);show("p^2=",p^2)
