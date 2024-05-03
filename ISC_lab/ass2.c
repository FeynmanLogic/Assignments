#include <stdio.h>
#include <string.h>
void Encrypt()
{
char msg[100];
printf("Enter the message to be encrypted in caesar cipher: ");
scanf(" %[^\n]%*c", msg);
int i,k;
printf("Enter shift value for the message: ");
scanf("%d",&k);
for(i=0;msg[i]!='\0';i++)
{
if(msg[i]<65+k)
{
msg[i]=90-(64+k-msg[i]);
}
else
{
msg[i]=msg[i]-k;
}
}
printf("encrypted message is: ");
puts(msg);
}
void Decrypt()
{
char msg[100];
printf("Enter the message to be decrypted in caesar cipher: ");
scanf(" %[^\n]%*c", msg);
int i,k;
printf("Enter shift value for the message: ");
scanf("%d",&k);
for(i=0;msg[i]!='\0';i++)
{
if(msg[i]+k>90)
{
msg[i]=msg[i]+k-26;
}
else
{
msg[i]=msg[i]+k;
}
}
printf("decrypted message is: ");
puts(msg);

}
void Freqanal()
{
char msg[100];
printf("Enter the message to be decrypted in caesar cipher: ");
scanf(" %[^\n]%*c", msg);
int i = 0,maxpos=0,m=0,key;
int freq[26] = { 0 };
while (msg[i] != '\0') {
freq[msg[i] - 'A']++;
i++;
}
i=0;
for(i=0;i<26;i++)
{
if(freq[i]>=m)
{
m=freq[i];
maxpos=i;
}
}
if(maxpos<4)
{key=26+key-maxpos+1;}
else{key=maxpos-4+1;}
printf("key is:%d",key);
}
void BruteForce(char msg[])
{
int shift;
printf("Brute forcing Caesar cipher...\n");
for (shift = 0; shift < 26; shift++) {
int i;
printf("Shift %d: ", shift);
for (i = 0; msg[i] != '\0'; i++) {
if (msg[i] >= 'A' && msg[i] <= 'Z') {
char decrypted_char = msg[i] - shift;
if (decrypted_char < 'A') {
decrypted_char += 26;
}
printf("%c", decrypted_char);
} else {
printf("%c", msg[i]);
}
}
printf("\n");

}
}
void main()
{
int n;
printf("Enter 1 for encrypt, 2 for decrypt, 3 for frequecy analysis, and 4 for decryption by brute force");
scanf("%d",&n);
char msg[100];
switch(n)
{
case 1:
Encrypt();
break;
case 2:
Decrypt();
break;
case 3:
Freqanal();
break;
case 4:
printf("Enter the message to be decrypted with brute force: ");
scanf(" %[^\n]%*c", msg);
BruteForce(msg);
break;
break;
}
}