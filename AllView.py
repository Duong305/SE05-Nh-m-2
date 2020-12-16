import ezdxf
import math
import xml.dom.minidom
from decimal import *
doc = xml.dom.minidom.parse("a.xml")
expertise = doc.getElementsByTagName("globalP")
a = []    
for i in range(len(expertise)):
    b = expertise[i].getAttribute("x")
    c = expertise[i].getAttribute("y")
    d = expertise[i].getAttribute("z")
    a.append((float(Decimal(b)),float(Decimal(c)),float(Decimal(d))))
s = []
for i in range(len(a)):
    if i%8 == 0:
        s.append(a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4]+a[i+5]+a[i+6]+a[i+7])
t = list(s[0])
for i in range(len(t)):
    if i%3 == 0:
        x0 = t[i]
        t[i] = x0 - 200
a.clear()
for i in range(len(t)):
    if i%3 == 0:
        a.append((t[i], t[i+1], t[i+2]))
k = ezdxf.new('R2010', setup = True)
msp = k.modelspace()
msp.add_line(a[0], a[1])
msp.add_line(a[1], a[2])
msp.add_line(a[2], a[3])
msp.add_line(a[3], a[0])
msp.add_line(a[4], a[5])
msp.add_line(a[5], a[6])
msp.add_line(a[6], a[7])
msp.add_line(a[7], a[4])
msp.add_line(a[2], a[6])
msp.add_line(a[7], a[3])
msp.add_line(a[1], a[5])
msp.add_line(a[4], a[0])
msp.add_text("1-1 Left Board",
             dxfattribs={
                 'style': 'LiberationSerif',
                 'height': 15}
             ).set_pos((a[0][0]-250, a[0][1]-250, 425), align='CENTER')
t1 = list(s[1])
for i in range(len(t1)):
    if i%3 == 0:
        x0 = t1[i]
        t1[i] = x0 + 200
a.clear()
for i in range(len(t1)):
    if i%3 == 0:
        a.append((t1[i], t1[i+1], t1[i+2]))
msp.add_line(a[0], a[1])
msp.add_line(a[1], a[2])
msp.add_line(a[2], a[3])
msp.add_line(a[3], a[0])
msp.add_line(a[4], a[5])
msp.add_line(a[5], a[6])
msp.add_line(a[6], a[7])
msp.add_line(a[7], a[4])
msp.add_line(a[2], a[6])
msp.add_line(a[7], a[3])
msp.add_line(a[1], a[5])
msp.add_line(a[4], a[0])
msp.add_text("1-2 Right Panel",
             dxfattribs={
                 'style': 'LiberationSerif',
                 'height': 15}
             ).set_pos((a[0][0]+350, a[0][1], 425), align='CENTER')
t2 = list(s[2])
a.clear()
for i in range(len(t2)):
    if i%3 == 0:
        a.append((t2[i], t2[i+1], t2[i+2]))
msp.add_line(a[0], a[1])
msp.add_line(a[1], a[2])
msp.add_line(a[2], a[3])
msp.add_line(a[3], a[0])
msp.add_line(a[4], a[5])
msp.add_line(a[5], a[6])
msp.add_line(a[6], a[7])
msp.add_line(a[7], a[4])
msp.add_line(a[2], a[6])
msp.add_line(a[7], a[3])
msp.add_line(a[1], a[5])
msp.add_line(a[4], a[0])
msp.add_text("1-3 Floor",
             dxfattribs={
                 'style': 'LiberationSerif',
                 'height': 15}
             ).set_pos((a[0][0]+100, a[0][1]-225, 130), align='CENTER')
t3 = list(s[3])
for i in range(len(t3)):
    if i%3 == 1:
        z = t3[i]
        t3[i] = z + 200
a.clear()
for i in range(len(t3)):
    if i%3 == 0:
        a.append((t3[i], t3[i+1], t3[i+2]))
msp.add_line(a[0], a[1])
msp.add_line(a[1], a[2])
msp.add_line(a[2], a[3])
msp.add_line(a[3], a[0])
msp.add_line(a[4], a[5])
msp.add_line(a[5], a[6])
msp.add_line(a[6], a[7])
msp.add_line(a[7], a[4])
msp.add_line(a[2], a[6])
msp.add_line(a[7], a[3])
msp.add_line(a[1], a[5])
msp.add_line(a[4], a[0])
msp.add_text("1-4 Thin back plate",
             dxfattribs={
                 'style': 'LiberationSerif',
                 'height': 15}
             ).set_pos((a[0][0]+110, a[0][1], 431.5), align='CENTER')
t4 = list(s[4])
for i in range(len(t4)):
    if i%3 == 1:
        x0 = t4[i]
        t4[i] = x0 + 200
a.clear()
for i in range(len(t4)):
    if i%3 == 0:
        a.append((t4[i], t4[i+1], t4[i+2]))
msp.add_line(a[0], a[1])
msp.add_line(a[1], a[2])
msp.add_line(a[2], a[3])
msp.add_line(a[3], a[0])
msp.add_line(a[4], a[5])
msp.add_line(a[5], a[6])
msp.add_line(a[6], a[7])
msp.add_line(a[7], a[4])
msp.add_line(a[2], a[6])
msp.add_line(a[7], a[3])
msp.add_line(a[1], a[5])
msp.add_line(a[4], a[0])
msp.add_text("1-5 Back Pull Bar",
             dxfattribs={
                 'style': 'LiberationSerif',
                 'height': 15}
             ).set_pos((a[0][0]+200, a[0][1], 690), align='CENTER')
t5 = list(s[5])
for i in range(len(t5)):
    if i%3 == 1:
        x0 = t5[i]
        t5[i] = x0 + 100
a.clear()
for i in range(len(t5)):
    if i%3 == 0:
        a.append((t5[i], t5[i+1], t5[i+2]))
msp.add_line(a[0], a[1])
msp.add_line(a[1], a[2])
msp.add_line(a[2], a[3])
msp.add_line(a[3], a[0])
msp.add_line(a[4], a[5])
msp.add_line(a[5], a[6])
msp.add_line(a[6], a[7])
msp.add_line(a[7], a[4])
msp.add_line(a[2], a[6])
msp.add_line(a[7], a[3])
msp.add_line(a[1], a[5])
msp.add_line(a[4], a[0])
msp.add_text("1-7 Cover board-Horizontal dress",
             dxfattribs={
                 'style': 'LiberationSerif',
                 'height': 15}
             ).set_pos((a[0][0]+200, a[0][1], 790), align='CENTER')

t6 = list(s[6])
a.clear()
for i in range(len(t6)):
    if i%3 == 0:
        a.append((t6[i], t6[i+1], t6[i+2]))
msp.add_line(a[0], a[1])
msp.add_line(a[1], a[2])
msp.add_line(a[2], a[3])
msp.add_line(a[3], a[0])
msp.add_line(a[4], a[5])
msp.add_line(a[5], a[6])
msp.add_line(a[6], a[7])
msp.add_line(a[7], a[4])
msp.add_line(a[2], a[6])
msp.add_line(a[7], a[3])
msp.add_line(a[1], a[5])
msp.add_line(a[4], a[0])
msp.add_text("1-9 Active Layer Board",
             dxfattribs={
                 'style': 'LiberationSerif',
                 'height': 15}
             ).set_pos((a[0][0]+200, a[0][1]-350, 500), align='CENTER')

t7 = list(s[7])
for i in range(len(t7)):
    if i%3 == 1:
        x0 = t7[i]
        t7[i] = x0 - 200
a.clear()
for i in range(len(t7)):
    if i%3 == 0:
        a.append((t7[i], t7[i+1], t7[i+2]))
msp.add_line(a[0], a[1])
msp.add_line(a[1], a[2])
msp.add_line(a[2], a[3])
msp.add_line(a[3], a[0])
msp.add_line(a[4], a[5])
msp.add_line(a[5], a[6])
msp.add_line(a[6], a[7])
msp.add_line(a[7], a[4])
msp.add_line(a[2], a[6])
msp.add_line(a[7], a[3])
msp.add_line(a[1], a[5])
msp.add_line(a[4], a[0])
msp.add_text("1-10 Cover Doors",
             dxfattribs={
                 'style': 'LiberationSerif',
                 'height': 15}
             ).set_pos((a[0][0]+150, a[0][1]-300, 790), align='CENTER')

k.saveas('allviews.dxf')
