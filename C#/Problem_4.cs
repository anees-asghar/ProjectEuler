using System;

namespace ProjectEuler
{
    class Problem_4
    {
        static void main(string[] args)
        {
            // Find the largest palindrome made from the product of two 3-digit numbers.
            
            int lpc = 0;

            for (int i = 1; i < 1000; i++)
            {
                for (int j = 1; j < 1000; j++)
                {
                    int k = i * j;
                    string kStr = k.ToString();
                    char[] kArray = kStr.ToCharArray();
                    Array.Reverse(kArray);
                    string kStrInverted = new string( kArray );

                    if (kStr == kStrInverted && k > lpc)
                    {
                        lpc = k;
                    }
                }
            }
            System.Console.WriteLine($"The largest palindrome made from the product of two 3-digit numbers is {lpc}");
        }
    }
}