#include <stdio.h>
void f()
{ static int X, Y=0; // Y initializes once
  X=0;
  printf("%d,%d: X resets, Y doesn't\n",X++,Y++);
}
int main() 
{ f(); // When called, X=0 & Y=0 
  f(); // When called, X=0 & Y=1
  f(); // When called, X=0 & Y=2
}
