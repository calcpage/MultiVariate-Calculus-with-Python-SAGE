#MrG 2018.0721 NCC28 Finding dS & Divergence Thm
#1) dS is a small portion of surface contributing small amount of Flux to sum up
#1) Let dS lie above dxdy, a small portion of the xy-plane. dS has vertices:
#1) (x,y,f(x,y)), (x+dx,y,f(x+dx,y)), (x,y+dy,f(x,y+dy)), (x+dx,y+dy,f(x+dx,y+dy))
#1) Linear Approximation: f(x+dx,y)=f(x,y)+fx*dx and f(x,y+dy)=f(x,y)+fy*dy
#1) Sides are vectors: <dx,0,fx*dx>, <0,dy,fy*dy> = <1,0,fx>dx, <0,d1,fy>dy
#1) Area: dS=+/-<1,0,fx>.cross_product(<0,d1,fy>)dxdy = +/-<-fx,-fy,1>dxdy
#1) N: dir(dS)=<-fx,-fy,1>/abs(<-fx,-fy,1>)=<-fx,-fy,1>/(fx^2+fy^2+1)
#1) N: mag(dS)=abs(<-fx,-fy,1>)=(fx^2+fy^2+1)dxdy
#1) F=<0,0,z>, S is portion of paraboloid z=x^2+y^2 over unit disk x^+y^2<=1 
#1) with N pointing up and NdS = <-2x,-2y,1>dxdy
show("#1) F=<0,0,z>, S is portion of paraboloid z=x^2+y^2 over unit disk x^+y^2<=1 ")
show("#1) with N pointing up and NdS = <-2x,-2y,1>dxdy")
var('y,r,t')
F=vector([0,0,x^2+y^2]);show("F=",F)
NdS=vector([-2*x,-2*y,1]);show("NdS=",NdS)
FNdS=F.dot_product(NdS);show("F.NdS=",FNdS)
show("integral(integral(FNdS,x,-sqrt(1-y^2),sqrt(1-y^2)),y,-1,1)=",integral(integral(FNdS,x,-sqrt(1-y^2),sqrt(1-y^2)),y,-1,1))
show("integral(integral(r^2*r,r,0,1),t,0,2*pi)=",integral(integral(r^2*r,r,0,1),t,0,2*pi))
show("")

#2) Divergence Thm: 3D analogue of Green's Thm for Flux in the Plane
#2) If S is a closed surface bounding a region D, then
#2) double integral over S of F.NdS = triple integral over D of divF dV
#2) div(F)=del.dot_product(F)=del.dot_product(P,Q,R)=Px+Qy+Rz
show("#2) Divergence Thm: 3D analogue of Green's Thm for Flux in the Plane")
show("#2) If S is a closed surface bounding a region D, then")
show("#2) double integral over S of F.NdS = triple integral over D of divF dV")
show("#2) div(F)=del.dot_product(F)=del.dot_product(P,Q,R)=Px+Qy+Rz")
var('z')
F=vector([0,0,z]);show("F(x,y,z=",F)
divF=0+0+1;show("divF=",divF)
show("ex: double integral of F.NdS over sphere of radius a at the origin=")
show("ex: triple integral of 1 dV = (4/3)*pi*a^3")
