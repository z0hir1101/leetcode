#include <stdio.h>

int main(int argc, char *argv[])
{
  int longest_substr(char *);
  printf("%d\n", longest_substr(*++argv));
}

int longest_substr(char *s)
{
  char *p = s;
  int last_index[128] = {0}; //Array to store last seen position of characters
  int maxln, start; // maxln stores the result, start is the current substring's first index

  maxln = start = 0;
  for (; *p; ++p) {
    //If the character was seen after 'start', move 'start' to exclude duplicates
    if (last_index[*p] > start)
      start = last_index[*p];

    //Update the character's last seen position (use 1-based indexing)
    last_index[*p] = p-s + 1;

    //Calculate the length of the current substring and update maxLength
    maxln = (p-s-start+1 > maxln) ? p-s-start+1 : maxln;
  }
  return maxln;
}

