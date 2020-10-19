#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, p, e;
    cin >> n >> p >> e;
    vector<pair<int,int>> member;
    vector<int> isGift(n);
    for (int i = 0; i < n; i++) {
        int min, max;
        cin >> min >> max;
        member.push_back(make_pair(min, max));
        if ((n - i) <= p) isGift[i] = 1;
    }
    do {
        int min = 0, max = 0;
        int sol[20] = { 0, };
        for (int i = 0; i < n; i++) {
            if (isGift[i] == 0) continue;
            min += member[i].first;
            max += member[i].second;
            sol[i] = member[i].first;
        }
        int remain = e - min;
        if (min <= e && max >= e) {
            for (int i = 0; i < n; i++) {
                if (isGift[i] == 0) continue;
                int diff = member[i].second - member[i].first;
                if (diff < remain) { 
                    remain -= diff;
                    sol[i] += diff;
                }
                else {
                    sol[i] += remain;
                    remain = 0;
                }
            }
            for (int i = 0; i < n; i++) cout << sol[i] << " ";
            return 0;
        }
    } while (next_permutation(isGift.begin(), isGift.end()));
    cout << -1 << endl;
    return 0;
}