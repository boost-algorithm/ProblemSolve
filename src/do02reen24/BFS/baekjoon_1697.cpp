#include <iostream>
#include <queue>
using namespace std;
const int MAX_RANGE = 2000000;
bool visit[MAX_RANGE + 1];
int cost[MAX_RANGE + 1];
int main() {
    int n, k;
    cin >> n >> k;
    queue<int> q;
    cost[n] = 0;
    visit[n] = true;
    q.push(n);
    while (!q.empty()) {
        int index = q.front();
        q.pop();
        if (index - 1 >= 0) {
            if (visit[index - 1] == false) {
                q.push(index - 1);
                visit[index - 1] = true;
                cost[index - 1] = cost[index] + 1;
            }
        }
        if (index + 1 < MAX_RANGE) {
            if (visit[index + 1] == false) {
                q.push(index + 1);
                visit[index + 1] = true;
                cost[index + 1] = cost[index] + 1;
            }
        }
        if (index * 2 < MAX_RANGE) {
            if (visit[index * 2] == false) {
                q.push(index * 2);
                visit[index * 2] = true;
                cost[index * 2] = cost[index] + 1;
            }
        }
        if (visit[k] == true) {
            cout << cost[k] << '\n';
            break;
        }
    }
    return 0;
}