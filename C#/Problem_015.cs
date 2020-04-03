using System;
using System.Collections.Generic;
using System.Numerics;

namespace EulerProject
{
    class Problem_015
    {
        static void main(string[] args)
        {
            // Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
            // there are exactly 6 routes to the bottom right corner.
            // How many such routes are there through a 20×20 grid?

            // As we have to move east and south 20 times each, we can calculate how many possible 40 step combinations of 20-Es (east) and 20-Ss (south)
            // are there. So, we can use the formula to find combinations, 40 choose 20, which is 40! / ((40-20)!*20!)
            BigInteger answer = Factorial(40) / (Factorial(20)*Factorial(20));
            System.Console.WriteLine($"There are {answer} possible routes.");
        }
        static BigInteger Factorial(int x)
        {
            BigInteger fact = x;
            for(int i=1; i < x; i++)
            {
                fact *= i;
            }
            return fact;
        }
    }
}