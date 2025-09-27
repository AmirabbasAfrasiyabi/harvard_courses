#include <stdio.h>

int main(void)
{
    char answer[100];  // Array to store the name (up to 99 characters + null terminator)
    printf("What is your name? ");
    scanf("%99s", answer);  // Read string input (limit to 99 chars to prevent buffer overflow)
    printf("Hello, %s!\n", answer);
    return 0;
}