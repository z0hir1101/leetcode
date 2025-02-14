int fib(int n){
  if (n == 0) return n;
  int n1 = 0, n2 = 1, temp;

  for (int i = 0; i < n-1; i++) {
    temp = n2;
    n2 += n1;
    n1 = temp;
  }
  return n2;
}
