int len(char s[])
{
    int count = 0, i = 0;
    while (s[i] != '\0')
    {
        i++;
    }
    return i;
}
char *concat(char s1[], char s2[])
{
    int i;
    char s3[200];
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
char *copy(char s1[])
{
    char s2[100];
    int i;
    for (i = 0; i < len(s1); i++)
    {
        s2[i] = s1[i];
    }
    return s2;
}
int compare(char s1[], char s2[])
{
    int i;
    for (i = 0; s1[i] != '\0'; i++)
    {
        if (s1[i] != s2[i])
        {
            return 1;
        }
        else
        {
            return 0;
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
    char *reverse(char s[])
    {
char s2[200];
        int i=0,x;
        while(s[i]!='\0')
{
    i++;
}

        x=i;
        i=0;
        
        s2[x]='\0';
       while(s2[i]!='\0')
       {
 s2[x-i-1]=s[i];
   i++;
       }
        
    return s2;

}
char *exchange(char s[])
{
    int i;
    for(i=0;s[i]!='\0';i++)
    {
        if(s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U'||s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u')
        {
            s[i]='*';
        }
        else
        {
            s[i]='#';
        }
    }
    return s;
}