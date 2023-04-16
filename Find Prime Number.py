# Find given number is Prime Number or not
def IsPrime(num):

    isPrime = True
    if num <= 1:
        isPrime = False
    elif num == 2:
        isPrime = True
    elif num%2 == 0:
        isPrime = False
    else:
        # Find Square root
        sqNum = int(num**(1/2))
        # skiping 4, 6, 8.. etc as we have done for 2
        for i in range(3, sqNum + 1, 2):
            if num % i == 0:
                isPrime = False
                break

    return isPrime



# User Input
gnNum = input("Enter your number:")
gnNum = int(gnNum)
# Find the previous prime
for i in range(gnNum,0,-1):
    if IsPrime(i):
        print(f"Previous prime number is {i}")
        break

# Find the next prime
nextPrime = gnNum + 1
while (IsPrime(nextPrime) == False):
    nextPrime += 1
print(f"Next prime number is {nextPrime}")
