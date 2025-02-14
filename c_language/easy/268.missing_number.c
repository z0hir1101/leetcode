#include  <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int missing_num(int);
  printf("%d\n", missing_num(atoi(*++argv), atoi(*++argv));
}

int missing_num(int *nums, int numsSize)
{
  int arr[numsSize+1], i;

  for (i = 0; i < numsSize+1; ++i)
    arr[i] = 0;
  for (i = 0; i < numsSize; ++i)
    arr[nums[i]]++;
  for (i = 0; i < numsSize+1; ++i)
    if (arr[i] == NULL)
      return i;
  return -1;
}

  
