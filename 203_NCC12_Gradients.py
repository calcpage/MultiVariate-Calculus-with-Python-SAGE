#MrG 2018.0629 NCC12 Gradients
#1) Chain Rule: df/dt=fx*dx/dt+fy*dy/dt+fz*dz/dt
#1) Let grad=del(f)=<fx,fy,fz>, dr/dt=<dx/dt,dy/dt,dz/dt>
#1) Chain Rule: df/dt=del(f).dot_product(dr/dt)
show("#1) Chain Rule: df/dt=fx*dx/dt+fy*dy/dt+fz*dz/dt")
show("#1) Let grad=del(f)=<fx,fy,fz>, dr/dt=<dx/dt,dy/dt,dz/dt>")
show("#1) Chain Rule: df/dt=del(f).dot_product(dr/dt)")
show("")

#2) Find a Tangent Plane to the surface x^2+y^2-z^2=4 at the point (2,1,1)
show("#2) Find a Tangent Plane to the surface x^2+y^2-z^2=4 at the point (2,1,1)")
var('y,z')
f=x^2+y^2-z^2-4;show("f=",f)
fx=diff(f,x);show("fx=",fx)
fy=diff(f,y);show("fy=",fy)
fz=diff(f,z);show("fz=",fz)
grad=vector([fx,fy,fz]);show("grad=",grad)
show("df/dt=<2*x,2*y,-2*z>.dot+product(<dx/dt,dy/dt,dz/dt>) by chain rule")
show("df/dt=<2*x,2*y,-2*z>.dot+product(<dx/dt,dy/dt,dz/dt>)=0 because grad is normal to level surface")
show("2*x*dx+2*y*dy-2*z*dz=0")
show("4*dx+2*dy-2*dz=0 at point (2,1,1)")
show("4*(x-2)+2*(y-1)-2*(z-1)=0 is the Tangent Plane")
show("4*x-8+2y-2-2*z+2=0 is the Tangent Plane")
show("4*x+2y-2*z=8 is the Tangent Plane")
show(4*(x-2)+2*(y-1)-2*(z-1)==0)
show("")

#2) What is a Normal Vector to the Plane f(x,y,z)=a*x+b*y+c*z
show("#2) What is a Normal Vector to the Plane f(x,y,z)=a*x+b*y+c*z")
var('a,b,c')
f(x,y,z)=a*x+b*y+c*z
fx=diff(f,x);show("fx=",fx)
fy=diff(f,y);show("fy=",fy)
fz=diff(f,z);show("fz=",fz)
grad=vector([fx,fy,fz]);show("grad=",grad)
show("")

#3) What is a Normal Vector to the Surface f(x,y)=x^2+y^2
show("#3) What is a Normal Vector to the Surface f(x,y)=x^2+y^2")
f(x,y)=x^2+y^2
fx=diff(f,x);show("fx=",fx)
fy=diff(f,y);show("fy=",fy)
grad=vector([fx,fy]);show("grad=",grad)
