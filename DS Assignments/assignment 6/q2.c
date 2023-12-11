#include <stdio.h>
#include <string.h>
struct student
{
    long reg_no;
    char name[100];
    float cgpa;
};
void insertion_sort(struct student s[10])
{
    int i, j;
    struct student temp;
    for (i = 1; i < 10; i++)
    {
        temp = s[i];
        j = i - 1;
        while (j >= 0 && s[j].cgpa < temp.cgpa)
        {
            s[j + 1] = s[j];

            j--;
        }
        s[j + 1] = temp;
    }
    printf("Array is\n");
    for (i = 0; i < 10; i++)
    {
        printf("%s\n", s[i].name);
        printf("%f\n", s[i].cgpa);
        printf("%ld", s[i].reg_no);
    }
}
void lsearch(struct student s[10])
{
    long search;
    int i;
    printf("Enter registration number of a student to be searched");
    scanf("%ld", &search);
    for (i = 0; i < 10; i++)
    {
        if (s[i].reg_no != search && i == 4)
        {
            printf("Student not found");
            break;
        }
        if (s[i].reg_no == search)
        {
            printf("Student is :%d", i + 1);
            break;
        }
    }
}
void bsearch(struct student *base)
{
    struct student *temp = base;
    long search;
    printf("ENter regiwtration number for student to be searched");
    scanf("%ld", &search);
    int front = 0, rear = 9, mid;
    while (front != rear && front < rear)
    {
        if ((front + rear) % 2 == 0)
        {
            mid = (front + rear) / 2;
        }
        else
        {
            mid = (front + rear + 1) / 2;
        }
        temp = temp + mid;
        if (temp->reg_no == search)
        {
            printf("ELement found at position:%d\n", mid + 1);
            printf("Name is:%s\n", temp->name);
            printf("CGPA is:%f", temp->cgpa);
            return;
        }

        if (temp->reg_no > search)
        {
            rear = mid;
        }
        if (temp->reg_no < search)
        {
            front = mid;
        }
        temp = base;
    }
    printf("ELement not found!");
}
struct student *bsort(struct student s[10])
{
    int i, j;
    for (i = 0; i < 10; i++)
    {
        for (j = i; j < 10; j++)
        {
            if (s[i].reg_no > s[j].reg_no)
            {

                struct student temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            }
        }
    }
    printf("Sorted array is:");
    for (i = 0; i < 10; i++)
    {
        printf("Name is:%s\n", s[i].name);
        printf("registration number is:%ld\n", s[i].reg_no);
        printf("CGPA is:%f\n", s[i].cgpa);
    }
    struct student *base = &s[0];
    return base;
}
int main()
{
    long search;
    struct student s[10];
    struct student *base;
    int i, j;
    printf("Enter the details ");
    for (i = 0; i < 10; i++)
    {
        printf("Enter the details of student :%d\n", (i + 1));

        printf("Enter name\n");
        scanf("\n");
        scanf("%[^\n]*c", s[i].name);
        printf("Enter cgpa");
        scanf("%f", &s[i].cgpa);
        printf("Enter reg no.");
        scanf("%ld", &s[i].reg_no);
    }

    char f[100];
    base = bsort(s);
    bsearch(base);
    insertion_sort(s);
    return 0;
}