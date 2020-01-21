#UMC02 NOTES: Functions Of Several Variables
#1) sphere
show('sphere')
var('y')
p1=plot3d(sqrt(4-x^2-y^2),(x,-2,2),(y,-2,2))
p2=plot3d(-sqrt(4-x^2-y^2),(x,-2,2),(y,-2,2))
#show(p1+p2,aspect_ratio=(1,1,1))

#2) parabaloid
show('parabaloid')
show(expand(5-(x-1)^2-(y-2)^2))
plot3d(5-(x-1)^2-(y-2)^2,(x,-1,3),(y,0,4),aspect_ratio=1).show()

#3) plane
show('plane')
plot3d(x+y,(x,-5,5),(y,-5,5)).show()

#4) what is it?
show('what is it?')
var('z')
show(solve(4*x^2+y^2+z^2==4,z))
p1=plot3d(sqrt(-4*x^2 - y^2 + 4),(x,-2,2),(y,-2,2))
p2=plot3d(-sqrt(-4*x^2 - y^2 + 4),(x,-2,2),(y,-2,2))
#show(p1+p2,aspect_ratio=(1,1,1))
implicit_plot3d(4*x^2+y^2+z^2==4,(x,-2,2),(y,-2,2),(z,-2,2)).show(aspect_ratio=(1,1,1))
