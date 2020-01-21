#MrG 2018.0630 UMC24 Triple Integrals
#1) Evaluate and Interpret: integral(integral(integral(1,z,0,2),y,0,3),x,0,4)
show("#1) Evaluate and Interpret: integral(integral(integral(1,z,0,2),y,0,3),x,0,4)")
var('y,z')
show(integral(integral(integral(1,z,0,2),y,0,3),x,0,4))
show("")

#2) Evaluate and Interpret: integral(integral(integral(1,z,0,1-y),x,0,2),y,0,1)
show("#2) Evaluate and Interpret: integral(integral(integral(1,z,0,1-y),x,0,2),y,0,1)")
show(integral(integral(integral(1,z,0,1-y),x,0,2),y,0,1))

#3) Evaluate and Interpret: integral(integral(integral(1,z,x^2+y^2,2-x^2-y^2),y,-sqrt(1-x^2),sqrt(1-x^2)),x,-1,1)
show("#3) Evaluate and Interpret: integral(integral(integral(1,z,x^2+y^2,2-x^2-y^2),y,-sqrt(1-x^2),sqrt(1-x^2)),x,-1,1)")
show(integral(integral(integral(1,z,x^2+y^2,2-x^2-y^2),y,-sqrt(1-x^2),sqrt(1-x^2)),x,-1,1))

#4) Find the mass of the unit cube in the first octant when rho is proportional to the square of the distance from the origin
show("#4) Find the mass of the unit cube in the first octant when rho is proportional to the square of the distance from the origin")
var('k')
show(integral(integral(integral(k*(x^2+y^2+z^2),z,0,1),y,0,1),x,0,1))
