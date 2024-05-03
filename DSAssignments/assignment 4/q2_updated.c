#include <stdio.h>
int queue[20];
int front=-1;
int rear=-1;
int insert(int job)
{
    if(rear==-1&&front==-1)
    {
        rear=front=0;
        queue[front]=job;
    }
    else if((front==rear+1)||(front==0&&rear==19))
    {
        printf("Queue full");
    }
    else if(front==-1&&rear==-1)
    {
        front=rear=0;
        queue[front]=job;
    }

else{
    rear = 0;
    if (front>0){
        queue[--front] = job;
    }else {
        queue[19] = job;
        front =19;
        printf("%d %d\n",queue[0],queue[front]);
    }
    
}
return 1;
}
int delete()
{
    if(front==-1)
    {
        printf("\nQueue empty!\n");
    }
    else if(rear==19)
    {
         
        printf("Job performed is:\n%d\n",queue[front]);
       front=0;
    }
    else if(front==rear)
    {
        printf("Job performed is:\n%d\n",queue[front]);
       front=-1;
       
        
    }
    else{
        printf("Job performed is:\n%d\n",queue[front]);
        queue[front] = 0;
        front = (front+1)%20;
    }
    int i;
    printf("Status of queue is");
    i=front;
             while((i%20)!=rear)
             {
                 printf("%d\n",queue[i%20]);
                 i++;
             }
             printf("%d",queue[rear]);
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
             insert(job);
             int i;
    printf("Status of queue is");
    i=front;
    
             while((i%20)!=rear)
             {
                 printf("%d\n",queue[i%20]);
                 i++;
             }
             printf("%d\n",queue[rear]);
            }
           
        

        else if(ans==2)
        {
            delete();
            int i;
   
        }
        else
        {
           break;
        }
        
        
    }
    return 0;
}