using System;
using System.Collections.Generic;

class SharePriceVolatility
{
    static void Main()
    {
        int itter = Int32.Parse(Console.ReadLine());
        string[] share = new string[itter];
        bool[] nums = new bool[itter];
        for (int it = 0; it < itter; it++)
        {
            
            List<string> lineToFun = ScaneLine();
            share[it] = lineToFun[0];
            lineToFun.RemoveAt(0);
            nums[it] = DoubliFinder(lineToFun.ToArray());
        }
        for (int it = 0; it < itter; it++)
        {
            if (nums[it])
                Console.Write("{0} ", share[it]);
        }
        Console.ReadKey();
    }

    static List<string> ScaneLine()
    {

        string newLine = Console.ReadLine();
        List<string> lineToFun = new List<string>(newLine.Split(' '));

        return lineToFun;
    }

    static bool DoubliFinder(string[] ListGlist)
    {
        double summator = 0.0, dizintegrator = 0.0;
        int[] masssConvert = new int[ListGlist.Length];
        for (int i = 0; i < ListGlist.Length; i++)
        {
            masssConvert[i] = Convert.ToInt32(ListGlist[i]);
            summator += (double)masssConvert[i];
        }
        summator /= ListGlist.Length;

        foreach (int i in masssConvert)
        {
            dizintegrator = dizintegrator + Math.Pow(((double)i - summator), 2.0);
        }
        dizintegrator /= ListGlist.Length;
        dizintegrator = Math.Sqrt(dizintegrator);


        return (dizintegrator / (summator * 0.01)) > 4;
    }
}
