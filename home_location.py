import math
##S = raw_input()
##N = map(int,S.split())
##num_nodes = N.pop(0)
##num_edges = N.pop(0)

a,b = map(int,raw_input().split())
x = [0]
y = [0]
for i in range(1,5):
    x1,y1 = (map(int,raw_input().split()))
    x.append(x1)
    y.append(y1)

#print x
#print y
w = 1-a*a
z = 1 - b*b
c = 2*(a*a*x[2]-x[1])
d = 2*(a*a*y[2]-y[1])
e = 2*(b*b*x[4]-x[3])
f = 2*(b*b*y[4]-y[3])
g = a*a*(x[2]*x[2]+y[2]*y[2])-(x[1]*x[1]+y[1]*y[1])
h = b*b*(x[4]*x[4]+y[4]*y[4])-(x[3]*x[3]+y[3]*y[3])

ca = w*(z*d-f*w)*(z*d-f*w)+(z*c-e*w)*(z*c-e*w)
cb = 2*(e*w-z*c)*(g*z-h*w)+c*(z*d-f*w)*(z*d-f*w)+(e*w-z*c)*(z*d-f*w)*d
cc = ((g*z-h*w)*(g*z-h*w))-((z*d-f*w)*(z*d-f*w))*g+(g*z-h*w)*d*(z*d-f*w)
#print ca
#print cb
#print cc

disc = cb*cb-4*ca*cc
if (z*d-f*w) == 0:
    disc = -1
#print disc

if disc < 0:
    print "Impossible!"
elif disc == 0:
    posx = -cb/(2*ca)
    posy = ((g*z - h*w)-posx*(z*c-e*w))/(z*d-f*w)
    if posx == 0:
        posx = 0
    if posy == 0:
        posy = 0
    print ("%.2f" % posx)+" "+("%.2f" % posy)
else:
    posx = min([(-cb+math.sqrt(disc))/(2*ca),(-cb-math.sqrt(disc))/(2*ca)])
    posy = ((g*z - h*w)-posx*(z*c-e*w))/(z*d-f*w)
    if posx == 0:
        posx = 0
    if posy == 0:
        posy = 0
    print ("%.2f" % posx)+" "+("%.2f" % posy)
