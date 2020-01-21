#MrG 2018.0630 UMC30 Fundamental Theorem of Line Integrals
#IF C is a peicewise smooth curve in an open region R: r(t)=<x(t),y(t)> for a<=t<=b
#And F(x,y)=<M,N> is conservative, M & N are continuous and f is the potential function for F,
#Then the line integral over C of F.dot_product(dr) = line integral over C of (f.gradient()).dot_product(dr) = f(x(b),y(b))-f(x(a),y(a)).
#Corollary: F is conservative = line integral is independent of path = line integral over a closed curve is zero.
#1) Find the work done by the force field F(x,y)=<2*x*y,x^2> on a particle moving from (0,0) to (1,1) along the path y=x
show("#1) Find the work done by the force field F(x,y)=<2*x*y,x^2> on a particle moving from (0,0) to (1,1) along the path y=x")
var('t')
F=vector([2*t^2,t^2]);show("F(t)=",F) #F=<2*x*y,x^2>=<2*x^2,x^2>=<2*t^2,t^2>
r=vector([t,t]);show("r(t)=",r) #r=<x,y>=<x,x>=<t,t>
v=diff(r,t);show("v(t)=",v)
Fdr=F.dot_product(v);show("Fdr=",Fdr)
W=integral(Fdr,t,0,1);show("W=",W)
show("")

#2) Find line integral of Fdr where C is a smooth curve from (-1,4) to (1,2) given F(x,y)=<2*x*y,x^2-y> so f(x,y)=x^2*y-y^2/2
show("#2) Find line integral of Fdr where C is a smooth curve from (-1,4) to (1,2) given F(x,y)=<2*x*y,x^2-y> so f(x,y)=x^2*y-y^2/2")
var('y')
f(x,y)=x^2*y-y^2/2;show("f(x,y)=",f(x,y))
g=f(x,y).gradient();show("grad(x,y)=",g)
show("line integral of Fdr over C: ",f(1,2)-f(-1,4))
show("")

#3) Find line integral of Fdr where C is a smooth curve from (1,1,0) to (0,2,3) given F(x,y,z)=<2*x*y,x^2-z^2,2*y*z> so f(x,y,z)=x^2*y+y*z^2
show("#3) Find line integral of Fdr where C is a smooth curve from (1,1,0) to (0,2,3) given F(x,y,z)=<2*x*y,x^2-z^2,2*y*z> so f(x,y,z)=x^2*y+y*z^2")
f(x,y,z)=x^2*y+y*z^2;show("f(x,y,z)=",f(x,y,z))
show("line integral of Fdr over C: ",f(0,2,3)-f(1,1,)) # curlF=0 so vector field is conservative
show("")

#4a) Find line integral of Fdr where C is a smooth curve from (0,0) to (2,0) over semicircular path centered at (1,0)
#4a) Given F(x,y)=<y^3+1,3*x*y^2+1> is conservative so f(x,y)=x*y^3+x+y
show("#4a) Find line integral of Fdr where C is a smooth curve from (0,0) to (2,0) over semicircular path centered at (1,0)")
f(x,y)=x*y^3+x+y;show("f(x,y)=",f(x,y))
show("line integral of Fdr over C: ",f(2,0)-f(0,0))
show("")

#4b) Find line integral of Fdr where C is a smooth curve from (0,0) to (2,0) over simpler horizontal path
#4b) Given F(x,y)=<y^3+1,3*x*y^2+1> is conservative so f(x,y)=x*y^3+x+y
show("#4b) Find line integral of Fdr where C is a smooth curve from (0,0) to (2,0) over simpler horizontal path")
F=vector([1,1]);show("F(t)=",F) #F=<y^3+1,3*x*y^2+1>=<1,1> since x=t, y=0
r=vector([t,0]);show("r(t)=",r) #r=<x,0>=<t,x>, 0<=t<=2
v=diff(r,t);show("v(t)=",v)
Fdr=F.dot_product(v);show("Fdr=",Fdr)
W=integral(Fdr,t,0,2);show("W=",W)
show("")

#4c) Find line integral of Fdr where C is a smooth curve from (0,0) to (2,0) over semicircular path centered at (1,0)
#4c) Given F(x,y)=<y^3+1,3*x*y^2+1> is conservative so f(x,y)=x*y^3+x+y
show("#4b) Find line integral of Fdr where C is a smooth curve from (0,0) to (2,0) over simpler horizontal path")
F=vector([(sin(t))^3+1,3*(1-cos(t))*(sin(t))^2+1]);show("F(t)=",F) #F=<y^3+1,3*x*y^2+1> since x=1-cos(t), y=sin(t)
r=vector([1-cos(t),sin(t)]);show("r(t)=",r) #0<=t<=pi
v=diff(r,t);show("v(t)=",v)
Fdr=F.dot_product(v);show("Fdr=",Fdr)
W=integral(Fdr,t,0,pi);show("W=",W)
