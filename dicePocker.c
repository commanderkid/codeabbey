#include <stdio.h>
#include <malloc.h>

int readerOffunction(void);

void main(void)
{
    int *answers;
    int numberOfexersise;
    scanf("%d", &numberOfexersise);
    answers = (int*)malloc(numberOfexersise * sizeof(int));
    for(int i = 0; i < numberOfexersise; i++)
    {
        answers[i] = readerOffunction(); 
    }
    for(int i = 0; i < numberOfexersise; i++)
    {
        if(answers[i] == 1)
            printf("small-straight");
        else if(answers[i] == 2)
            printf("pair");
        else if(answers[i] == 3)
            printf("three");
        else if(answers[i] == 4)
            printf("four");
        else if(answers[i] == 5)
            printf("yacht");
        else if(answers[i] == 22)
            printf("two-pairs");
        else if(answers[i] == 23)
            printf("full-house");
        else if(answers[i] == 11)
            printf("big-straight"); 
        else
            printf("none");
        
        if (i != numberOfexersise - 1)
            printf(" ");
    }
}

int readerOffunction(void)
{
    int ms[] = {0, 0, 0, 0, 0};
    int cH[] = {0, 0, 0, 0, 0, 0};
    scanf("%d %d %d %d %d", &ms[0], &ms[1], &ms[2], &ms[3], &ms[4]);
    
    for(int i = 0; i < 5; i++)
    {
        if (cH[ms[i]-1] != 0)
        {
            continue;
        }
        for(int j = i; j < 5; j++)
        {
            if(ms[i] == ms[j])
                cH[ms[i]-1] += 1;
        }
    }
    
    int holderReturn = 0;
    for (int i = 0; i < 6; i++)
    {
        if (cH[i] == 5)
            return 5;
        else if (cH[i] == 4)
            return 4;
        else if (cH[i] == 2 || cH[i] == 3)
           holderReturn += cH[i];
    }
    
    if(holderReturn == 4)
        return 22;
    else if (holderReturn == 5)
        return 23;
    else if (holderReturn == 2)
        return 2;   
    else if (holderReturn == 3)
        return 3;
    else if (holderReturn == 0)
    {
        for(int i = 0; i < 5; i ++)
        {
            if(ms[i] == 1)
                return 1;
        }
        return 11;
    }
    else
        return 0;
}
