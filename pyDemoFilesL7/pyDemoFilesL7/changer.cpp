#include <iostream>
#include <string>
using namespace std;
void changer(int a, int &b, int *c, string d, char *e) {
  a=1;b=1;c[0]=1;d="one";e[0]='o';e[1]='n';e[0]='e';e[1]='\0';
}
main() {
 int a=0, b=0, c[100]={0};
 string d="zero";
 char e[]="zero";
 cout<<"a="<<a<<",b="<<b<<",c="<<c[0]<<",d="<<d<<","<<e<<"\n";
 changer(a,b,c,d,e);
 cout<<"a="<<a<<",b="<<b<<",c="<<c[0]<<",d="<<d<<","<<e<<"\n";
}
