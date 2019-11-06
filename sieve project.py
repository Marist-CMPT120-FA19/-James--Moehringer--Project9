def sieve(n):
    m = []
    for i in range(2, n+1):
        if i not in m:
            print (i)
            for j in range(i*i, n+1, i):
                m.append(j)
                 
def main():
    print("This program outputs the prime numbers up to a number n")
    n=int(input("please enter a number n: "))
    return(sieve(n))
main()
