#MrG 2018.0722 UMC35 Divergence Thm
#1) Let Q be the solid between the paraboloid z=4-x^2-y^2 and the xy-plane z=0. Let F(x,y,z)=<2*z,x,y^2>
#1a) Evaluate the Flux Integral of F through the circular portion S1 along z=0 of the closed surface of Q: F.N*dS
show("#1) Let Q be the solid between the paraboloid z=4-x^2-y^2 and the xy-plane z=0. Let F(x,y,z)=<2*z,x,y^2>")
show("#1a) Evaluate the Flux Integral of F through the circular portion S1 along z=0 of the closed surface of Q: F.N*dS")
var('y,z')
F=vector([2*z,x,y^2]);show("F(x,y,z)=",F)
N=vector([0,0,-1]);show("N=",N)
FN=F.dot_product(N);show("F.N=",FN)
var('r,t')
show(integral(integral(-(r*sin(t))^2*r,r,0,2),t,0,2*pi))
show("")

#1b)Evaluate the Flux Integral of F through the paraboloid portion S2 along z=4-x^2-y^2 of the closed surface of Q: F.N*dS
show("#1b)Evaluate the Flux Integral of F through the paraboloid portion S2 along z=g(x,y)=4-x^2-y^2 of the closed surface of Q: F.N*dS")
g=4-x^2-y^2;show("g(x,y)=",g)
gx=diff(g,x);show("gx(x,y)=",gx)
gy=diff(g,y);show("gy(x,y)=",gy)
G=z-g;show("G(x,y,z)=",G)
Gx=diff(G,x);show("Gx=",Gx)
Gy=diff(G,y);show("Gx=",Gy)
dS=sqrt(1+gx^2+gy^2);show("dS=",dS)
gradG=G.gradient();show("gradG=",gradG)
magGradG=abs(gradG);show("abs(gradG)=",magGradG)
N=gradG/magGradG;show("N=",N)
NdS=N*dS;show("N*dS=",NdS)
FNdS=F.dot_product(NdS);show("F.NdS=",FNdS)
show(integral(integral(FNdS,x,-sqrt(4-y^2),sqrt(4-y^2)),y,-2,2))
show("")

#1c) Verify that The Divergence Thm also gives flux=0
show("#1c) Verify that The Divergence Thm also gives flux=0")
divF=F.div(variables=[x,y,z]);show("divF=",divF)
show("")

#2) Find the Flux Integral over S: x^2+y^2+z^2=4 for F=<x,y,z>
show("#2) Find the Flux Integral over S: x^2+y^2+z^2=4 for F=<x,y,z>")
F=vector([x,y,z]);show("F=",F)
divF=F.div(variables=[x,y,z]);show("divF=",divF)
show("3*(triple integral of dV over the solid Q) =", 3*(4/3*pi*2^3))
