class marks:
    java=0
    python=0
    cpp=0
    avg=0
    
prachi=marks()
prachi.java=95
prachi.python=96
prachi.cpp=90
prachi.avg=float((prachi.java+prachi.python+prachi.cpp)*100/300)

siddharth=marks()
siddharth.java=90
siddharth.python=95
siddharth.cpp=92
siddharth.avg=float((siddharth.java+siddharth.python+siddharth.cpp)*100/300)


omkar=marks()
omkar.java=98
omkar.python=95
omkar.cpp=96
omkar.avg=float((omkar.java+omkar.python+omkar.cpp)*100/300)

print("prachi's Marks: %.2f "%(prachi.avg))
print("siddharth's Marks: %.2f "%(siddharth.avg))
print("omkar's Marks: %.2f "%(omkar.avg))

