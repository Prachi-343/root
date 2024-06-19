# def cheak(gr,no):
#     result=True
#     for i in gr:
#         if(i==no):
#             result=True
#         else:
#             result=False
#     print(result) 
    
# g=[1,2,3]
# n=3
# cheak(g,n)

def check(gr, n):
   for i in gr:
       if n == i:
           return True
   return False
g=[1, 5, 8, 3]
n=9
print(check(g, n))
