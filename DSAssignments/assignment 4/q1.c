#include <stdio.h>
#include <stdlib.h>
int queue[20];
int front=-1;
int rear=-1;
int enqueue(int job)
{
    if(rear==19)
    {
        printf("\nOverflow!\n");
    }
    else
    {
        rear+=1;
        queue[rear]=job;
        }
return 1;
    
    
}
int dequeue()
{
    if(front>=rear)
    {
        printf("\nQueue empty!\n");
    }
    else
    {
         front++;
        printf("Job performed is:\n%d\n",queue[front]);
       
    }
return 11;
    
}
void main()
{
   
    while(1){
         int ans;
        int job;
        printf("Enter 1 for add 2 for remove and anything else for exit\n");
        scanf("%d",&ans);

        if(ans==1)
        {
            printf("Enter job to be performed\n");
            scanf("%d",&job);
             enqueue(job);
            }
        else if(ans==2)
        {
            dequeue();
        }
        else
        {
           break;
        }
        
        
    }
}
