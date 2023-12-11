#include <stdio.h>
#include <stdlib.h>

struct node*{
    int data;
    struct node* left;
    struct node* right;
}

struct node* bst(int value)
{
    struct node* newnode= malloc(sizeof(struct node));
    int c1,c2;
    newnode->data=value;
    newnode->left=NULL;
    newnode->right=NULL;
    if(value==-1)
    {
        return 0;
    }
    printf("Enter value of two childs:");
    scanf("%d %d",&c1,&c2);
    newnode->left=bst(min(c1,c2));
    newnode->right=bst(max(c1,c2));

    return newnode;
}


int main()
{
    int r;
    printf("Enter value: ");
    scanf("%d",&r);
    bst(r);

    return 0;
}