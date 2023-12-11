#include <stdio.h>
#include<math.h>

int max = INFINITY;

int nV;



//This function is used to point all the nodes to the last inserted node
//Hence if two nodes are already inserted then they both will point to the same node which is last inserted node 
//And hence we will not add any edge there
int check(int i, int inTree[])
{
    while(inTree[i] != i)
    {
        i = inTree[i];
    }
    return i;
}

//this union function connect prev last node to new last node 
// void union1(int i, int j, int inTree[]){
//     int a = find(i, inTree);
//     int b = find(j, inTree);
    
//     inTree[a] = b;
// }
void union1(int i, int j, int inTree[])
{
	int a = check(i, inTree);
	int b = check(j, inTree);
	inTree[a] = b;
}


void print_krushkal(int arr[nV][nV])
{
    
    int totalCost = 0;
    int inTree[nV];
    
    for(int i=0; i<nV; i++)
    {
        inTree[i] = i;
    }
    
    
    for(int i=0; i<nV-1; i++)
    {
        int min = max, a = -1, b = -1;
        for(int j=0; j<nV; j++)
        {
            for(int k=0; k<nV; k++)
            {
                if(check(j, inTree) != check(k, inTree) && arr[j][k]<min)
                {
                    min = arr[j][k];
                    a = j;
                    b = k;
                }
            }
        }
        
        
        union1(a, b, inTree);
        printf("Edge (%d, %d) , cost : %d\n", a, b, min);
        totalCost += min;
        
    }
    
    printf("Total cost is %d", totalCost);
}



void print_prims(int arr[nV][nV])
{
    
    int visited[nV];
    
    //First make all nodes not visited
    for(int i=0; i<nV; i++)
    {
        visited[i] = 0;
    }
    
    visited[0] = 1;
    
    for(int l=0; l<nV-1; l++)
    {
        int min = max, ind = -1, source = -1;
        //Here i is Source node and all visited nodes will become souce node 
        for(int i=0; i<nV; i++)
        {
            if(visited[i] == 1)
            {
                //Here j is the destination node
                for(int j=0; j<nV; j++)
                {
                    if(arr[i][j] != max && arr[i][j]<min &&  visited[j] == 0 )
                    {
                        min = arr[i][j];
                        ind = j;
                        source = i;
                    }
                }
            }
        }
        
        visited[ind] = 1;
        printf("Edge (%d, %d) , cost is : %d\n", source, ind, min);
    }
    

    
    
    
}



int main()
{
    int nE;
    
    printf("Enter the number of Vertices:\t");
    scanf("%d", &nV);
    
    printf("Enter the number of Edges:\t");
    scanf("%d", &nE);
    
    int arr[nV][nV];
    
    for(int j=0; j<nV; j++)
    {
        for(int k=0; k<nV; k++)
        {
            arr[j][k] = max;
        }
    }
    
    for(int i=0; i<nE; i++)
    {
        int s, d, w;
        printf(" Source:\t");
        scanf("%d", &s);
        printf(" Destination:\t");
        scanf("%d", &d);
        printf(" Weight:\t");
        scanf("%d", &w);
        
        arr[s][d] = w;
        
    }
    

    printf("\n****\n");
    printf("Using Kruskal's Algorithm spanning tree is : \n");
    print_krushkal(arr);
    
    printf("\n****\n");
    printf("Using Prim's Algorithm spanning tree is : \n");
    print_prims(arr);


    return 0;
}