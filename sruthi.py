import math 
def decrypt(s) -> str:
        
        tail = len(s)//2
        head = tail-1 

        while (head>-1):
            rs = s[head]+s[tail]
            head = head -1 
            tail = tail+1
        if head%2 == 0:
            rs = rs+s[tail] 

        return rs   


    


        

print(decrypt("segeko"))

