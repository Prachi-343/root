class prachi:
    x=10
    y=20
    def __init__(self):
        print("i am a prachis constructor")
        
    def msg1(self):
        print("i am prachi ",self.x+self.y)
        
class mate(prachi):
    g=30
    f=5
    def __init__(self):
        print("hi i am a mate's constructor")
    def msg4(self):
        print("hi i am a mate",self.g+self.f)
class unknown(mate):
    t=20
    c=5
    def __init__(self):
        print("hi i am a unknown constructor")
    def msg3(self):
        print("hi i am a unknown",self.t+self.c)
    
    
class sid(unknown):
    a=10
    b=5
    def __init__(self):
        print("i am a sids constructor")
        prachi.__init__(self)
        mate.__init__(self)
        unknown.__init__(self)
        
    def msg2(self):
        print("i am a sid ",self.a+self.b)

a=sid()
a.msg1()    
a.msg2()
a.msg3()
a.msg4()
