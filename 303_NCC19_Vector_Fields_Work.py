#MrG 2018.0702 NCC19 Vector Fields and Work
#1) Visualize Vector Fields
show("#1) Visualize Vector Fields")
var('y')
plot_vector_field((2,1), (x,-3,3), (y,-3,3))
plot_vector_field((x,0), (x,-3,3), (y,-3,3))
plot_vector_field((x,y), (x,-3,3), (y,-3,3))
plot_vector_field((-y,x), (x,-3,3), (y,-3,3))
show("")

#2) Calculate Work: F(x,y)=<-y,x> along path x=t, y=t^2 for 0<=t<=1
show("#2) Calculate Work: F(x,y)=<-y,x> along path x=t, y=t^2 for 0<=t<=1")
var('t')
F=vector([-y,x]);show("F(x,y)=",F)
r=vector([t,t^2]);show("r(t)=",r)
v=diff(r,t);show("v(t)=",v)
Fdr=vector([-t^2,t]).dot_product(v);show("Fdr=",Fdr)
W=integral(Fdr,t,0,1);show("W=",W)
show("")

#3) Calculate Work: F(x,y)=<M,N>=<-y,x> along path x=t, y=t^2 for 0<=t<=1
#3) line integral of Mdx+Ndy=-ydx+xdy=-t^2dt+t(2t)dt from t=0 to t=1
show("#3) line integral of Mdx+Ndy=-ydx+xdy=-t^2dt+t(2t)dt from t=0 to t=1")
x=t;show("x(t)=",x)
y=t^2;show("y(t)=",y)
M=-y;show("M(x,y)=",M)
N=x;show("N(x,y)=",N)
xp=diff(x,t);show("x'(t)=",xp)
yp=diff(y,t);show("y'(t)=",yp)
show("integral(Mdx+Ndy)=",integral(-t^2*1+t*2*t,t,0,1))

