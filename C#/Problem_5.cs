using System;

namespace ProjectEuler
{
    class Problem_5
    {
        static void main(string[] args)
        {
            int i = 20;
            // Keep increasing i until you get to a number that is evenly divisible by all numbers between 11-20
            while(true)
            {
                int answer = i;
                for (int j = 11; j <= 20; j++)
                {
                    // Check for any number between 11-20 which is not a factor of i
                    if (i % j != 0)
                    {
                        answer = 0;
                        break;
                    }
                }
                if (answer > 0)
                {
                    System.Console.WriteLine(answer);
                    break;
                }
                i++;
            }    
        }
    }
}