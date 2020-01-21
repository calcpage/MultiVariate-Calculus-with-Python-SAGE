#MrG 2018.0721 NCC31 Stokes' Theorem (Filk: Symphony Of Science + http://www.maxwells-equations.com, MIT33, UMC36
#1a) If C is a closed curve and S is any surface bounded by C, 
#1a) then the Line Integral of F.dr over C = the Double Integral of curlF.NdS over S.
show("#1a) If C is a closed curve and S is any surface bounded by C, ")
show("#1a) then the Line Integral of F.dr over C = the Double Integral of curlF.NdS over S.")
show("")

#1b) Let S be a portion of the xy-plane bounded by a closed curve C CCW,
#1b) Then the Line Integral of F.dr over C = the Line Integral of Pdx+Qdy over C is, by Green's Thm:
#1b) The Double Integral of Qx-Py over S = Double Integral curlF.k*dx*dy =
#1b) Double Integral curlF.NdS over S. So Stoke's in Space is an extension of Greens' in the Plane
show("#1b) Let S be a portion of the xy-plane bounded by a closed curve C CCW,")
show("#1b) Then the Line Integral of F.dr over C = the Line Integral of Pdx+Qdy over C is, by Green's Thm:")
show("#1b) The Double Integral of Qx-Py over S = Double Integral curlF.k*dx*dy =")
show("#1b) Double Integral curlF.NdS over S. So Stoke's in Space is an extension of Greens' in the Plane")
show("")

#2a Remember grad, div, curl? Let f(x,y,z)=x^2*y+x*z-y*x^3 and F(x,y,z)=<z,x,y>
var('y,z')
show("#2a Remember grad, div, curl? Let f(x,y,z)=x^2*y+x*z-y*x^3 and F(x,y,z)=<z,x,y>")
gradf=(x^2*y+x*2-y*z^3).gradient(variables=(x,y,z));show("gradf=",gradf)
divF=vector([z,x,y]).div(variables=(x,y,z));show("divF=",divF)
curlF=vector([z,x,y]).curl(variables=(x,y,z));show("curlF=",curlF)
show("")

#2b) F=<z,x,y>, C: unit circle in xy-plance CCW, S: piece of paraboloid z=1-x^2-y^2, find work!
show("#2b) F=<z,x,y>, C: unit circle in xp-plance CCW, S: piece of paraboloid z=1-x^2-y^2, find work!")
var('t')
F=vector([z,x,y]);show("F(x,y,z)=",F)
r=vector([cos(t),sin(t),0]);show("r(t)=",r)
v=diff(r,t);show("v(t)=",v)
Fdr=F.dot_product(v);show("Fdr=",Fdr)
show(integral(cos(t)*cos(t),t,0,2*pi))
show("")

#2c) Redo by Stokes' Thm:
#2c) F=<z,x,y>, C: unit circle in xp-plance CCW, S: piece of paraboloid z=1-x^2-y^2, find work!
show("#2c) Redo by Stokes' Thm:")
show("#2c) F=<z,x,y>, C: unit circle in xp-plance CCW, S: piece of paraboloid z=1-x^2-y^2, find work!")
z=1-x^2-y^2;show("z=",z)
zx=diff(z,x);show("zx=",zx)
zy=diff(z,y);show("zy=",zy)
curlFNdS=curlF.dot_product(vector([-zx,-zy,1]));show("curlFNdS=",curlFNdS)
show(integral(integral(curlFNdS,x,-sqrt(1-y^2),sqrt(1-y^2)),y,-1,1))

#3a) SUMMARY: GREEN'S THM FOR WORK IN THE PLANE: F=<M,N> (R is vertically simple, W=0 if F is conservative)
#3a) Line Integral over closed path C CCW for F.dr = Double Integral over R bounded by C for curlF*dA
#3a) Line Integral over closed path C CCW for Mdx+Ndy = Double Integral over R bounded by C for (Nx-My)*dA
#3b) SUMMARY: STOKES' THM FOR WORK IN SPACE: F=<P,Q,R> (normal N points by RHR, W=0 if F is conservative)
#3b) Line Integral over closed path C CCW for F.dr = Double Integral over S bounded by C for curlF.NdS
#3b) Line Integral over closed path C CCW for Pdx+Qdy+Rdz = Double Integral over S bounded by C for <Ry-Qz,Rx-Pz,Qx-Py>.NdS

#4a) SUMMARY: GREEN'S THM FOR FLUX IN THE PLANE: F=<P,Q> (normal n pointing outward from R, R is vertically simple)
#4a) Line Integral over closed path C CCW for F.nds = Double Integral over R bounded by C for divF*dA
#4a) Line Integral over closed path C CCW for -Qdx+Pdy = Double Integral over R bounded by C for (Px+Qy)*dA
#4b) SUMMARY: DIVERGENCE THM FOR FLUX IN THE PLANE: F=<P,Q,R> (normal n pointing outward from S)
#4b) Line Integral over closed surface S for F.Nds = Triple Integral over solid Q bounded by S for divF*dV = (Px+Qy+Rz)*dV

#4) For all 4 throerms, F is defined, continuous and differentialble over all of C, R and V
