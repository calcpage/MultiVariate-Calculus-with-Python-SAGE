#MrG 2018.0722 UMC34 Surface Integrals & Flux (Filk: Physics Rap + Carl Sagan on Pale Blue Dot)
#1) Evaluate the Double Integral over S of F(x,y,z)=y^2+2*y*z
#1) Let S be the 1st Octant portion of the plane z=3-x-y/2
#1) Let G(x,y,z)=0=z+x+y/2-3
show("#1) Evaluate the Double Integral over S of F(x,y,z)=y^2+2*y*z")
show("#1) Let S be the 1st Octant portion of the plane z=g(x,y)=3-x-y/2")
var('y,z')
g=3-x-y/2;show("g(x,y,z)=",g)
gx=diff(g,x);show("gx(x,y,z)=",gx)
gy=diff(g,y);show("gy(x,y,z)=",gy)
dS=sqrt(1+gx^2+gy^2);show("dS=",dS)
F=y^2+2*y*(3-x-y/2);show("F(x,y)=",F)
show(integral(integral(F*3/2,y,0,6-2*x),x,0,3))
show("")

#2) Consider a cup given by S: z=sqrt(9-x^2-y^2)
#2) Find the mass of the cup given rho(x,y,z)=2*z
show("#2) Consider a cup given by S: z=g(x,y)=sqrt(9-x^2-y^2)")
show("#2) Find the mass of the cup given rho(x,y,z)=2*z")
g=sqrt(9-x^2-y^2);show("g(x,y,z)=",g)
gx=diff(g,x);show("gx(x,y,z)=",gx)
gy=diff(g,y);show("gy(x,y,z)=",gy)
dS=sqrt(1+gx^2+gy^2);show("dS=",dS.canonicalize_radical())
F=2*sqrt(9-x^2-y^2);show("F(x,y)=",F)
show("double integral of 6*dA = 6*pi*3^2 = 54pi")
show("")

#3) Let S be the portion of the paraboloid z=4-x^2-y^2 above the xy-plane
#3) Let S be oriented with unit normal N point upward & F(x,y)=<x,y,z>
#3) Find the Double Integral over S of F.NdS = rate of flow through the surface = Flux in Space
show("#3) Let S be the portion of the paraboloid z=g(x,y)=4-x^2-y^2 above the xy-plane")
show("#3) Let S be oriented with unit normal N point upward & F(x,y)=<x,y,z>")
show("#3) Find the Double Integral over S of F.NdS = rate of flow through the surface = Flux in Space")
g=4-x^2-y^2;show("g(x,y)=",g)
gx=diff(g,x);show("gx(x,y)=",gx)
gy=diff(g,y);show("gy(x,y)=",gy)
G=z-g;show("G(x,y,z)=",G)
Gx=diff(G,x);show("Gx(x,y,z)=",Gx)
Gy=diff(G,y);show("Gy(x,y,z)=",Gy)
dS=sqrt(1+gx^2+gy^2);show("dS=",dS)
F=vector([x,y,4-x^2-y^2]);show("F(x,y,z)=",F)
show("grad(G)=",G.gradient())
show("abs(grad(G))=",abs(G.gradient()))
N=G.gradient()/abs(G.gradient());show("N=",N)
NdS=N*dS;show("NdS=",NdS)
FNdS=F.dot_product(NdS);show("F.NdS=",FNdS)
var('r,t')
show(integral(integral((4+r^2)*r,r,0,2),t,0,2*pi))
