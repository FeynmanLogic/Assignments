//this is first program.
#include <stdio.h>
#include <stdbool.h>
void push(char);
void pop();
int peek();
bool isEmpty();
bool isFull();
int top=-1;
char stack1[20];
int n=20;
 char stack2[20];

void main()
{
  char c;
  printf("Enter instruction to be performed.");
  scanf("%c",&c);
  while(1)
  {
  
  int m;
  push(c);
  printf("Enter 1 for UNDO and 2 for REDO 3 for exit");
  scanf("%d",&m);
  if(m==1)
  {
pop();
  }
 else if(m==2)
  {
push(c);
  }
  else if(m==3)
  {
    break;
  }
}
}
void push(char c)
{
  if(top==(n-1))
  {
    printf("Overload!");

  }
  else
  {
    top+=1;
    stack1[top]=c;
    printf("element added is:%c",stack1[top]);
  }
}
void pop()
{
  printf("ELement popped is:%c\n",stack1[top]);
  stack2[top]=stack1[top];
  char m=stack2[top];
  push(m);
  stack1[top]='\0';

}