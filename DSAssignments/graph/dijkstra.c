#include <stdio.h>
#include <math.h>

int nV;

//Find minDistance from all distrances from source
int minDistance(int dist[], int fin[])
{
    int min = INFINITY, minIndex;
    for(int i=0; i<nV; i++)
    {
        if(fin[i] == 0 && dist[i]<=min)
        {
            min = dist[i];
            minIndex = i;
        }
    }
    
    return minIndex;
}


void print(int dist[], int source)
{
    for(int i=0; i<nV; i++)
    {
        printf("Minimum way from %d -> %d :\t%d\n", source, i, dist[i]);
    }
}


void dijkstra_sort(int arr[nV][nV], int source)
{
    int dist[nV];
    int max = INFINITY;
    int fin[nV];
    
    //Assigning all Vertices distances as inifinity from souce
    for(int j=0; j<nV; j++)
    {
        dist[j] = max;
        fin[j] = 0;
    }

    dist[source] = 0;

    for(int l=0; l<nV-1; l++)
    {
        int min = minDistance(dist, fin);
        fin[min] = 1;

        for(int j=0; j<nV; j++)
        {
            if(arr[min][j] !=0 && dist[min] != max && (dist[min]+arr[min][j])<dist[j])
            {
                dist[j] =  dist[min]+arr[min][j];
            }
        }
    }
    
    print(dist, source);
    
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
            arr[j][k] = 0;
        }
    }
    
    for(int i=0; i<nE; i++)
    {
        int s, d, w;
        printf("Source:\t");
        scanf("%d", &s);
        printf(" Destination:\t");
        scanf("%d", &d);
        printf(" Weight:\t");
        scanf("%d", &w);
        
        arr[s][d] = w;
        
    }
    
    for(int j=0; j<nV; j++)
    {
        dijkstra_sort(arr, j);
    }
    
    


    return 0;
}
