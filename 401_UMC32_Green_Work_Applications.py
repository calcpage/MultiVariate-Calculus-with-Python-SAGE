#MrG 2018.0630 UMC32 Applications of Green's Theorem 
#1) Let R be the region bounded by y=x and y=x^2-2*x
#1) Find the Line Integral of (y-x)dx+(2*x-y)dy
show("#1) Let R be the region bounded by y=x and y=x^2-2*x")
show("#1) Find the Line Integral of (y-x)dx+(2*x-y)dy")
var('y')
M=y-x;show("M=",M)
N=2*x-y;show("N=",N)
Nx=diff(N,x);show("Nx=",Nx) #Nx!=My means F is a
My=diff(M,y);show("My=",My) #non conservative field!
show("integral(integral(1,y,x^2-2*x,x),x,0,3)=",integral(integral(1,y,x^2-2*x,x),x,0,3))
show("")

#2) Planimeter uses Green's Theorem by tracing out boundary of the region:
#2) To calculate planar areas find the Line Integral of xdy-ydx divided by 2 over the path C enclosing the area:
#2) Find the area enclosed by the ellipse: x^2/a^2+y^2/b+2=1 which is parametrized as <a*cos(t),b*sin(t)> for 0<=t<=2*pi
show("#2) Planimeter uses Green's Theorem by tracing out boundary of the region:")
show("#2) To calculate planar areas find the Line Integral of xdy+ydx over the path C enclosing the area:")
show("#2) Find the area enclosed by the ellipse: x^2/a^2+y^2/b+2=1 which is parametrized as <a*cos(t),b*sin(t)> for 0<=t<=2*pi")
var('a,b,t')
show("Line Integral of xdy+ydx over C =",integral(a*cos(t)*b*cos(t)-b*sin(t)*(-a)*sin(t),t,0,2*pi)/2)
