#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable : 4996)

/*
Sofia works as a sales manager in the net of retailers.
Now the company is going to launch several brand - 
new items to their shops.The only trouble is that the name 
for new brands is yet to be choosen.
Sofia is ordered to invent these names.
However, many good words are already used(like Apple, Ikea, Gillet).
So she asked you to write a program which can generate a collection 
of funny words.She then will be able to read the list leisurely 
and pick some for brand names.
*/

const int A = 445; // parameter A
const unsigned long int M = 2097152; // parameter M
const unsigned long int C = 700001; // parameter C

//Linear Congruential Generator
unsigned long int linearCongruentialGenerator(int A, unsigned long int C, unsigned long int M, int xCur)
{
	xCur = (A * xCur + C) % M;
	return xCur;
}


int main(void)
{
	int xCur; //initial value
	int N; //letters in the word
	char consonant[] = "bcdfghjklmnprstvwxz"; //consonant
	char volwels[] = "aeiou"; //volwels
	char stringHolder[100] = {0};
	int stringIntegern[100] = {0};
	// letters at odd(1, 3, 5...) position should be consonant - use consonant[]
	// letters at even(2, 4, 6...) position should be volwels - use vilwels[]
	// examples: suragat, turinoma
	scanf("%d %d\n", &N, &xCur); //scaning first line
	scanf("%[^\n]", &stringHolder); //scaning input string
	//printf("%s\n", stringHolder);

	//iteration for whole string
	int iter = 0, integ = 0;
	//input string become an integer massive
	while (stringHolder[iter] != '\0')
	{
		if (stringHolder[iter] != ' ')
		{
			stringIntegern[integ] = (int)stringHolder[iter] - 48;
			integ++;
		}
		iter++;
	}

	integ = 0;
	while(stringIntegern[integ] != 0)
	{
		char stringHolder[100] = { 0 };
		for(int i = 0; i <= stringIntegern[integ]; i++)
		{
			if (i == stringIntegern[integ])
		        stringHolder[i] = '\0';
			else
			{
				xCur = linearCongruentialGenerator(A, C, M, xCur);
				stringHolder[i] = (i % 2 == 0) ? (consonant[xCur % 19]) : (volwels[xCur % 5]);
			}
		}
		printf("%s\n", stringHolder);
		integ++;
	}
	system("pause");
	return 0;
}
