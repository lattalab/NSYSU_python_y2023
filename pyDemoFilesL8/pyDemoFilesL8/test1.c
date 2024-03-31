#include <stdio.h>
int total= 0;
void sum(int arg1, int arg2 ){ 
   int total = arg1 + arg2; 
   printf("Inside total= %d\n",total);
}
int main(){
sum( 10, 20 ); 
printf("Outside total= %d\n",total);
}
