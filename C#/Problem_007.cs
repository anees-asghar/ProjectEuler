using System;

namespace EulerProject
{
    class Problem_007
    {
        static void main(string[] args)
        {
            // What is the 10 001st prime number?
            
            int counter = 0; // Prime count
            int i = 0; // iterator
            while(counter < 10001)
            {
                i++;
                if (isPrime(i))
                {
                    counter++;
                }
            }
            System.Console.WriteLine($"The 10001th prime number is {i}.");
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