#include  <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  char *int_to_Roman(int);
  printf("%s\n", int_to_Roman(atoi(*++argv)));
}

char *int_to_Roman(int num)
{
  int digit = 0;
  static char s[16] = "\0";
  char *p = s;

  if (num >= 1000) {
    digit = (int)(num/1000);
      for (; digit > 0; --digit)
        *p++ = 'M';
    num %= 1000;
  }

  if (num >= 100)
    if ((digit = (int)(num/100))==4 || digit==9) {
      *p++ = 'C';
      *p++ = (digit == 9) ? 'M' : 'D';
      num %= 100;
    } else {
      if (digit >= 5) {
        *p++ = 'D';
        digit -= 5;
      }
      for (; digit > 0; --digit)
        *p++ = 'C';
      num %= 100;
    }

  if (num >= 10)
    if ((digit = (int)(num/10))==4 || digit==9) {
      *p++ = 'X';
      *p++ = (digit == 9) ? 'C' : 'L';
      num %= 10;
    } else {
      if (digit >= 5) {
        *p++ = 'L';
        digit -= 5;
      }
      for (; digit > 0; --digit)
        *p++ = 'X';
      num %= 10;
    }

  if (num >= 1)
    if ((digit = num) == 4 || digit == 9) {
      *p++ = 'I';
      *p++ = (digit == 9) ? 'X' : 'V';
    } else {
      if (digit >= 5) {
        *p++ = 'V';
        digit -= 5;
      }
      for (; digit > 0; --digit)
        *p++ = 'I';
    }
  *p = '\0';
  return s;
}


