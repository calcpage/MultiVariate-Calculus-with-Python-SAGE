#MrG 2018.0630 UMC31 Green's Theorem for Line Inegrals and Work in the Plane:
#Line Integral of Ndx+Ndy over the path C = Double Integral (Nx-My)dA over the region R 
#1a) Let R be the region bounded by y=x and y=x^2. Let C be the boundary of R oriented CCW. 
#1a) Find the Line Integral of y^2dx+x^2dy
show("#1) Let R be the region bounded by y=x and y=x^2. Let C be the boundary of R oriented CCW.")
show("#1) Find the Line Integral of y^2dx+x^2dy")
var('y,t')
M=y^2;show("M=",M)
N=x^2;show("N=",N)
Nx=diff(N,x);show("Nx=",Nx) #Nx!=My means F is a
My=diff(M,y);show("My=",My) #non conservative field!
r1=vector([t,t^2]);show("r1=",r1) #let path C=C1+C2, C1 goes along parabola from point (0,0) to point (1,1) so 0<=t<=1
v1=diff(r1,t);show("v1=",v1)
show("Line Integral of y^2dx+x^2dy over C1 = integral((t^2)^2*(1)+(t)^2*(2*t),t,0,1)=",integral((t^2)^2*(1)+(t)^2*(2*t),t,0,1))
r2=vector([2-t,2-t]);show("r2=",r2) #let path C=C1+C2, C2 goes along line from point (1,1) to point (0,0) so 1<=t<=2
v2=diff(r1,t);show("v2=",v2)
show("Line Integral of y^2dx+x^2dy over C2 = integral((2-t)^2*(-1)+(2-t)^2*(-1),t,1,2)=",integral((2-t)^2*(-1)+(2-t)^2*(-1),t,1,2))
show("Total Line Integral over C1+C2=",7/10-2/3)
show("")

#1b) Redo 1a by Green's Theorem! Find doube integral of Nx-My over dA
show("#1b) Redo 1a by Green's Theorem! Find doube integral of Nx-My over dA")
show("integral(integral(Nx-My,y,x^2,x),x,0,1)=",integral(integral(Nx-My,y,x^2,x),x,0,1))
show("")

#2) A particle moves once CCW along x^2+y^2=9 subject to the Force Field F=<y^3,x^3+3*x*y^2>
#2) Use Green's Theorem to find the total work done by the Force Field.
show("#2) A particle moves once CCW along x^2+y^2=9 subject to the Force Field F=<y^3,x^3+3*x*y^2>")
show("#2) Use Green's Theorem to find the total work done by the Force Field.")
M=y^3;show("M=",M)
N=x^3+3*x*y^2;show("N=",N)
Nx=diff(N,x);show("Nx=",Nx) #Nx!=My means F is a
My=diff(M,y);show("My=",My) #non conservative field!
show("integral(integral(Nx-My,y,-sqrt(x^2-9),sqrt(x^2-9)),x,-3,3)=",integral(integral(Nx-My,y,-sqrt(x^2-9),sqrt(x^2-9)),x,-3,3)) #cartesian
var('r,t')
show("integral(integral(3*r^2*cos(t)^2*r,r,0,3),t,0,2*pi)=",integral(integral(3*r^2*cos(t)^2*r,r,0,3),t,0,2*pi)) #polar
show("")

#3) Evaluate the Line Integral for y^3dx+3*x*y^2dy where the path C is x^2+y^2=9 (or any closed curve)
show("#3) Evaluate the Line Integral for y^3dx+3*x*y^2dy where the path C is x^2+y^2=9 (or any closed curve)")
M=y^3;show("M=",M)
N=3*x*y^2;show("N=",N)
Nx=diff(N,x);show("Nx=",Nx) #Nx!=My means F 
My=diff(M,y);show("My=",My) #IS conservative!
show("Line Integral is 0 OVER ANY CLOSED CURVE C since field is Conservative such that Nx-My=0")
