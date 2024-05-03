

#include <stdio.h>
#include <string.h>
int solve(char []);
int top=-1;
void main()
{
    char s[100];
 printf("enter your string");
 scanf("%[^\n]%*c",s);
  int m=solve(s);
  if(m==0)
  {
      printf("balanced");
  }
  else{
       printf("not balanced");
  }
}
int solve(char s1[])
{
int i;
int temp=0;
for(i=0;s1[i]!='\0';i++)
{
if(s1[i]=='{'||s1[i]=='('||s1[i]=='[')
{
    temp++;
}
if(s1[i]=='}'||s1[i]==')'||s1[i]==']')
{
   temp--;
}
}
return temp;
}