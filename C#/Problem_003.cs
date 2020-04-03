using System;

namespace ProjectEuler
{
    class Problem_003
    {
        static void main(string[] args)
        {
            // What is the largest prime factor of the number 600851475143?
            long number = 600851475143;
            int factor = 2;

            while (factor < number)
            {
                if (number % factor == 0)
                {
                    number =  number / factor;
                    factor = 2;
                }
                else
                {
                    factor += 1;
                }
            }
            System.Console.WriteLine($"The largest prime factor of the number 600851475143 is {factor}.");
        }
    }
}
