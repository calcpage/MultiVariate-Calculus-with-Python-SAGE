#MrG 2015.0619 REVIEWD s(t), v(t), a(t) (filk: I Will Derive!)
#1) Find v(t) Given s(t)=-16*t^2+100*t+1000, [s]=ft, [t]=sec
show("#1) Find v(t) Given s(t)=-16*t^2+100*t+1000, [s]=ft, [t]=sec")
s(t)=-16*t^2+100*t+1000;show("s(t)=",s(t))
v(t)=diff(s(t),t);show("v(t)=",v(t))
show("")

#2) Find a(t) Given s(t)=-16*t^2+100*t+1000, [s]=ft, [t]=sec
show("#2) Find a(t) Given s(t)=-16*t^2+100*t+1000, [s]=ft, [t]=sec")
a(t)=diff(v(t),t);show("a(t)=",a(t))
show("")

#3) Calculate and interpret s(0), s'(0), s"(0) [s(t) is the height of a baseball thrown upward, t is time of flight]
show("#3) Calculate and interpret s(0), s'(0), s''(0) [s(t) is the height of a baseball thrown upward, t is time of flight]")
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
