bool isHappy(int n) {
  int tmp = 0, cntr = 0;

  do {
    while (n > 0) {
      tmp += (n%10) * (n%10);
      n /= 10;
    }
    n = tmp;
    tmp = 0;
    cntr++;
  } while (n != 1 && cntr < 7);

  return (n == 1) ? true : false;
}
