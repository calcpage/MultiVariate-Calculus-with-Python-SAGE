#MrG 2018.0630 UMC28 Div & Curl
#1) Calculate the curl: F(x,y,z)=<2*x*y,x^2+z^2,2*y*z>) 
#1) If the curl is 0, then the vector field is conservative!
#1) curlF(x,y,z)=del.cross_product(<M,N,P>)
show("#1) Calculate the curl: F(x,y,z)=<2*x*y,x^2+z^2,2*y*z>) If the curl is 0, then the vector field is conservative!")
var('y,z')
curl=vector([diff(2*y*z,y)-diff(x^2+z^2,z),diff(2*y*z,x)-diff(2*x*y,z),diff(x^2+z^2,x)-diff(2*x*y,y)]);show("curlF(x,y,z)=",curl)
show("")

#2) Calculate the divergence of F(x,y,z)=<x^3*y^2*z,x^2*z,x^2*y>
#2) divF(x,y,z)=del.dot_product(<M,N,P>)
show("#2) Calculate the divergence of F(x,y,z)=<x^3*y^2*z,x^2*z,x^2*y>")
div=vector([diff(x^3*y^2*z,x),diff(x^2*z,y),diff(x^2*y,z)]);show("divF(x,y,z)=",div)
show("")

#3) Evaluate the Line Integral: integrate (x^2-y+3*z)ds along C: line segment along r(t)=<t,2*t,t> for 0<=t<=1
show("#3) Evaluate the Line Integral: integrate (x^2-y+3*z)ds along C: line segment along r(t)=<t,2*t,t> for 0<=t<=1")
var('t')
r=vector([t,2*t,t]);show("r(t)=",r)
v=diff(r,t);show("v(t)=",v)
ds=sqrt((1)^2+(2)^2+(1)^2);show("ds=",ds)
show("line integral of (x^2-y+3*z)ds along C: ",integral((t^2-2*t+3*t)*sqrt(6),t,0,1))
show("")

#4) Find the mass of a spring along the helix r(t)=<cos(t),sin(t),1> for 0<=t<=6*piwith density rho(x,y,z)=1+z
show("#4) Find the mass of a spring along the helix r(t)=<cos(t),sin(t),1> with density rho(x,y,z)=1+z")
r=vector([cos(t),sin(t),1]);show("r(t)=",r)
v=diff(r,t);show("v(t)=",v)
ds=sqrt((-sin(t))^2+(cos(t))^2+(1)^2);show("ds=",ds,"=",sqrt(2))
show("line integral: ",integral((t^2-2*t+3*t)*sqrt(6),t,0,1))
show("line integral of (1+z)ds along C: ",integral((1+t)*sqrt(2),t,0,6*pi))
