#include<cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long MaxPairwiseProductfast(const vector<int> &numbers) {
    long long max_product = 0;
    int n = numbers.size();

    long long maxindex1 = -1;
    for (int i = 0; i < n; i++){
        if(maxindex1 == -1 || numbers[i] > numbers[maxindex1])
        maxindex1 = i;
    }

    long long maxindex2 = -1;
    for (int i = 0; i < n; i++){
        if(i == maxindex1)
        continue;

        if(maxindex2 == -1 || numbers[i] > numbers[maxindex2])
        maxindex2 = i;
    }
    return ((long long) numbers[maxindex1] * numbers[maxindex2]); 
}

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }

    cout << MaxPairwiseProductfast(numbers) << "\n";
    return 0;
}
