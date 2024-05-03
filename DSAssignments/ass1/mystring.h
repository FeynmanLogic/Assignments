int len(char s[])
{
    int count = 0, i = 0;
    while (s[i] != '\0')
    {
        i++;
    }
    return i;
}
char *concat(char s1[], char s2[], char s3[])
{
    int i;

    for (i = 0; i < 200; i++)
    {
        if (i < len(s1))
        {
            s3[i] = s1[i];
        }
        else
        {
            s3[i] = s2[(i - len(s1))];
        }
    }
    return s3;
}
char *copy(char s1[], char sl[])
{

    int i;
    for (i = 0; i < len(s1); i++)
    {
        sl[i] = s1[i];
    }
    return sl;
}
int compare(char s1[], char s2[])
{
    int i;
   while(1)
   {    
        if (s1[i] == s2[i])
        {
            return 0;
            i++;
        }
        else if(s1[i]<s2[i])
        {
            return -1;
        }
          else if(s1[i]>s2[i])
          {
            return 1;
          }
    }
}
int count_c(char s3[])
{
    int i;
    for (i = 0; s3[i] != '\0'; i++)
    {
        if (s3[i] == 'c')
        {
            return i;
            break;
        }
        else
        {
            return 13;
        }
    }
}
char *reverse(char s[], char st[])
{

    int i = 0, x;
    while (s[i] != '\0')
    {
        i++;
    }

    x = i;
    i = 0;

    st[x] = '\0';
    while (s[i] != '\0')
    {
        st[x - i - 1] = s[i];
        i++;
    }

    return st;
}
char *exchange(char s[])
{
    int i;
    for (i = 0; s[i] != '\0'; i++)
    {
        if (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U' || s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
        {
            s[i] = '*';
        }
        else
        {
            s[i] = '#';
        }
    }
    return s;
}
int search(char s1[], char s2[])
{
    int i, j, k, count = 0,fl;
    for (i = 0; i < (len(s1)-len(s2))+1; i++)
    {
         fl=1;
        for (j = 0; j < len(s2); j++)
        {
            if (s1[i + j] != s2[j])
            {
                fl=0;
                break;
            }
            else
            {
                fl=1;
               
            }
        }
        if(fl){
            return 1;
        }
       
    }
   return 0;
}