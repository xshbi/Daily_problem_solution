#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int x;
    cout<<"Type the given no: ";
    cin>>x;
    if (x%2==0)
    {
        cout<<"This is even no: ",x;
    }
    else
    {
        cout<<"This is an odd no: ",x;
    }
    return 0;
}



