#include <stdio.h>
#include <stdlib.h>
int queue1[20];
int front=-1;
int rear=-1;
int queue2[20];
int front2=-1;
int rear2=-1;
int enqueue(int job)
{
    if(rear==19)
    {
        printf("\nOverflow!\n");
    }
    else if(front==-1&&rear==-1)
    {
        rear=front=0;
        queue1[rear]=job;
        }
        else{
            rear+=1;
            queue1[rear]=job;
        }
return 1;
    
    
}
int dequeue()
{
    if(front>rear)
    {
        printf("\nQueue empty!\n");
    }
    else if(front==-1&&rear==-1)
    {
         printf("\nQueue empty!\n");
    }
    else if(front==rear)
    {
        if(rear2==front2&&front2==-1){
            rear2=front2=0;
        queue2[rear2]=queue1[front];
        front=rear=-1;

    }
    else if(rear2==19){
        printf("Stack Overflow!");
    }
    else{
        rear2+=1;
        queue2[rear2]=queue1[front];
        front++;
    }}
    else
    {
                if(rear2==19)
    {
        printf("\nOverflow!\n");
    }
    else if(front2==-1&&rear2==-1)
    {
        rear2=front2=0;
        queue2[rear2]=queue1[front];
        front++;
        }
        else{
            rear+=1;
            queue1[rear]=queue1[front];
            front++;
        }
        
       
    }
    int i;
    printf("Status of queue is");
             for(i=front2;i<=rear2;i++)
             {
                 printf("%d\n",queue2[i]);
             }
return 11;
    
}
int pop()
{
    if(front2>=rear2)
    {
        printf("\nQueue empty!\n");
    }
    else
    {
         
        printf("Job performed is:\n%d\n",queue2[front2]);
       front2++;
    }
    int i;
    printf("Status of queue is");
             for(i=front2;i<=rear2;i++)
             {
                 printf("%d\n",queue2[i]);
             }
return 11;
    
}
int main()
{
   int i;
    while(1){
         int ans;
        int job;
        printf("Enter 1 for push 2 for pop and anything else for exit\n");
        scanf("%d",&ans);

        if(ans==1)
        {
            printf("Enter job to be performed\n");
            scanf("%d",&job);
             enqueue(job);
             dequeue();
             
            }
        else if(ans==2)
        {
            pop();
            
        }
        else
        {
           break;
        }
        
        
    }
    return 0;
}
