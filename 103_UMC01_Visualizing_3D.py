#UMC01 NOTES: A Visual Introduction To 3D Calculus
#1) graph sphere with diameter endpoints P(4,-2,3) and Q(0,4,-3)
show("#1) graph sphere with diameter endpoints P(4,-2,3) and Q(0,4,-3)")
var('y,z')
d=sqrt((0-4)^2+(4+2)^2+(-3-3)^2);show("d=",d);show("d=",d.n())
r=d/2;show("r=",r);show("r=",r.n())
show(solve((x-2)^2+(y-1)^2+(z)^2==22,z))
#p1=plot3d(sqrt(-x^2 - y^2 + 4*x + 2*y + 17),(x,2-r,2+r),(y,1-r,1+r),color='red')
#p2=plot3d(-sqrt(-x^2 - y^2 + 4*x + 2*y + 17),(x,2-r,2+r),(y,1-r,1+r),color='green')
#show(p1+p2,aspect_ratio=1)
implicit_plot3d((x-2)^2+(y-1)^2+(z)^2==22,(x,2-r,2+r),(y,1-r,1+r),(z,-r,+r)).show()
show("")

#2) graph paraboloid z=x^2+y^2
show("#2) graph paraboloid z=x^2+y^2")
#plot3d(x^2+y^2,(x,-2,2),(y,-2,2))
