#MrG 2018.0721 NCC30 Line Integrals in Space
#1) Let F=<y*z,x*z,x*y>, C: x=t^3, y=t^2, z=t, 0<=t<=1
show("#1) Let F=<y*z,x*z,x*y>, C: x=t^3, y=t^2, z=t, 0<=t<=1")
var('y,z,t')
F=vector([y*z,x*z,x*y]);show("F(x,y,z)=",F)
r=vector([t^3,t^2,t]);show("r(t)=",r)
v=diff(r,t);show("v(t)=",v)
Fdr=F.dot_product(v);show("Fdr=",Fdr)
Fdr=3*t^2*t^2*t+2*t*t^3*t+t^3*t^2;show("Fdr=",Fdr)
show(integral(3*t^2*t^2*t+2*t*t^3*t+t^3*t^2,t,0,1))
show("")

#2) If F=<a*x*y, x^2+z^3, b*y*z^2-4*z^3> is a conservative field, find a and b.
show("#2) If F=<a*x*y, x^2+z^3, b*y*z^2-4*z^3> is a conservative field, find a and b.")
var('a,b,y,z')
Ry=diff(b*y*z^2-4*z^3,y);show("Ry=",Ry)
Qz=diff(x^2+z^3,z);show("Qz=",Qz)
Rx=diff(b*y*z^2-4*z^3,x);show("Rx=",Rx)
Pz=diff(a*x*y,z);show("Pz=",Pz)
Qx=diff(x^2+z^3,x);show("Qx=",Qx)
Py=diff(a*x*y,y);show("Py=",Py)
show("")

#3) If F=<2*x*y, x^2+z^3, 3*y*z^2-4*z^3> is a conservative field, 
#3) Find f the potential function such that F=def(f) and CurlF=<Ry-Qz,Rx-Pz,Qx-Py>=0
show("#3) If F=<2*x*y, x^2+z^3, 3*y*z^2-4*z^3> is a conservative field,")
show("#3) Find f the potential function such that F=def(f) and CurlF=<Ry-Qz,Rx-Pz,Qx-Py>=0")
fx=2*x*y;show("fx=",fx)
f=integral(fx,x);show("f=",f,"+g(y,z)")
fy=diff(x^2*y,y);show("fy=",fy,"+gy")
g=integral(z^3,y);show("g(y,z)=",g,"+h(z)")
fz=diff(x^2*y+y*z^3,z);show("fz=",fz,"+h'(z)")
h=integral(-4*z^3,z);show("h=",h,"+C")
f=x^2*y+y*z^3-z^4;show("f=",f,"+C")
