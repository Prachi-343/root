class marks:
    java=0
    python=0
    cpp=0
    avg=0

siddharth=marks()
siddharth.java=99
siddharth.python=97
siddharth.cpp=95
siddharth.avg=float((siddharth.java+siddharth.python+siddharth.cpp)*100/300)

omkar=marks()
omkar.java=98
omkar.python=96
omkar.cpp=94
omkar.avg=float((omkar.java+omkar.python+omkar.cpp)*100/300)

prachi=marks()
prachi.java=88
prachi.python=90
prachi.cpp=91
prachi.avg=float((prachi.java+prachi.python+prachi.cpp)*100/300)

print("siddharth's marks: %.2f "%(siddharth.avg))
print("omkar's marks: %.2f "%(omkar.avg))
print("prachi's marks: %.2f "%(prachi.avg))

