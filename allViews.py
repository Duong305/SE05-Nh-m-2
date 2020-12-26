import ezdxf 
import math
import xml.dom.minidom
from decimal import *
def sapxepX(s):
    s1 = []
    for i in range(len(s)):
        if i%3 == 0:
            s1.append(s[i])
    x = list(set(s1))
    x.sort()
    return x
def sapxepY(s):
    s1 = []
    for i in range(len(s)):
        if i%3 == 1:
            s1.append(s[i])
    y = list(set(s1))
    y.sort()
    return y
def sapxepZ(s):
    s1 = []
    for i in range(len(s)):
        if i%3 == 2:
            s1.append(s[i])
    z = list(set(s1))
    z.sort()
    return z
def sapxep(a):
    b = []
    for i in a:
        for m in a:
            if i != m:                                             
                b.append(list((i,m)))
    c = []
    for i in b:
        i.sort()
        c.append(tuple(i))
    return list(set(c))
doc = xml.dom.minidom.parse("a.xml")
expertise = doc.getElementsByTagName("globalP")
expertise1 = doc.getElementsByTagName("Values")
expertise2 = doc.getElementsByTagName("Part")
expertise2.pop(len(expertise2)-1)
expertise2.pop(len(expertise2)-1)
expertise2.pop(len(expertise2)-1)
expertise2.pop(len(expertise2)-2)
expertise1.pop(0)
expertise1.pop(len(expertise1)-2)
expertise1.pop(len(expertise1)-2)
expertise1.pop(len(expertise1)-2)
expertise1.pop(len(expertise1)-3)
k = ezdxf.new('R2010', setup = True)
msp = k.modelspace()
a = []    
for i in range(len(expertise)):
    x = expertise[i].getAttribute("x")
    y = expertise[i].getAttribute("y")
    z = expertise[i].getAttribute("z")
    a.append((float(Decimal(x)),float(Decimal(y)),float(Decimal(z))))    
ToaDoDiem = []
TenTam = []
KichThuoc = []
for i in range(len(a)):
    if i%8 == 0:
        ToaDoDiem.append(a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4]+a[i+5]+a[i+6]+a[i+7]) #(1,0) + (0,1) = (1,0,0,1) ((0 
for i in expertise1:         
    e = i.getAttribute("W")
    e1 = i.getAttribute("D")
    e2 = i.getAttribute("H")
    KichThuoc.append((float(Decimal(e)), float(Decimal(e1)), float(Decimal(e2))))
for i in expertise2:
    Name = i.getAttribute("name")
    TenTam.append(Name)
for i in range(len(ToaDoDiem)):
    t1 = list(ToaDoDiem[i])
    for m in range(len(t1)):
        if m%3 == 0:
            if max(sapxepX(t1)) < max(sapxepX(ToaDoDiem[2])) and max(sapxepX(t1)) < max(sapxepX(ToaDoDiem[5])) and max(sapxepX(t1)) < max(sapxepX(ToaDoDiem[6])):
                x0 = t1[m]
                t1[m] = x0 - 200
            if min(sapxepX(t1)) > min(sapxepX(ToaDoDiem[2])) and min(sapxepX(t1)) > min(sapxepX(ToaDoDiem[5])) and min(sapxepX(t1)) > min(sapxepX(ToaDoDiem[6])):
                x01 = t1[m]
                t1[m] = x01 + 200
            if min(sapxepY(t1)) > min(sapxepY(ToaDoDiem[2])) and min(sapxepY(t1)) > min(sapxepY(ToaDoDiem[5])) and min(sapxepY(t1)) > min(sapxepY(ToaDoDiem[6])):
                y = t1[m+1]
                if i != 4:
                    t1[m+1] = y + 200
                else:
                    t1[m+1] = y + 120
            if max(sapxepY(t1)) < max(sapxepY(ToaDoDiem[2])) and max(sapxepY(t1)) < max(sapxepY(ToaDoDiem[5])) and max(sapxepY(t1)) < max(sapxepY(ToaDoDiem[6])):
                y1 = t1[m+1]
                t1[m+1] = y1 - 200
    a.clear()
    for m in range(len(t1)):
        if m%3 == 0:
            a.append((t1[m], t1[m+1], t1[m+2]))
    if max(sapxepX(t1)) < max(sapxepX(ToaDoDiem[2])) and max(sapxepX(t1)) < max(sapxepX(ToaDoDiem[5])) and max(sapxepX(t1)) < max(sapxepX(ToaDoDiem[6])):
        msp.add_text(TenTam[i], dxfattribs = {'style': 'LiberationSerif', 'height': 15}).set_pos((a[0][0]-250, a[0][1]-250, (sapxepZ(t1)[0]+sapxepZ(t1)[1])/2), align='CENTER')
    if min(sapxepX(t1)) > min(sapxepX(ToaDoDiem[2])) and min(sapxepX(t1)) > min(sapxepX(ToaDoDiem[5])) and min(sapxepX(t1)) > min(sapxepX(ToaDoDiem[6])):
        msp.add_text(TenTam[i], dxfattribs = {'style': 'LiberationSerif', 'height': 15}).set_pos((a[0][0]+250, a[0][1], (sapxepZ(t1)[0]+sapxepZ(t1)[1])/2), align='CENTER')
    if min(sapxepY(t1)) > min(sapxepY(ToaDoDiem[2])) and min(sapxepY(t1)) > min(sapxepY(ToaDoDiem[5])) and min(sapxepY(t1)) > min(sapxepY(ToaDoDiem[6])):
        if i != 4:
            msp.add_text(TenTam[i], dxfattribs = {'style': 'LiberationSerif', 'height': 15}).set_pos((a[0][0]+110, a[0][1], (sapxepZ(t1)[0]+sapxepZ(t1)[1])/2), align='CENTER')
        else:
            msp.add_text(TenTam[i], dxfattribs = {'style': 'LiberationSerif', 'height': 15}).set_pos((a[0][0]+200, a[0][1], (sapxepZ(t1)[0]+sapxepZ(t1)[1])/2), align='CENTER')
    if max(sapxepY(t1)) < max(sapxepY(ToaDoDiem[2])) and max(sapxepY(t1)) < max(sapxepY(ToaDoDiem[5])) and max(sapxepY(t1)) < max(sapxepY(ToaDoDiem[6])):
        msp.add_text(TenTam[i], dxfattribs = {'style': 'LiberationSerif', 'height': 15}).set_pos((a[0][0]+150, a[0][1]-300, (sapxepZ(t1)[0]+sapxepZ(t1)[1])/2), align='CENTER')
    if i == 2:
        msp.add_text(TenTam[i], dxfattribs = {'style': 'LiberationSerif', 'height': 15}).set_pos(((sapxepX(ToaDoDiem[2])[0]+sapxepX(ToaDoDiem[2])[1])/2, (sapxepY(ToaDoDiem[2])[0]+sapxepY(ToaDoDiem[2])[1])/2, sapxepZ(ToaDoDiem[2])[1]+50), align='CENTER')
    if i == 5:
        msp.add_text(TenTam[i], dxfattribs = {'style': 'LiberationSerif', 'height': 15}).set_pos(((sapxepX(ToaDoDiem[5])[0]+sapxepX(ToaDoDiem[5])[1])/2, (sapxepY(ToaDoDiem[5])[0]+sapxepY(ToaDoDiem[5])[1])/2, sapxepZ(ToaDoDiem[5])[1]+50), align='CENTER')
    if i == 6:
        msp.add_text(TenTam[i], dxfattribs = {'style': 'LiberationSerif', 'height': 15}).set_pos(((sapxepX(ToaDoDiem[6])[0]+sapxepX(ToaDoDiem[6])[1])/2, (sapxepY(ToaDoDiem[6])[0]+sapxepY(ToaDoDiem[6])[1])/2, sapxepZ(ToaDoDiem[6])[1]+50), align='CENTER')
    a1 = sapxep(a)
    for m in a1:
        if math.sqrt((m[0][0]-m[1][0])**2 + (m[0][1]-m[1][1])**2 + (m[0][2]-m[1][2])**2) == KichThuoc[i][0]:
            msp.add_line(m[0], m[1])
        if math.sqrt((m[0][0]-m[1][0])**2 + (m[0][1]-m[1][1])**2 + (m[0][2]-m[1][2])**2) == KichThuoc[i][1]:
            msp.add_line(m[0], m[1])
        if math.sqrt((m[0][0]-m[1][0])**2 + (m[0][1]-m[1][1])**2 + (m[0][2]-m[1][2])**2) == KichThuoc[i][2]:
            msp.add_line(m[0], m[1])           
k.saveas('allView.dxf')

    



