#include <stdio.h>


int main(void)
{
    unsigned int number = 0xffffffff;  // 0b11111111111111111111111111111111, highest unsigned 32 bit number
    printf("before increment: %u\n", number);
    number += 1;
    /* if (number < 0xffffffff) */
    /*     number += 1; */
    /* else */
    /*     printf("not incrementing, dager of overflow!!!\n"); */
    printf("after increment: %u\n", number);
    return 0;
}
