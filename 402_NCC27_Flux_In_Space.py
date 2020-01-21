#MrG 2018.0721 NCC27 Flux and Vector Fields in Space
#1) F is a Vector Field measuring Fluid Flow: 
#1) Let F(x,y)=<P,Q>, then flux = Line Integral over a path C of F.Nds
#1) In the plane, Flux measures flow per unit time across s (arc)
#1) Let F(x,y,z)=<P,Q,R>, then flux = Double Integral over a surface S of F.NdS
#1) In space, Flux measures flow per unit time across S (surface)
show("#1) F is a Vector Field measuring Fluid Flow: ")
show("#1) Let F(x,y)=<P,Q>, then flux = Line Integral over a path C of F.Nds")
show("#1) In the plane, Flux measures flow per unit time across s (arc)")
show("#1) Let F(x,y,z)=<P,Q,R>, then flux = Double Integral over a surface S of F.NdS")
show("#1) In space, Flux measures flow per unit time across S (surface)")
show("")

#2) F=<x,y,x>, S: x^2+y^2+z^2=a^2, N=<x,y,z>/a, F.N=a
#2) Note: Line Integral in the Plane can be parametrized over path C with a single parameter,
#2) Note: Double Integral in Space can be parametrized over surface S with two parameters.
#2) Note: Here we look for a simple geometric interpretation to evaluate the double integral!
show("#2) F=<x,y,x>, S: x^2+y^2+z^2=a^2, N=<x,y,z>/a, F.N=a")
var('y,z,a')
F=vector([x,y,z]);show("F(x,y,z)=",F)
N=vector([x/a,y/a,z/a]);show("N=",N)
FN=F.dot_product(N);show("F.N=",FN) #(x^2+y^2+z^2)/a=a^2/a=a
show("if surface area of S=4*pi*a^2, then double integral over S of a*dS=a*4*pi*a^2=4*pi*a^3")

#3) Plotting Vector Fields in 3D!
#show(plot_vector_field3d([x,y,z],(x,-3,3),(y,-3,3),(z,-3,3),colors=['red','green','blue']))
#a = plot_vector_field((x,y), (x,-3,3), (y,-3,3), color='blue')
#b = plot_vector_field((y,-x), (x,-3,3), (y,-3,3), color='red')
#show(a + b)
#a = plot_vector_field3d((x,y,0), (x,-3,3), (y,-3,3),(z,-3,3), colors='blue')
#b = plot_vector_field3d((y,-x,0), (x,-3,3), (y,-3,3),(z,-3,3), colors='red')
#show(a + b)

#4a) If S is z=a parallel to xy-plane, then N=+/-k, dS=dxdy
#4b) (optional) If S is sphere of radius a centered at the origin, then N=<x,y,z>/a, dS=a^2(sin(phi))*dphi*dtheta
#4c) If S is cylinder of radius a centered on z-axis, then N=<x,y,0>/a, dS=a*dz*dtheta
#4d) If S is z=f(x,y), then NdS=<-fx,-fy,1>dxdy because:
#4d) We let G=z-f(x,y)=0 be a Level Curve, then del(G)=<-fx,-fy,1> is the gradient vector normal to the Level Curve:
#4d) N=del(G)/abs(G)=<-fx-fy+1>/(sqrt(fx^2+fy^2+1)) 
#4d) N*dS=<-fx-fy+1>/(sqrt(fx^2+fy^2+1))*sqrt(fx^2+fy^2+1)*dA=<-fx,-fy,1>dA
#4d) F.N*dS=<P,Q,R>.<-fx,-fy,1>*dA

