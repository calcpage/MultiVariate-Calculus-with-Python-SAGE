#MrG 2015.0619 REVIEWE a(t), v(t), s(t) (filk: Bohemian Calculus)
#1) Find v(t) Given a(t)=-5, v(0)=10, [a]=ft/sec^2, [t]=sec
show("#1) Find v(t) Given a(t)=-5, v(0)=10, [a]=ft/sec^2, [t]=sec")
a(t)=-5;show("a(t)=",a(t))
v(t)=integral(a(t),t);show("v(t)=",v(t),"+C")
var('C')
show(solve(v(0)+C==10, C))
show("")

#2) Find s(t) Given a(t)=-5, v(0)=10, s(0)=100, [a]=ft/sec^2, [t]=sec
show("#2) Find s(t) Given a(t)=-5, v(0)=10, s(0)=100, [a]=ft/sec^2, [t]=sec")
s(t)=integral(v(t)+10,t);show("s(t)=",s(t),"+C")
show(solve(s(0)+C==100, C))
show("")

#3) Calculate and interpret s(0), s'(0), s"(0) [s(t) is the height of a baseball thrown upward, t is time of flight]
show("#3) Calculate and interpret s(0), s'(0), s''(0) [s(t) is the height of a baseball thrown upward, t is time of flight]")
v(t)=-5*t+10
s(t)=-5/2*t^2+10*t+100
show("s(0)=",s(0))
show("s'(0)=",v(0))
show("s''(0)=",a(0))
show("")

#4) Find the maximum height of the ball's trajectory (aka apex or zenith point)
show("#4) Find the maximum height of the ball's trajectory (aka apex or zenith point)")
show(solve(v(t)==0,t))
show(solve(v(t)==0,t)[0])
show("t=",solve(v(t)==0,t)[0].rhs())
show("t=",solve(v(t)==0,t)[0].rhs().n()," sec")
show("smax=",s(solve(v(t)==0,t)[0].rhs()))
show("smax=",s(solve(v(t)==0,t)[0].rhs()).n()," ft")
