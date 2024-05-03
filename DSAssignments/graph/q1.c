#include <stdio.h>


int nV;



int MAXSIZE = 8;       
int stack[8];     
int topS = -1;            

int isemptyS() {

   if(topS == -1)
      return 1;
   else
      return 0;
}
   
int isfullS() {

   if(topS == MAXSIZE)
      return 1;
   else
      return 0;
}

int peek() {
   return stack[topS];
}

int pop() {
   int data;
	
   if(!isemptyS()) {
      data = stack[topS];
      topS = topS - 1;   
      return data;
   } else {
      printf("Could not retrieve data, Stack is empty.\n");
   }
}

int push(int data) {

   if(!isfullS()) {
      topS = topS + 1;   
      stack[topS] = data;
   } else {
      printf("Could not insert data, Stack is full.\n");
   }
}





//proto Types
int isFull(int head, int tail);
int isEmpty(int head, int tail);


void dequeue(int *que, int *head, int *tail, int limit)
{
    if(isEmpty(*head, *tail) == 0)
    {
        printf("Queue underflow \n");
    }
    else 
    {
        (*head)++;
        (*head) = (*head)%limit;

        if((*head) == (*tail))
        {
            *head = -1;
            *tail = -1;
        }
    }
}

void inqueue(int *que, int *head, int *tail, int limit, int data)
{
    
    if(isFull(*head, *tail) == 0)
    {
        printf("Queue is  full\n");
    }
    else 
    {

        if(*head == -1)
        {
            (*head)++;
            que[*head] = data;
            (*tail)+=2;
        }
        else 
        {
            que[*tail] = data;
            (*tail)++;
            (*tail) = (*tail)%limit;
        }
    }
   
}


int isFull(int head, int tail)
{
    if(head == tail && head != (-1))
    {
        return 0;
    }
    
    return 1;
}

int isEmpty(int head, int tail)
{
    if(head == -1)
    {
        return 0;
    }
    
    return 1;
}







void printDFS(int arr[nV+1][nV+1])
{
    
    int sourceN;
    int visited[nV+1];
     
    for(int j=0; j<=nV; j++)
    {
        visited[j] = 0;
    }
    
    printf("Enter the source element :\t");
    scanf("%d", &sourceN);
    
    printf("Using DFS search:\n");
    printf("****\n");
    printf("%d\t", sourceN);
    
    visited[sourceN] = 1;
    push(sourceN);
    

    while(!isemptyS())
    {
        for(int j=1; j<=nV; j++)
        {
            if(arr[sourceN][j] == 1 && visited[j]==0)
            {
                printf("%d\t", j);
                visited[j] = 1;
                push(sourceN);
                push(j);
                sourceN = j;
                break;
            }
            
            else if(j==nV && visited[j] == 1)
            {
                sourceN = pop();
            }
        }
        
        
    }
}


void printBFS(int arr[nV+1][nV+1])
{
    int  head = -1;
    int tail = -1;
    int flag = 0;
    
    int sourceN, limit = nV;
    
    int que[limit];
    int visited[nV+1];
    
    for(int j=0; j<=nV; j++)
    {
        visited[j] = 0;
    }
    
    printf("Enter the source element to print all approchable nodes:\t");
    scanf("%d", &sourceN);
    
    printf("Using BFS search:\n");
    printf("****\n");
    printf("%d\t", sourceN);
    
    inqueue(que, &head,  &tail,  limit, sourceN);
    visited[sourceN] = 1;

    while(isEmpty(head, tail) != 0)
    {
        sourceN = que[head];
        dequeue(que, &head, &tail, limit);
        for(int i=1; i<=nV; i++)
        {
            //Means pair and not visited
            if(arr[sourceN][i] == 1 && visited[i] == 0)
            {
                printf("%d\t", i);
                visited[i] = 1;
                inqueue(que, &head,  &tail,  limit, i);
                
            }
        }
    }
    
    printf("\n");
    
    
}

int main()
{
    int nE;
    
    printf("Enter the number of Vertices:\t");
    scanf("%d", &nV);
    
    printf("Enter the number of Edges:\t");
    scanf("%d", &nE);
    
    int arr[nV+1][nV+1];
    
    for(int j=0; j<=nV; j++)
    {
        for(int k=0; k<=nV; k++)
        {
            arr[j][k] = 0;
        }
    }
    
    for(int i=0; i<nE; i++)
    {
        int s, d;
        printf(" Source:\t");
        scanf("%d", &s);
        printf(" Destination:\t");
        scanf("%d", &d);
        
        arr[s][d] = 1;
        
    }
    

    printBFS(arr);
    
    printDFS(arr);
    
    
    
    

    return 0;
}