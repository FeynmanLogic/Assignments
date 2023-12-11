#include <stdio.h>
#include <stdlib.h>
struct node
{
    int content;
    struct node* next;
};
struct node* input(int n)
{
int i;
struct node* start=(struct node*)malloc(sizeof(struct node));
scanf("%d",&start->content);
struct node* current;
current=malloc(sizeof(struct node));
scanf("\n%d",&current->content);
start->next=current;
current->next=NULL;
current=current->next;
for(i=2;i<n;i++)
{
    current=malloc(sizeof(struct node));
scanf("\n%d",&current->content);
current->next=NULL;
current=current->next;
}
return start;
}
void display( struct node* start,int n)
{
struct node* current=start;
    int i;
    for(i=0;i<n;i++)
    {
        printf("%d",current->content);
        current=current->next;
    }
}
void main()
{
    int n;
    printf("enter the no. of nodes");
    scanf("%d",&n);
    printf("Enter the content");
    struct node* start=input(n);
    printf("Content is");
    display(start,n);
}