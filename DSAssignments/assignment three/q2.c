#include <stdio.h>
#include <stdlib.h>
struct node
{
    int content;

    struct node *next;
};
struct node *input()
{
    char ans;
    printf("enter first node content:");
    struct node *start = malloc(sizeof(struct node));
    scanf("%d", &start->content);
    start->next = NULL;
    struct node *current = malloc(sizeof(struct node));
    printf("enter second node content:");
    scanf("%d", &current->content);
    start->next = current;
    int i = 3;
    while (1)
    {

        printf("enter N to terminate");
        scanf("\n%c", &ans);
        if (ans == 'N')
        {
            break;
        }
        else
        {

            printf("enter node %d content\n", i);
            struct node *temp = malloc(sizeof(struct node));
            scanf("%d", &temp->content);
            current->next = temp;
            temp->next = NULL;
            current = current->next;
            i++;
        }
    }
    return start;
}
struct node *merge(struct node *start1, struct node *start2)
{
    struct node *current1 = start1;
    struct node *current2 = start2;
    struct node *current = malloc(sizeof(struct node));
    struct node *temp;
    struct node *head_super;
    if (current1->content <= (current2->content))
    {
        current->content = current1->content;
        current1 = current1->next;
    }
    else
    {
        current->content = current2->content;
        current2 = current2->next;
    }
    head_super = current;

    while (current1 != NULL && current2 != NULL)
    {
        if (current1->content <= (current2->content))
        {
            temp = malloc(sizeof(struct node));
            temp->content = current1->content;
            current->next = temp;
            current = current->next;
            current1 = current1->next;
        }
        else
        {

            temp = malloc(sizeof(struct node));
            temp->content = current2->content;
            current->next = temp;
            current = current->next;
            current2 = current2->next;
        }
    }
    if (current1 == NULL)
    {
        current->next = current2;
    }
    else if (current2 == NULL)
    {
        current->next = current1;
    }

    return head_super;
}
void display(struct node *start)
{
    struct node *current = start;
    while (current != NULL)
    {
        printf("\n%d", current->content);
        current = current->next;
    }
}
void main()
{
    printf("enter the first list\n");
    struct node *start1 = input();
    printf("enter second list");
    struct node *start2 = input();
    printf("Merged list is");
    struct node *new_start = merge(start1, start2);
    display(new_start);
}
