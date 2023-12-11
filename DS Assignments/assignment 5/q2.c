#include <stdio.h>
#include <stdlib.h>
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
}struct node* minValueNode(struct node* node)
{
    struct node* current = node;
  
    
    while (current && current->left != NULL)
        current = current->left;
  
    return current;
}
struct node* deleteNode(struct node* root, int key)
{
   
    if (root == NULL)
        return root;
  
  
    if (key < root->data)
        root->left = deleteNode(root->left, key);
  
  
    else if (key > root->data)
        root->right = deleteNode(root->right, key);
  
    else {
    
        if (root->left == NULL) {
            struct node* temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL) {
            struct node* temp = root->left;
            free(root);
            return temp;
        }
  
        struct node* temp = minValueNode(root->right);
  
       
        root->data = temp->data;

        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}

 struct node *insertinbst(struct node *(root), int d)
{
    if (root == NULL)
    {
        root = newNode(d);
        return root;
    }
    if (d > root->data)
    {
        root->right = insertinbst(root->right, d);
    }
    else
    {
        root->left = insertinbst(root->left, d);
    }
    return root;
}
int search(struct node* root,int value)
{
    if(root==NULL)
    {
        return -1;
    }
    else if(root->data==value)
    {
        return 1;
    }
    else if(root->data<value)
    {
        return search(root->right,value);
    }
    else if(root->data>value)
    {
        return search(root->left,value);
    }

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
      printf("Enter value to be inserted");
      int value;
      scanf("%d",&value);
      insertinbst(root,value);
      int search_val;
 printf("enter value to be searched");
 scanf("%d",&search_val);
 int x=search(root,search_val);
 if(x==1)
 {
    printf("value present");
 }
 else{
    printf("value absent");
 }
 printf("Inorder after this is");
 printPostorder(root);
 int del_val;
  printf("Enter the value to be deleted");
  scanf("%d",&del_val);
    root = deleteNode(root, del_val);
    printf("Inorder traversal of the modified tree \n");
    printInorder(root);

}