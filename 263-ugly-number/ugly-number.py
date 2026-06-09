class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 :
            return False
        primes = {2,3,5,7,11,13,17,19,23,29,31}
        # n =  abs(n)
        def isPrime(x):
            if x <= 31:
                return x in primes
            for i in range(2,int(math.ceil(x**(0.5)))):
                if x % i == 0:
                    return False
            return True
        acc_primes =  {2,3,5}
        # print(n**(0.5),n)
        print(int(math.ceil(n**(1/2))))
        for x in range(1,int(math.ceil(n**(0.5)))):
            # print(n,x , n%x)
            if n % x == 0:
                f1 = x
                f2 = n / x
                # print(f1,f2)
                if f1 not in acc_primes and isPrime(f1):          
                    return False
                if f2 not in acc_primes and isPrime(f2):
                    return False
        return True