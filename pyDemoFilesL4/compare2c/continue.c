#include <stdio.h>
int main()
{  int var = 0;                   
   while (var <= 5)   //This code skips the #3 
   {  var +=1;
      if (var == 3) continue;
      printf("%d",var);  }  }
