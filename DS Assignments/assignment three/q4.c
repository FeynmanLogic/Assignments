#include <stdio.h>
#include <stdlib.h>
struct node{
    int power;
    int coefficient;
    struct node* next;
};
struct node* input()
{
    char ans;
    printf("enter first node content:");
    struct node* start=malloc(sizeof(struct node));
    scanf("%d %d",&start->coefficient,&start->power);
    start->next=NULL;
    struct node* current=malloc(sizeof(struct node));
    printf("enter second node content:");
    scanf("%d %d",&current->coefficient,&current->power);
    start->next=current;
    int  i=3;
    while(1)
    {
     
printf("enter N to terminate");
scanf("\n%c",&ans);
if(ans=='N')
{
    break;
}
else{
     
printf("enter node %d content\n",i);
struct node* temp=malloc(sizeof(struct node));
scanf("%d %d",&temp->coefficient,&temp->power);
current->next=temp;
temp->next=NULL;
current=current->next;
i++;
}
    }
    return start;
}
void  evaluate_and_display(struct node* start,int x)
{
    struct node* current=start;
  long  S=0;
int i,f=1,temp;
while(current!=NULL)
{
    temp=x;
    for(i=1;i<=current->power;i++)
    {
    temp=temp*f;

    }
    S=S+(current->coefficient)*temp;
    f=1;
    current=current->next;
}
printf("Evaluated expression is:%d",S);
}
void main()
{
    int x;
    printf("Enter the  list");
struct node* start=input();
printf("enter the value of x");
scanf("%d",&x);
evaluate_and_display(start,x);

}