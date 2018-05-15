using System;
using System.Collections.Generic;

class InsertionSort
{
    static void Main()
    {
        Console.WriteLine(String.Join(" ", GoGo()));
    }
    static int[] Reader(int N)
    {
        string[] arrayString = Console.ReadLine().Split();
        int[] arrayItself = new int[N];
        for (int i = 0; i < N; i++)
            arrayItself[i] = Int16.Parse(arrayString[i]);
        return arrayItself;
    }
    static string[] GoGo()
    {
        int N = Int16.Parse(Console.ReadLine()); 
        int[] arraY = Reader(N);
        int[] arrayInt = new int[N - 1];
        string[] arrayS = new string[N - 1];
        int iter = 1;
        int index = 0;
        int iteraholder = 0;
        int[] answerer = new int[N - 1];
        arrayInt = ArrayShifter(arraY, iter, N, answerer, index, iteraholder);
        for (int i = 0; i < N-1; i++)
            arrayS[i] = arrayInt[i].ToString();
        return arrayS;
    }
    static int[] ArrayShifter(int[] arrayBase, int iter, int N, int[] answerer, int index, int iteraholder)
    {
        if (index == (N - 1))
        {
            return answerer;
        }
        else if (arrayBase[iter - 1] > arrayBase[iter])
        {
            int T = arrayBase[iter - 1];
            arrayBase[iter - 1] = arrayBase[iter];
            arrayBase[iter] = T;
            answerer[index]++;
            if (iter > 1)
            {
                iter--;
            }
            return ArrayShifter(arrayBase, iter, N, answerer, index, iteraholder);
        }
        else
        {
            if (iteraholder < iter)
            {
                iteraholder = iter;
                index++;
            }
            if (iter < (N - 1))
            {
                iter++;
            }
            return ArrayShifter(arrayBase, iter, N, answerer, index, iteraholder);
        } 
    }
}
