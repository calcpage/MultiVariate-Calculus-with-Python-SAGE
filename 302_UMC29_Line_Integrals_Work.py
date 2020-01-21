#MrG 2018.0630 UMC29 Line Integrals & Work
#1) Integrate F.dot_product(dr) along C. C is r(t)=<cos(t),sin(t)> for 0<=t<=pi/2 and F(x,y)=<3*x,4*y>.
show("#1) Integrate F.dot_product(dr) along C. C is r(t)=<cos(t),sin(t)> for 0<=t<=pi/2 and F(x,y)=<3*x,4*y>.")
var('y,t')
F=vector([3*x,4*y]);show("F(x,y)=",F)
r=vector([cos(t),sin(t)]);show("r(t)=",r)
v=diff(r,t);show("v(t)=",v)
Fdr=vector([3*cos(t),4*sin(t)]).dot_product(v);show("Fdr=",Fdr)
W=integral(Fdr,t,0,pi/2);show("W=",W)
show("")

#2) Find work done by force field F(x,y,z)=<-0.5*x,-0.5*y,0.25> on a particle moving along helix r(t)=<cos(t),sin(t),t> from (1,0,0) to (-1,0,3*pi)
show("#2) Find work done by force field F(x,y,z)=<-0.5,-0.5,0.25> on a particle moving along helix r(t)=<cos(t),sin(t),t> from (1,0,0) to (-1,0,3*pi)")
F=vector([-0.5*x,-0.5*y,0.25]);show("F(x,y)=",F)
r=vector([cos(t),sin(t),t]);show("r(t)=",r)
v=diff(r,t);show("v(t)=",v)
Fdr=vector([-0.5*cos(t),-0.5*sin(t),0.25]).dot_product(v);show("Fdr=",Fdr)
W=integral(Fdr,t,0,3*pi);show("W=",W)
show("")

#3) Evaluate the line integral of M*dx+N*dy = y*dx+x^2*y along C: y=4x-x^2 from (4,0) to (1,3)
show("#3) Evaluate the line integral of y*dx+x^2*y along C: y=4x-x^2 from (4,0) to (1,3)")
show("line integral of M*dx+N*dy = y*dx+x^2*y along C: ",integral(4*x-x^2+(4-2*x)*x^2,x,4,1))
