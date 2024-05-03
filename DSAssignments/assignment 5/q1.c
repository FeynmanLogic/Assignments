#include <stdio.h>
#include <stdlib.h>
#include <math.h>
struct node
{
    struct node* left;
    struct node* right;
    int data;
};
struct node* newNode(int value)
{
    struct node* root=(struct node*)malloc(sizeof(struct node));
    root->data=value;
    root->left=NULL;
    root->right=NULL;
    return root;
    
}

int height(struct node *root)
{
    if (root == NULL)
        return 0;
    return fmax(height(root->left), height(root->right)) + 1;
}

void printInorder(struct node* node)
{
    if (node == NULL)
        return;
 
    
    printInorder(node->left);
 
   
    printf("%d ", node->data);
 
    
    printInorder(node->right);
}


void printPreorder(struct node* node)
{
   if(node==NULL)
    return;
    printf("%d ",node->data);
    printPreorder(node->left);
    printPreorder(node->right);
}
void printPostorder(struct node* node)
{
    if (node == NULL)
    return;
    
    printPreorder(node->left);
    printPreorder(node->right);
    printf("%d ",node->data);
}
void main()
{
    struct node* root = newNode(25);
    root->left = newNode(20);
    root->right = newNode(36);
    root->left->left = newNode(10);
    root->left->right = newNode(22);
    root->left->left->left = newNode(5);
    root->left->left->right = newNode(12);
    root->right->left= newNode(30);
    root->right->left->left= newNode(30);
    root->right->right = newNode(40);
     root->right->right->left = newNode(38);
      root->right->right->right = newNode(48);
 

printf("Inorder is\n");
printInorder(root);
printf("Preorder is\n");
printPostorder(root);
printf("Post order is\n");
printPreorder(root);
printf("Height is:%d",height(root));

}