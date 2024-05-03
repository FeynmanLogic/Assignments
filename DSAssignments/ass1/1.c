#include <stdio.h>
#include "mystring.h"
void main()
{
    int a, i, x;
    char scompare_concat_len[100], s2[100], *s3[200], *s4[100], s_copied[100], *s6[100], *changestr[200], s7[100], s_concatenated[100], s_reversed[100], s_main[100], s_searched[100];
    char *t;
    printf("enter a string\n");
    scanf("%[^\n]%*c", scompare_concat_len);

    x = len(scompare_concat_len);
    printf("length of the string is:\n%d\n", x);
    printf("enter another string\n");
    scanf("%[^\n]%*c", s2);
    *s3 = concat(scompare_concat_len, s2, s_concatenated);
    printf("concatenated string is:\n%s\n", *s3);
    printf("enter a new string");
    scanf("%[^\n]%*c", s_copied);

    *s4 = copy(s_copied, s7);
    printf("copied string is:\n%s\n", *s4);
    i = compare(scompare_concat_len, s2);
    if (i == 0)
    {

        printf("strings same\n");
    }
    else
    {
        printf("strings not same\n");
    }
    a = count_c(s_copied);
    if (a != 13)
    {
        printf("first occurence of c is:\n%d", a);
    }
    else
    {
        printf("no c in string\n");
    }
    *s6 = reverse(scompare_concat_len, s_reversed);
    printf("reversed string is:%s\n",*s6);
    *changestr = exchange(scompare_concat_len);
    printf("exchanging vowels with * and consonants with #, we get:\n%s\n", scompare_concat_len);
    printf("Enter main string\n");
    scanf("%[^\n]%*c", s_main);
    printf("enter string to be searched\n");
    scanf("%[^\n]%*c", s_searched);
    int m = search(s_main, s_searched);
    if (m == 1)
    {
        printf("String present");
    }
    else
    {
        printf("String absent");
    }
}
