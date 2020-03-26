using System;

namespace EulerProject
{
    class Problem_9
    {
        static void main(string[] args)
        {
            // There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

            System.Console.WriteLine(findAbc(1000));

        }

        static int findAbc(int s)
        {
            for (int a = 1; a < s; a++)
            {
                for (int b = 1; b < a; b++)
                {
                    int c = s - a - b;
                    if (c*c == a*a + b*b)
                    {
                        return (a*b*c);
                    }
                }
            }
            return 0;
        }
    }
}