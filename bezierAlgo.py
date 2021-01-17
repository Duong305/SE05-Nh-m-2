import ezdxf
import more_itertools as mit
import xml.dom.minidom
from math import factorial
def calculateGeneral(n, d):
    x = []
    y = []
    s1 = []
    s2 = []
    for i in range(n+1):
        s1.append(i)
    for m in range(len(d)):
        if m%2 == 0:
            s2.append((int(d[m]), int(d[m+1])))
    for i,m in zip(s1,s2):
        x.append((factorial(n)/(factorial(n-i)*factorial(i)))*m[0])
        y.append((factorial(n)/(factorial(n-i)*factorial(i)))*m[1])
    return x,y
doc1 = xml.dom.minidom.parse("bezierAlgo_data.svg")
expertise = doc1.getElementsByTagName("path")
b = []
for i in expertise:
    a = i.getAttribute("d")
    c = a.split(',')
    b.append(c)
d = []
for i in b:
    m = i[0]
    for n in range(1, len(i)):
        m += i[n]
    a = m.split()
    a.remove("M")
    a.remove("C")
    d.append(a)
print(len(d))
doc = ezdxf.new('R2010')
msp = doc.modelspace()
ToaDoDiem = []
s = 0
s1 = 0
count = -1
for i in range(len(d)):
    ToaDoDiem.append([])
    n = int((len(d[i])/2))-1
    for t in mit.numeric_range(0, 1.01, 0.01):
        for k1,k2 in zip(calculateGeneral(n, d[i])[0], calculateGeneral(n, d[i])[1]):
            count += 1
            s += k1*((1-t)**(n-count))*(t**count)
            s1 += k2*((1-t)**(n-count))*(t**count)
        count = -1
        ToaDoDiem[i].append((s, s1))
        s,s1 = 0,0         
for i in ToaDoDiem:
    for m in range(len(i)-1):
        msp.add_line(i[m], i[m+1], dxfattribs = {'color':1})
doc.saveas('bezier.dxf')
