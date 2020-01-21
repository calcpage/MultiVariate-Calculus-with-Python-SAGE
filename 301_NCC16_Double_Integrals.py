#MrG 2018.0702 NCC16 Double Integrals
#1) Evaluate and Interpret: integral(integral(1-x^2-y^2,y,0,1),x,0,1)
show("#1) Evaluate and Interpret: integral(integral(1-x^2-y^2,y,0,1),x,0,1)")
show("#1) Volume above unit square on the xy-plane below parabaloid z=1-x^2-y^2")
var('y')
show("integral(1-x^2-y^2,y)=",integral(1-x^2-y^2,y))
show("integral(1-x^2-y^2,y,0,1)=",integral(1-x^2-y^2,y,0,1))
show("integral(-x^2+2/3,x)=",integral(-x^2+2/3,x))
show("integral(-x^2+2/3,x,0,1)=",integral(-x^2+2/3,x,0,1))
show("integral(integral(1-x^2-y^2,y,0,1),x,0,1)=",integral(integral(1-x^2-y^2,y,0,1),x,0,1)) 
show("")

#2) Volume under z=1-x^2-y^2 above quarter disc R:x^2+y^2<1 in the first quadrant
show("#2) Volume under z=1-x^2-y^2 above quarter disc R:x^2+y^2<1 in the first quadrant")
show(integral(integral(1-x^2-y^2,y,0,sqrt(1-x^2)),x,0,1))
show("")

#3) Evaluate: integral(integral(e^y/y,y,x,sqrt(x)),x,0,1)
show("#3) Evaluate: integral(integral(e^y/y,y,x,sqrt(x)),x,0,1)")
# show(integral(integral(e^y/y,y,x,sqrt(x)),x,0,1)) can't find antiderivative!
show(integral(integral(e^y/y,x,y^2,y),y,0,1)) #exchange order of integration!
show(integral(integral(e^y/y,x,y^2,y),y,0,1).n())
