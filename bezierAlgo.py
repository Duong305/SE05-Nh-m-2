'''dữ liệu đầu vào của file bezierAlgo_data.svg: 
<svg width="190" height="160" xmlns="http://www.w3.org/2000/svg">

  <path d="M 10 10 C 20 20, 40 20, 50 10" stroke="black" fill="transparent"/>
  <path d="M 70 10 C 70 20, 110 20, 110 10" stroke="black" fill="transparent"/>
  <path d="M 130 10 C 120 20, 180 20, 170 10" stroke="black" fill="transparent"/>
  <path d="M 10 60 C 20 80, 40 80, 50 60" stroke="black" fill="transparent"/>
  <path d="M 70 60 C 70 80, 110 80, 110 60" stroke="black" fill="transparent"/>
  <path d="M 130 60 C 120 80, 180 80, 170 60" stroke="black" fill="transparent"/>
  <path d="M 10 110 C 20 140, 40 140, 50 110" stroke="black" fill="transparent"/>
  <path d="M 70 110 C 70 140, 110 140, 110 110" stroke="black" fill="transparent"/>
  <path d="M 130 110 C 120 140, 180 140, 170 110" stroke="black" fill="transparent"/>
</svg>
'''
import ezdxf
import more_itertools as mit
import xml.dom.minidom
from math import factorial
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
doc = ezdxf.new('R2010')
msp = doc.modelspace()
ToaDoDiem = []
x = 0
y = 0
count = -1
for i in range(len(d)):
    ToaDoDiem.append([])
    n = int((len(d[i])/2))-1
    for t in mit.numeric_range(0, 1.01, 0.01):
        for m in range(len(d[i])):
            if m%2 == 0:
                count += 1            
                x += ((1-t)**(n-count))*(t**count)*(factorial(n)/(factorial(n-count)*factorial(count)))*int(d[i][m]) 
                y += ((1-t)**(n-count))*(t**count)*(factorial(n)/(factorial(n-count)*factorial(count)))*int(d[i][m+1])
        count = -1
        ToaDoDiem[i].append((x, y))
        x,y = 0,0
for i in ToaDoDiem:
    for m in range(len(i)-1): 
        msp.add_line(i[m], i[m+1], dxfattribs = {'color':1})
doc.saveas('bezierAlgo.dxf')
