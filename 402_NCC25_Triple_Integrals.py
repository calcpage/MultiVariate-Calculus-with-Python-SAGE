#MrG 2018.0630 NCC25 Triple Integrals and Cylindrical Coordinates (Filk: Science Wars + Grace Hopper on 60 Minutes)
#1) Find the volume of the solid bounded above by z=4-x^2-y^2 and bounded below by z=x^2+y^2
show("#1a) Find the volume of the solid bounded above by z=4-x^2-y^2 and bounded below by z=x^2+y^2 using dV=dzrdrdt")
var('r,t,z')
show(integral(integral(integral(r,z,r^2,4-r^2),r,0,sqrt(2)),t,0,2*pi))
show("")

show("#1b) Find the volume of the solid bounded above by z=4-x^2-y^2 and bounded below by z=x^2+y^2 using dV=dzdydx")
var('y')
show(integral(integral(integral(1,z,x^2+y^2,4-x^2-y^2),y,-sqrt(2-x^2),sqrt(2-x^2)),x,-sqrt(2),sqrt(2)))
