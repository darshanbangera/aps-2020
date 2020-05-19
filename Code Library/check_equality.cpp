#include <iostream> 
using namespace std; 
 
void areSame(int a, int b) 
{ 
    if (a ^ b) 
        cout << "Not Same"; 
    else
        cout << "Same"; 
} 
int main() 
{ 
    areSame(10, 20); 
} 
