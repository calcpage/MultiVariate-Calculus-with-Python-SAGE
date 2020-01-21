#MrG 2018.0722 UMC36 Stokes' Thm
#1a) Let S: portion of z=4-x^2-y^2 above xy-plane and F=<2*z,x,y^2>
#1a) Use Stokes' Thm to find the Line Integral over the closed path C: x^2+y^2=4 for Work: F.dr
show("#1) Let S: portion of z=4-x^2-y^2 above xy-plane and F=<2*z,x,y^2>")
show("#1) Find Line Integral over the closed path C: x^2+y^2=4 for Work: F.dr")
var('y,z')
F=vector([2*z,x,y^2]);show("F(x,y,z)=",F)
curlF=F.curl(variables=[x,y,z]);show("curlF=",curlF)
G=z-(4-x^2-y^2);show("G(x,y,z)=",G)
gradG=G.gradient();show("gradG=",gradG)
magGradG=abs(gradG);show("abs(gradG)=",magGradG)
N=gradG/magGradG;show("N=",N)
Gx=diff(G,x);show("Gx=",Gx)
Gy=diff(G,y);show("Gy=",Gy)
dS=sqrt(1+Gx^2+Gy^2);show("dS=",dS)
NdS=N*dS;show("N*dS=",NdS)
curlFNdS=curlF.dot_product(NdS);show("curlF.NdS=",curlFNdS)
show(integral(integral(curlFNdS,y,-sqrt(4-x^2),sqrt(4-x^2)),x,-2,2))
show("")

#1b) Let S: portion of z=4-x^2-y^2 above xy-plane and F=<2*z,x,y^2>
#1b) Use Parameterization to find the Line Integral over the closed path C: x^2+y^2=4 for Work: F.dr
show("#2) Let S: portion of z=4-x^2-y^2 above xy-plane and F=<2*z,x,y^2>")
show("#2) Use Parameterization to find the Line Integral over the closed path C: x^2+y^2=4 for Work: F.dr")
var('t')
r=vector([2*cos(t),2*sin(t),0]);show("r(t)=",r)
v=diff(r,t);show("v(t)=",v)
Fdr=F.dot_product(v);show("F.dr=",Fdr)
show(integral(4*cos(t)^2,t,0,2*pi))
show("")

#2) Let S: portion of z=4-x^2-y^2 above xy-plane and F=<y*z*e^x,z*e^x,y*e^x>
#2) Use Stokes' Thm to show the Line Integral over the closed path C: x^2+y^2=4 for Work: F.dr = 0!
F=vector([y*z*e^x,z*e^x,y*e^x]);show("F(x,y,z)=",F)
curlF=F.curl(variables=[x,y,z]);show("curlF=",curlF)
