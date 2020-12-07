#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    stack<int> s;
    stack<int> trackmax;
    string s1;
    int n, max;
    int i;
    cin >> i;
    for (int j = 0; j < i; j++)
    {
        cin >> s1;
        if (s1 == "push")
        {
            cin >> n;
            s.push(n);
            if (j == 0)
            {
                trackmax.push(n);
            }
            else if (trackmax.top() < n)
            {
                trackmax.push(n);
            }
            else
            {
                max = trackmax.top();
                trackmax.push(max);
            }
        }
        else if (s1 == "max")
        {
            cout << trackmax.top() << endl;
        }
        else if (s1 == "pop")
        {

            trackmax.pop();
            s.pop();
        }
    }
}