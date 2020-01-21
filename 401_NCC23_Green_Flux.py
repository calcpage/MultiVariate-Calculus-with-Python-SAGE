#MrG 2018.0702 NCC23 Green's Thm for Flux
#1) Work is a line integral over C of the form F.T*ds=F.dr=M*dx+N*dy where F=<M,N>, sums component of F along C
#1) Flux is a line integral over C of the form F.N*ds=-Q*dx+P*dy where F=<P,Q>, sums component of F normal to C
#1) Note: T is tangent unit vector along C, N is normal unit vector along C
#1) Let C = circle of radius a at origin CCW, F=<x,y> such that F is parallel to N so F.N=abs(F)*abs(N)*cos(t)=a*1*cos(0)=a
show("#1) Let C = circle of radius a at origin CCW, F=<x,y> such that F is parallel to N so F.N=abs(F)*abs(N)*cos(t)=a*1*cos(0)=a")
show("#1) ds=differential for arc length of circle=, so Line Integral of FNds=a*ds=2*pi*a^2")
show("")

#2) For Work we evaluate F.T*ds=<M,N>.<dx,dy>=M*dx+N*dy
#2) For Flux we evaluate F.N*ds=<P,Q>.<dy,-dx>=P*dy-Q*dx=-Q*dx+P*dy or
#2) For Flux we evaluate F.N*ds=<M,N>.<dy,-dx>=M*dy-N*dx=-N*dx+M*dy
show("#2) For Work we evaluate F.T*ds=<M,N>.<dx,dy>=M*dx+N*dy")
show("#2) For Flux we evaluate F.N*ds=<P,Q>.<dy,-dx>=P*dy-Q*dx=-Q*dx+P*dy or")
show("#2) For Flux we evaluate F.N*ds=<M,N>.<dy,-dx>=M*dy-N*dx=-N*dx+M*dy")
show("")

#3) If C is a positively oriented closed curve enclosing a region R and the Vector Field F is defined and differentiable in R
#3) Then the Line Integral for Work of F.T*ds = M*dx+N*dy over C = the double integral over R of curl(F)dA = (Nx-My)dA or
#3) Then the Line Integral for Flux of F.N*ds = -Q*dx+P*dy over C = the double integral over R of (Px-(-Qy))dA = div(F)dA
#3a) If F=<x,y>, then div(F)=2 and flux = double inegral over R (circle of radius a at origin CCW) of 2dA=2*pi*a^2
show("#3) If C is a positively oriented closed curve enclosing a region R and the Vector Field F is defined and differentiable in R")
show("#3) Then the Line Integral for Work of F.N*ds = M*dx+N*dy over C = the double integral over R of curl(F)dA = (Nx-My)dA or")
show("#3) Then the Line Integral for Flux of F.N*ds = -Q*dx+P*dy over C = the double integral over R of (Px-(-Qy))dA = div(F)dA")
show("#3a) If F=<x,y>, then div(F)=2 and flux = double inegral over R (circle of radius a at origin CCW) of 2dA=2*pi*a^2")
show("")

#3b) Evaluate Line Integral over R (circle of radius a at origin CCW) of -Q*dx+P*dy=-y*dx+x*dy
show("#3b) Evaluate Line Integral over R (circle of radius a at origin CCW) of -Q*dx+P*dy=-y*dx+x*dy")
var('y,a,t')
F=vector([x,y]);show("F(x,y)=",F)
r=vector([a*cos(t),a*sin(t)]);show("r(t)=",r)
v=diff(r,t);show("v(t)=",v, " this is <dx,dy> we need <dy,-dx>")
FNds=vector([a*cos(t),a*sin(t)]).dot_product(vector([a*cos(t),a*sin(t)]));show("FNds=",FNds)
show(integral(FNds,t,0,2*pi))
