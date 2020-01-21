#MrG 2018.0630 UMC25 Cylindrical Coordinates
#1) Find the volume of the solid bounded above by z=2-x^2-y^2 and bounded below by z=x^2+y^2
show("#1) Find the volume of the solid bounded above by z=2-x^2-y^2 and bounded below by z=x^2+y^2")
var('r,t,z')
show(integral(integral(integral(r,z,r^2,2-r^2),r,0,1),t,0,2*pi))

