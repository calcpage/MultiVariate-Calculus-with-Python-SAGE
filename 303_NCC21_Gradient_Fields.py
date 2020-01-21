#MrG 2018.0702 NCC21 Gradient Fields
#1) If F(x,y)=<M,N>=<fx,fy> be a vector field and Nx=fyx and My=fxy ,the F is a Gradient Field with Potential f if Nx=My=0
#1) Show that F(x,y)=<-y,x> is not a Gradient Field
show("#1) Show that F(x,y)=<-y,x> is not a Gradient Field")
var('y')
M=-y;show("M(x,y)=",M);show("My=fxy=",diff(M,y))
N=x;show("N(x,y)=",N);show("Nx=fyx=",diff(N,x))
show("curl(F)=Nx-My=",diff(N,x)-diff(M,y),"= twice angular velocity of retational field")
show("")

#2a) Find a such that F(x,y)=<4*x^2+a*x*y,3*y^2+4*x^2> such that F a Gradient Field
show("#2a) Find a such that F(x,y)=<4*x^2+a*x*y,3*y^2+4*x^2> such that F a Gradient Field")
var('a')
M=4*x^2+a*x*y;show("M(x,y)=",M);show("My=fxy=",diff(M,y))
N=3*y^2+4*x^2;show("N(x,y)=",N);show("Nx=fyx=",diff(N,x))
show(solve(diff(N,x)-diff(M,y),a))
show("")

#2b) Find the potential function f such that f.gradient()=F(x,y)=<4*x^2+a*x*y,3*y^2+4*x^2> with a=8
show("#2b) Find the potential function f such that f.gradient()=F(x,y)=<4*x^2+a*x*y,3*y^2+4*x^2> with a=8")
M=4*x^2+8*x*y;show("M(x,y)=",M);show("My=fxy=",diff(M,y))
N=3*y^2+4*x^2;show("N(x,y)=",N);show("Nx=fyx=",diff(N,x))
show("f(x,y)=integral(M,x)=",integral(4*x^2+8*x*y,x)," + g(y)")
show(diff(integral(4*x^2+8*x*y,x),y)," + g'(y)")
show("g(y)=integral(3*y^2,y)=",integral(3*y^2,y)," + C")
show("f(x,y)=",integral(4*x^2+8*x*y,x)+integral(3*y^2,y)," + C")
