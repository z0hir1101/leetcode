#include <iostream>
#include <cmath>

int main()
{
  std::cout << is_palindrome(1001);
}

bool is_palindrome(int x) {
  if (x < 0) return false;

  int n = 0, tmp;
  for (long i = 1; i <= x; i *= 10, n++)
    ;

  tmp = n;
  for (int i = 0; i < (int)(tmp / 2); ++i, --n)
    if ((int)(x/pow(10, n-1)) % 10 != (int)(x/pow(10, i)) % 10)
      return false;         

  return true;
}

