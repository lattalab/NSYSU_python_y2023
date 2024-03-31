int x=1, y=1, z=1;
int f() {  
  int x = 2;
  y=5;
  print("%d",x+y+z);//8
}
int main() {    f(); 
   print("%d",x+y+z);
              //1+5+1=7
}
