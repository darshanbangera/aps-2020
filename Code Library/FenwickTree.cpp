#include<iostream>
using namespace std

int BIT[1000],a[1000];
int n = 10;

void update(int index, int value)
{
  for( ; index<=n ; index+=(index&-index))
  {
    BIT[i] += value;
  }
}
int query(int i)
{
  int sum = 0;
  for(;i>=1;i-=(i&-i))
  {
    sum = sum + BIT[i];
  }
  return sum;
}

void main()
{
  cin>>n;
  int lower,upper,sum;
  int i;
  for(i = 0;i<=n;i++)
  {
    cin>>a[i];
    update(i,a[i]);
  }
  cin>>lower>>upper;
  sum = query(upper) - query(lower);
}
