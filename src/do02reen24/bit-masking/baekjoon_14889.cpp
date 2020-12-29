#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int MAX_INT = 20;
int main() {
    int n;
    int ans = -1;
    vector<int> order;
    int team[MAX_INT][MAX_INT];
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cin >> team[j][i];
        if (i < (n / 2)) order.push_back(0);
        else order.push_back(1);
    }
   
    do {
        int start = 0;
        int link = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (order[i] == 0 && order[j] == 0) start += team[i][j] + team[j][i];
                if(order[i] == 1 && order[j] == 1) link += team[i][j] + team[j][i];
            }
        }
        int diff = abs(start - link) / 2;
        if (ans == -1 || ans > diff) ans = diff;
    } while (next_permutation(order.begin(), order.end()));
    
    cout << ans << endl;
}