#include "stuff.h"
int main() {
   A=(coord*)malloc(sizeof(coord));
   A->x=1;
   B=A; C=B;
   A->y=2; C->z=3;
   A=NULL; B=NULL;
   print(C);
   C=NULL;
   print(C);
}
