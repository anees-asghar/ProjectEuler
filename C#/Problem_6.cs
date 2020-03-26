using System;

namespace ProjectEuler
{
    class Problem_6
    {
        static void main(string[] args)
        {
            // Find the difference between the sum of the squares of the first one hundred natural numbers
            //  and the square of the sum.

            int sumOfNumbers = 0;
            int sumOfSquares = 0;

            for(int i = 1; i <= 100; i++)
            {
                sumOfNumbers += i;
                sumOfSquares += Convert.ToInt32(Math.Pow(i, 2));
            }

            // square of sum of natural numbers from 1-100
            int squareOfSum = Convert.ToInt32(Math.Pow(sumOfNumbers, 2));

            System.Console.WriteLine($"The difference is { squareOfSum - sumOfSquares }.");
        }
    }
}