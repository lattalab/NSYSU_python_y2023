# include <iostream>
using namespace std;

// 若是沒有先宣告，會有Error產生
int g(int);
int f(int i) { return g(i+1); }

int main()
{
    int a = f(1);
    cout<<a<<endl;
    return 0;
}

int g(int i) { if (i<99) {return f(2*i);} else return i;}