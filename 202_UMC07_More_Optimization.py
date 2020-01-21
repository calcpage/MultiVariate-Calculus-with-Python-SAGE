#MrG 2018.0607 UMC07 Optimization
#1) Maximize Volume of USPS Package: girth=z+2*x+2*y=108, v=x*y*z=x*y*(108-2*x-2*y)
show("Maximize Volume of USPS Package: girth=z+2*x+2*y=108, v=x*y*z=x*y*(108-2*x-2*y)")
var("y")
v=x*y*(108-2*x-2*y);show("v=",v)
vx=diff(v,x);show("vx=",vx)
vy=diff(v,y);show("vy=",vy)
show(solve([diff(v,x)==0,diff(v,y)==0],(x,y)))
show(18*18*36)
show("")

#2) Minimize Cost of Pipe Line: c(x,y)=3*sqrt(x^2+4)+2*sqrt((y-x)^2+1+1*(10-y)
show("Minimize Cost of Pipe Line: c(x,y)=3*sqrt(x^2+4)+2*sqrt((y-x)^2+1+1*(10-y)")
c(x,y)=3*sqrt(x^2+4)+2*sqrt((y-x)^2+1)+1*(10-y);show("c(x,y)=",c(x,y))
cx(x,y)=diff(c(x,y),x);show("cx(x,y)=",cx(x,y))
cy(x,y)=diff(c(x,y),y);show("cy(x,y)=",cy(x,y))
show(solve([cx(x,y)==0,cy(x,y)==0],(x,y)))
show(c(sqrt(2)/2,sqrt(2)*(sqrt(6)+3)/6).n())
