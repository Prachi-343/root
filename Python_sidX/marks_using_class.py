class marks:
    python=0
    cpp=0
    java=0
    mark=0
    
prachi=marks()

prachi.python=99
prachi.cpp=95
prachi.java=90
prachi.mark= float(((prachi.python + prachi.cpp + prachi.java)*100)/300)

siddharth=marks()

siddharth.python=92
siddharth.cpp=90
siddharth.java=95
siddharth.mark=float(((siddharth.python + siddharth.cpp + siddharth.java)*100)/300)

omkar=marks()

omkar.python=99
omkar.cpp=96
omkar.java=95
omkar.mark= float(((omkar.python + omkar.cpp + omkar.java)*100)/300)

print("prachi's marks %.2f%"%(prachi.mark))

print("Siddharth's marks %.2f%"%(siddharth.mark))

print("omkar's marks %.2f%"%(omkar.mark))
