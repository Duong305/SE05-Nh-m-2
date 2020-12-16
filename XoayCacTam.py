import ezdxf
import math
import xml.dom.minidom
from decimal import *
import more_itertools as mit
def sapxep(a):
    b = []
    for i in a:
        for m in a:
            if i[0]+i[1]+i[2] != m[0]+m[1]+m[2]:
                b.append(list((i,m)))
    c = []
    for i in b:
        i.sort()
        c.append(tuple(i))
    return list(set(c))
doc = xml.dom.minidom.parse("a.xml")
expertise = doc.getElementsByTagName("globalP")
expertise1 = doc.getElementsByTagName("Values")
expertise1.pop(0)
expertise1.remove(expertise1[len(expertise1)-2])
expertise1.remove(expertise1[len(expertise1)-2])
expertise1.remove(expertise1[len(expertise1)-2])
expertise1.remove(expertise1[len(expertise1)-3])

k = ezdxf.new('R2010')
msp = k.modelspace()
a = []    
for i in range(len(expertise)):
    b = expertise[i].getAttribute("x")
    c = expertise[i].getAttribute("y")
    d = expertise[i].getAttribute("z")
    a.append((float(Decimal(b)),float(Decimal(c)),float(Decimal(d))))    
s = []
s1 = []
for i in range(len(a)):
    if i%8 == 0:
        s.append(a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4]+a[i+5]+a[i+6]+a[i+7])
for i,m in zip(s,expertise1):         
    e = m.getAttribute("W")
    e1 = m.getAttribute("D")
    e2 = m.getAttribute("H")
    rx = m.getAttribute("RX")
    ry = m.getAttribute("RY")
    rz = m.getAttribute("RZ")
    s1.append(i+(float(Decimal(e)), float(Decimal(e1)), float(Decimal(e2)), float(Decimal(rx)), float(Decimal(ry)), float(Decimal(rz))))
for i in s1:
    t = list(i)
    for m in range(len(t)-8):
        if m%3 == 0:
            x0 = t[m]
            z = t[m+2]
            t[m] = x0*math.cos(math.radians(t[len(t)-2])) + z*math.sin(math.radians(t[len(t)-2]))
            t[m+2] = z*math.cos(math.radians(t[len(t)-2])) - x0*math.sin(math.radians(t[len(t)-2]))
    for m in range(len(t)-8):
        if m%3 == 0:
            x0 = t[m+1]
            z = t[m+2]
            t[m+1] = x0*math.cos(math.radians(t[len(t)-3])) - z*math.sin(math.radians(t[len(t)-3]))
            t[m+2] = z*math.cos(math.radians(t[len(t)-3])) + x0*math.sin(math.radians(t[len(t)-3]))
    for m in range(len(t)-8):
        if m%3 == 0:
            x0 = t[m]
            z = t[m+1]
            t[m] = x0*math.cos(math.radians(t[len(t)-1])) - z*math.sin(math.radians(t[len(t)-1]))
            t[m+1] = z*math.cos(math.radians(t[len(t)-1])) + x0*math.sin(math.radians(t[len(t)-1]))
    a.clear()
    for m in range(len(t)-8):
        if m%3 == 0:
            a.append((t[m], t[m+1], t[m+2]))
    a1 = sapxep(a)
    for m in a1:
        if math.sqrt((m[0][0]-m[1][0])**2 + (m[0][1]-m[1][1])**2 + (m[0][2]-m[1][2])**2) == t[24]:
            msp.add_line(m[0], m[1])
        if math.sqrt((m[0][0]-m[1][0])**2 + (m[0][1]-m[1][1])**2 + (m[0][2]-m[1][2])**2) == t[25]:
            msp.add_line(m[0], m[1])
        if math.sqrt((m[0][0]-m[1][0])**2 + (m[0][1]-m[1][1])**2 + (m[0][2]-m[1][2])**2) == t[26]:
            msp.add_line(m[0], m[1])
k.saveas('yeah5.dxf')

    



