#include <stdio.h>
void main()
{
    int i, j, k, count_swap = 0, n, min;
    while (1)
    {
        printf("Enter 1 for selection sort 2 for insertion sort 3 for bubble sort 4 forlinear search 5 for binary search 6 for exit\n");
        scanf("%d", &k);
        if (k == 6)
        {
            break;
        }
        if (k == 1)
        {
            printf("ENter the size of the array\n");
            scanf("%d", &n);
            int arr[n];
            printf("Enter the array");
            for (i = 0; i < n; i++)
            {
                scanf("\n%d", &arr[i]);
            }int compare=0;

            for (i = 0; i < n; i++)
            {
                for (j = i+1; j < n-1; j++)
                {
                    int k=j;
                    compare++;
                    if (arr[j+1] <= arr[j])
                    {
                        k=j+1;
                       
                    }
                    
                }
                
                if(arr[i]>arr[k])
                    {
                        compare++;
                         int temp = arr[i];
                        arr[i] = arr[k];
                        arr[k] = temp;
                        count_swap += 1;
                    }
            }
            for (i = 0; i < n; i++)
            {
                printf("Element at position %d is %d\n", i, arr[i]);
            }
            printf("No. of swaps are:%d\n", count_swap);
            printf("COmparisons are:%d",compare);
        }
        if (k == 3)
        {
            int swap=0;
            printf("Enter the size of the array");
            scanf("%d", &n);
            int a[n];
            printf("enter the array\n");
            for (i = 0; i < n; i++)
            {
                scanf("%d", &a[i]);
            }
            int temp;
            for (i = 0; i < n; i++)
            {
                for (j = i; j < n; j++)
                {
                    if (a[j] < a[i])
                    {
                        temp = a[i];
                        a[i] = a[j];
                        a[j] = temp;
                        swap += 1;
                    }
                }
            }
            printf("array is:");
            for (i = 0; i < n; i++)
            {
                printf("%d ", a[i]);
            }
            printf("No. of swaps are:%d", swap);
        }
        if (k == 4)
        {
            printf("Enter the size of the array");
            scanf("%d", &n);
            int a[n];
            printf("enter the array\n");
            for (i = 0; i < n; i++)
            {
                scanf("%d", &a[i]);
            }
            int temp, traversal = 0;
            printf("Enter element to be searched");
            scanf("%d", &temp);
            for (i = 0; i < n; i++)
            {
                traversal += 1;
                if (a[i] != temp && i == (n - 1))
                {
                    printf("Element not found!");
                    break;
                }
                if (a[i] == temp)
                {
                    printf("Element found at position:%d", i);
                    printf("No.of positions visited;%d", traversal);
                    break;
                }
            }
        }
        if (k == 5)
        {
            printf("Enter the size of the array");
            scanf("%d", &n);
            int a[n];
            printf("enter the array\n");
            for (i = 0; i < n; i++)
            {
                scanf("%d", &a[i]);
            }
            int temp, traversal = 0, front = 0, rear = n - 1, mid;
            printf("Enter element to be searched");
            scanf("%d", &temp);
            while (front != rear && front < rear)
            {
                traversal += 1;
                if ((front + rear) % 2 == 0)
                {
                    mid = (front + rear) / 2;
                }
                else
                {
                    mid = (front + rear + 1) / 2;
                }

                if (a[mid] == temp)
                {
                    printf("Element found at position :%d with traversals:%d", mid, traversal);
                    break;
                }
                if (a[mid] > temp)
                {
                    rear = mid;
                }
                if (a[mid] < temp)
                {
                    front = mid;
                }
            }
            if (a[mid] != temp)
            {
                printf("ELement not found");
            }
        }
        if(k==2)
        {
            printf("ENter the size of the array\n");
            scanf("%d", &n);
            int arr[n];
            printf("Enter the array");
            for (i = 0; i < n; i++)
            {
                scanf("\n%d", &arr[i]);
            }
int temp,swaps=0;
for(i=1;i<n;i++)
{
    temp=arr[i];
    j=i-1;
    while(j>=0&&arr[j]>temp)
    {
arr[j+1]=arr[j];
swaps++;
j--;
    }
    arr[j+1]=temp;
}
printf("The array is: swaps are:%d\n",swaps);
for(i=0;i<n;i++)
{
    printf("%d ",arr[i]);
}
        }
    }
}