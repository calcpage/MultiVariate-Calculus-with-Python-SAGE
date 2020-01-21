#MrG 2018.0528 UMC04 Second Partial Derivatives & PDEs
show("Second Partial Derivatives & PDEs")
var('y')
#f(x,y)=sin(x)+e^y+x*y;show("f(x,y)=",f(x,y))
#f(x,y)=3*x*y^2-2*y+5*x^2*y^2;show("f(x,y)=",f(x,y))
f(x,y)=sin(y)*e^x;show("f(x,y)=",f(x,y))
show('')
fx(x,y)=diff(f(x,y),x);show("fx(x,y)=",fx(x,y))
fxx(x,y)=diff(diff(f(x,y),x),x);show("fxx(x,y)=",fxx(x,y)) #harmonic functions satisfy Laplace's Heat Distribution PDE fxx(x,y)+fyy(x,y)==0
fxy(x,y)=diff(diff(f(x,y),x),y);show("fxy(x,y)=",fxy(x,y)) #well behaved functions fxy(x,y)==fyx(x,y)
show('')
fy(x,y)=diff(f(x,y),y);show("fy(x,y)=",fy(x,y))
fyy(x,y)=diff(diff(f(x,y),y),y);show("fyy(x,y)=",fyy(x,y)) #harmonic functions satisfy Laplace's Heat Distribution PDE fxx(x,y)+fyy(x,y)==0
fyx(x,y)=diff(diff(f(x,y),y),x);show("fyx(x,y)=",fyx(x,y)) #well behaved functions fxy(x,y)==fyx(x,y)
