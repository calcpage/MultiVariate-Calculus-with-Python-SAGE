#MrG 2018.0516 NCC02 3D Vectors!
#5) What is a Scalar Product in 3D?
show("What is a Scalar Product in 3D?")
v=vector([4,1,2]);show("v=",v)
w=vector([2,4,1]);show("w=",w)
show("3*v=",3*v)
show("2*w=",2*w)
show("3*v+2*w",3*v+2*w)
vp=plot(v,color='red')
wp=plot(w,color='green')
tripleVp=plot(3*v,color='black')
doubleWp=plot(2*w,color='orange')
sp=plot(3*v+2*w,color='brown')
show("|v|=",abs(v))
show("|3*v|=",abs(3*v))
show("|w|=",abs(w))
show("|2*w|=",abs(2*w))
#show(tripleVp+doubleWp+sp,aspect_ratio=1)
show("")

#6) What about the dot product?
show("What about the dot product?")
dot=v.dot_product(w)
show("v.dot_product(w)=",dot)
t=arccos(dot/(abs(v)*abs(w)))
show("theta=",t.n()," radians")
show("theta=",(t*180/pi).n()," degrees")
show("")

#7) What about the cross product?
show("What about the cross product?")
cross=v.cross_product(w)
show("v.cross_product(w)=",cross)
t=arcsin(abs(cross)/(abs(v)*abs(w)))
show("theta=",t.n()," radians")
show("theta=",(t*180/pi).n()," degrees")
crossp=plot(cross)
show(vp+wp+crossp,aspect_ratio=1)