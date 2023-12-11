#include<stdio.h>
#include<stdlib.h>


struct node{
    int data;
    struct node* left;
    struct node* right;
};

struct node* create(int value)
{
    int l,r;
    struct node* newnode=malloc(sizeof(struct node));
    newnode->data=value;
    newnode->left=NULL;
    newnode->right=NULL;
    if(value==-1)
    {
        return 0;
    }
    printf("Enter the value of left child of %d: ",newnode->data);
    scanf("%d",&l);
    newnode->left=create(l);
    printf("Enter value of right child of %d: ",newnode->data);
    scanf("%d",&r);
    newnode->right=create(r);

    return newnode;
}
int main()
{
    struct node* root;
    int rn;
    printf("Enter root node:%d",&rn);
    root=create(rn);
    return 0;
}