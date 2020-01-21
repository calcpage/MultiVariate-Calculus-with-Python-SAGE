#MrG 2018.0702 NCC17 Polar Coordinates 
#1) Volume under z=1-x^2-y^2 above quarter disc R:x^2+y^2<1 in the first quadrant
show("#1) Volume under z=1-x^2-y^2 above quarter disc R:x^2+y^2<1 in the first quadrant")
var('r,t')
show(integral(integral((1-r^2)*r,r,0,1),t,0,pi/2))
show("")
