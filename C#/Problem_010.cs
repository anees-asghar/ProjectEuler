using System;

namespace EulerProject
{
    class Problem_10
    {
        static void main(string[] args)
        {
            // Find the sum of all the primes below two million.

            int limit = 2000000;
            long sum = 2;
            for (int j = 3; j < limit; j+=2)
            {
                if (isPrime(j))
                {
                    sum += j;
                }
            }
            System.Console.WriteLine($"The sum of all the primes below two million is {sum}.");
        }

        static bool isPrime(int x)
        {
            for (int i = 2; i < Math.Sqrt(x) + 1; i++)
            {
                if (x % i == 0)
                {
                    return false;
                }
            }
            return true;
        }
    }
}