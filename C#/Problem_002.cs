using System;

namespace ProjectEuler
{
    class Problem_002
    {
        static void main(string[] args)
        {
            // By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
            // find the sum of the even-valued terms.
            
            int x = 0;
            int y = 1;
            int sum = 0;
            
            while (x + y < 4000000)
            {
                int z = x + y;
                x = y;
                y = z;
                if (z % 2 == 0)
                {
                    sum += z;
                }
            }

            Console.WriteLine($"The sum is {sum}.");
        }
    }
}
