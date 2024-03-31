#include <stdio.h>
#include <stdlib.h>
typedef struct {
int x,y,z;
} coord;
coord *A, *B, *C;

void print(coord *P){
   printf("%d,%d,%d\n",
   P->x,P->y,P->z);
}
