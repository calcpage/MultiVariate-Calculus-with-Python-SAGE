#MrG 2015.0619 REVIEWF Limits (filk: Numa Numa Calculus)
#1) Let r(t)=t^2+1 represent the rate water is leaking from your bathtub, [r]=gal/min, [t]=min. 
show("#1) Let r(t)=t^2+1 represent the rate water is leaking from your bathtub, [r]=gal/min, [t]=min.")
#1a) Find total amount of water that leaked from t=1min to t=5min using 2 Right Reimann Rectangles
show("#1a) Find total amount of water that leaked from t=1min to t=5min using 2 Right Reimann Rectangles")
r(t)=t^2+1
a=1
b=5
n=2
deltaT=(b-a)/2;show("deltaT=",deltaT)
show("RSUM=",deltaT*r(3)+deltaT*r(5)," gal")
show("")

#1b) Find total amount of water that leaked from t=1min to t=5min using 2 Left Reimann Rectangles
show("#1b) Find total amount of water that leaked from t=1min to t=5min using 2 Left Reimann Rectangles")
show("LSUM=",deltaT*r(1)+deltaT*r(3)," gal")
show("")

#1c) Find total amount of water that leaked from t=1min to t=5min using 2 Reimann Trapezoids
show("#1c) Find total amount of water that leaked from t=1min to t=5min using 2 Reimann Trapezoids")
right=deltaT*r(3)+deltaT*r(5)
left=deltaT*r(1)+deltaT*r(3)
show("TRAP=",(right+left)/2," gal")
show("")

#1d) Find total amount of water that leaked from t=1min to t=5min Exactly!
show("#1d) Find total amount of water that leaked from t=1min to t=5min Exactly!")
show(integral(r(t),t))
show(integral(r(t),t,1,5)," gal")
show(integral(r(t),t,1,5).n()," gal")
