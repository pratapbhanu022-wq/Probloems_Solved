def prime_range(start,end):
    print(f"Prime number between {start} and {end} are :")
    for num in range(start,end+1):
        if num>1:
            is_prime=True
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    is_prime=False
                    break
            if is_prime:
                print(num,end=' ')
    print()
m=int(input("Start range"))
n=int(input("end range"))
prime_range(m,n)