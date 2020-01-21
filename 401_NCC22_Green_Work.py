#MrG 2018.0702 NCC22 Green's Theorem for Work in the Plane (Filk: Space Oddity + deGrasse Tyson on Apophis)
#1) If C is a positively oriented closed curve enclosing a region R and the Vector Field F is defined and differentiable in R
#1) Then the Line Integral for Work of F.dr = M*dx+N*dy over C = the double integral over R of curl(F)dA = (Nx-My)dA
#1) Evaluate Line Integral: M*dx+N*dy = y*e^(-x)*dx+x^2/2-e^(-x)*dy for R = unit disk at (2,0)
show("#1) Evaluate Line Integral: M*dx+N*dy = y*e^x*dx+x^2/2-e^(-x)*dy for R = unit disk at (2,0)")
var('y')
M=y*e^(-x);show("M(x,y)=",M);show("My=fxy=",diff(M,y))
N=x^2/2-e^(-x);show("N(x,y)=",N);show("Nx=fyx=",diff(N,x))
show("curl(F)=Nx-My=",diff(N,x)-diff(M,y))
show(integral(integral(x,y,-sqrt(1-(x-2)^2),sqrt(1-(x-2)^2)),x,1,3)) 
show("")

#2) If F is a Conservative Field, then Nx-My=0 so the Line Integral for Work=0 over any R since path independent
show("#2) If F is a Conservative Field, then Nx-My=0 so the Line Integral for Work=0 over any R since path independnent")
M=x^2*y+x;show("M(x,y)=",M);show("My=fxy=",diff(M,y))
N=x^3/3-1;show("N(x,y)=",N);show("Nx=fyx=",diff(N,x))
show("curl(F)=Nx-My=",diff(N,x)-diff(M,y))
show(integral(integral(0,y,-sqrt(1-(x-2)^2),sqrt(1-(x-2)^2)),x,1,3)) 
show("")
