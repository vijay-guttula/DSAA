#include<cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


long long MaxPairwiseProduct(const vector<int> &numbers) {
    int max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            max_product = (long long ) max(max_product, numbers[first] * numbers[second]);
        }
    }

    return max_product;
}

int MaxPairwiseProductfast(const vector<int> &numbers) {
    int max_product = -1;
    int n = numbers.size();
}

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {

        cin >> numbers[i];
    }

    cout << MaxPairwiseProduct(numbers) << "\n";
    return 0;
}
