#MrG 2018.0614 UMC08 Least Squares Regression (Least Squares see NCC09)
#1) Find Line Of Best Fit: (-3,0), (-1,1), (0,2), (2,3) by SAGE
show("#1) Find Line Of Best Fit: (-3,0), (-1,1), (0,2), (2,3) by SAGE")
var('a,b')
l=[[-3,0],[-1,1],[0,2],[2,3]]
f(x)=a*x+b
q=find_fit(l,f,solution_dict=True)
show(q[a])
show(q[b])
show(f(a=q[a],b=q[b]))
show(f(a=q[a],b=q[b],x=7)) #predict f(7)=?
show(points(l,color='blue')+plot(f(a=q[a],b=q[b]),-4,8,color='red'))
show("")

#2) Find Line Of Best Fit: (-3,0), (-1,1), (0,2), (2,3) by Formulae
show("#2) Find Line Of Best Fit: (-3,0), (-1,1), (0,2), (2,3) by Formulae")
x=[-3,-1,0,2];show("x=",x)
y=[0,1,2,3];show("y=",y)
n=len(x)
p=[]
for i in range(n):
    p.append(x[i]*y[i])
show("p=",p)
q=[]
for i in range(n):
    q.append(x[i]*x[i])
show("q=",q)
show("sum(x)=",sum(x))
show("sum(y)=",sum(y))
show("sum(p)=",sum(p))
show("sum(q)=",sum(q))
a=(n*sum(p)-sum(x)*sum(y))/(n*sum(q)-sum(x)^2)
show("a=",a)
b=(sum(y)-a*sum(x))/n
show("b=",b)
