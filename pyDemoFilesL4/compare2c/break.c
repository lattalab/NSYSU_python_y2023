#include <stdio.h>
int main()
{  int var = 0;
   while (var <= 5)   //This code stops on #3 
   {  var +=1;
      if (var == 3) break;
      printf("%d",var);  }  }
