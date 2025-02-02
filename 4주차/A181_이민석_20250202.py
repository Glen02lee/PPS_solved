#PPS "A181"
A = int(input()) 
B = int(input())

B1 = B % 10      
B10 = (B // 10) % 10 
B100 = B // 100    

print(A * B1)     
print(A * B10)     
print(A * B100)    
print(A * B)     
