#MrG 2015.0619 REVIEWC Chain Rule (filk: Lazy Calculus aka Calculus Time)
#1) if f(x)=(x+1)^2, is f'(x)=2*(x+1)?
show("#1) if f(x)=(x+1)^2, is f'(x)=2*(x+1)?")
f(x)=(x+1)^2;show("f(x)=",f(x))
g(x)=f(x).diff();show("f'(x)=",g(x))
show("")

#2) if f(x)=(3*x+1)^2, is f'(x)=2*(3*x+1)?
show("#2) if f(x)=(3*x+1)^2, is f'(x)=2*(3*x+1)?")
f(x)=(3*x+1)^2;show("f(x)=",f(x))
g(x)=f(x).diff();show("f'(x)=",g(x))
show("")

#3) Is this the power rule?
show("#3) Is this the power rule?")
show(diff((x+1)^1))
show(diff((x+1)^2))
show(diff((x+1)^3))
show("")

#4) Is this the power rule?
show("#4) Is this the power rule?")
show(diff((2*x+1)^1))
show(diff((2*x+1)^2))
show(diff((2*x+1)^3))

