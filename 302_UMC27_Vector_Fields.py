#MrG 2018.0630 UMC27 Vector Fields
#1) Sketch the Vector Field F(x,y)=<-y,x>
show("#1) Sketch the Vector Field F(x,y)=<-y,x>")
var('y')
plot_vector_field((-y,x), (x,-3,3), (y,-3,3))
show("")

#2) Sketch the Vector Field F(x,y)=<x,y>
show("#2) Sketch the Vector Field F(x,y)=<x,y>")
var('y')
plot_vector_field((x,y), (x,-3,3), (y,-3,3))
show("")

#3) The gradient of f(x,y)=x^2*y-y^2/2 is a Vector Field
show("#3) The gradient of f(x,y)=x^2*y-y^2/2 is a Vector Field")
f=x^2*y-y^2/2;show("f(x,y)=",f)
g=f.gradient();show("grad(x,y)=",g)
plot_vector_field(g, (x,-3,3), (y,-3,3))
show("")

#4) Show that F(x,y)=<10*x+3*y,3*x+2*y> is  conservative with potential function f(x,y)=5*x^2+3*x*y+y^2
show("#4) Show that F(x,y)=<x^2*y,x*y> is conservative with potential function f(x,y)=5*x^2+3*x*y+y^2")
M=10*x+3*y;show("M(x,y)=",M)
N=3*x+2*y;show("N(x,y)=",N)
My=diff(M,y);show("My(x,y)=",My)
Nx=diff(N,x);show("N(x,y)=",Nx)
f=5*x^2+3*x*y+y^2;show("f(x,y)=",f)
g=f.gradient();show("grad(x,y)=",g)
show("")

#5) Show that F(x,y)=<x^2*y,x*y> is NOT conservative 
show("#5) Show that F(x,y)=<x^2*y,x*y> is NOT conservative")
M=x^2*y;show("M(x,y)=",M)
N=x*y;show("N(x,y)=",N)
My=diff(M,y);show("My(x,y)=",My)
Nx=diff(N,x);show("N(x,y)=",Nx)
show("")

#6) Find the potential function for the conservative Vector Field F(x,y)=<2*x*y,x^2-y>
show("#6) Find the potential function for the conservative Vector Field F(x,y)=<2*x*y,x^2-y>")
M=2*x*y;show("M(x,y)=",M,"=fx(x,y)")
N=x^2-y;show("N(x,y)=",N,"=fy(x,y)")
My=diff(M,y);show("My(x,y)=",My)
Nx=diff(N,x);show("N(x,y)=",Nx)
show("f(x,y)=",integral(M,x),"+g(y)")
show("f(x,y)=",integral(N,y),"+h(x)")
show("f(x,y)=",x^2*y-y^2/2,"+K")
