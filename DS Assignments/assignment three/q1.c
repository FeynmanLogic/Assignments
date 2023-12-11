#include <stdio.h>
#include <stdlib.h>
struct node
{
    int content;
    struct node* next;
};
 struct node* start_eve;
    struct node* start_odd;
    struct node* head_eve;
    struct node* head_odd;
struct node* input(int n)
{
    struct node* start=(struct node*)malloc(sizeof(struct node));
    int i=0;
printf("content in node %d is:",(i+1));
    scanf("%d",&start->content);
start->next=NULL;
struct node* current=(struct node*)malloc(sizeof(struct node));
start->next=current;
printf("content in node %d is:",(i+2));
    scanf("%d",&current->content);
for(i=2;i<n;i++)
{
    printf("content in node %d is:",(i+1));
     struct node* temp=(struct node*)malloc(sizeof(struct node));
    scanf("%d",&temp->content);
    temp->next=NULL;
    current->next = temp;
    current = current->next;

}
current->next=NULL;
return start;
}
void seperate(struct node* start,int n)
{
    int i;
    struct node* current=(start->next)->next;
   struct node* temp_eve;
        struct node* temp_odd;
        start_odd=(struct node*)malloc(sizeof(struct node));
        start_eve=(struct node*)malloc(sizeof(struct node));
        
        start_eve->content=start->content;
        start_odd->content=(start->next)->content;
        head_eve=start_eve;
        head_odd=start_odd;
    for(i=2;i<n;i++)
    {
        
        if(i%2==0)
        {
            temp_eve=(struct node*)malloc(sizeof(struct node));
            temp_eve->content=current->content;
           temp_eve->next=NULL;
           start_eve->next = temp_eve;
           start_eve = start_eve->next;
            
        }
        else
        {
            temp_odd=(struct node*)malloc(sizeof(struct node));
            temp_odd->content=current->content;
                        temp_odd->next=NULL;

            start_odd->next=temp_odd;
            start_odd=start_odd->next;
        }
         current=current->next;
         
    }
   
   temp_eve->next=NULL;
   temp_odd->next=NULL;
}
void display( struct node* start)
{
    struct node* current=start;
    while(current!=NULL)
    {
        printf("\n%d",current->content);
        current=current->next;
    }
}
void main()
{
    int n;
    printf("Enter the  size oflist\n");
    scanf("%d",&n);
    printf("enter the list");
    struct node* start=input(n);
    
    seperate(start,n);
    printf("list having elements of even indexes is:");
    display(head_eve);
    printf("list having elements of odd indexes is:");
    display(head_odd);
}