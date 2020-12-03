#include <iostream>
#include <stack>
#include <string>

using namespace std;

int isBalanced(char s[])
{
    stack<char> a;
    char temp;
    int ret;
    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] == '{' || s[i] == '[' || s[i] == '(')
        {
            a.push(s[i]);
        }
        else
        {
            if (a.empty())
            {
                ret = i + 1;
                return ret;
            }
            temp = a.top();

            if ((temp == '{' && s[i] == '}') || (temp == '(' && s[i] == ')') || (temp == '[' && s[i] == ']'))
            {
                a.pop();
            }

            else
            {
                ret = i + 1;
                return ret;
            }
        }
    }
    if (a.empty())
        return -1;
}

int main()
{
    char s[50];
    cin >> s;

    int x = isBalanced(s);
    if (x == -1)
        cout << "Success";
    else
        cout << x;

    return 0;
}