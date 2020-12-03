#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    stack<int> s;
    string s1;
    int n, max;
    int i;
    cin >> i;
    for (int j = 0; j < i; j++)
    {
        cin >> s1 >> n;
        if (s1 == "push")
        {
            s.push(n);
        }
        else if (s1 == "max")
        {
            cout << max(s);
        }
        else if (s1 == "pop")
        {
            s.pop();
        }
    }
}