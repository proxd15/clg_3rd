a = float(input())
b = float(input())
c = float(input())

if a > 0 and b > 0 and c > 0:
   if a + b > c or a + c > b or b + c > a :
     print("Its a triangle")
   else : 
    print("Its not a triangle") 
else:
    print("Not a correct value")