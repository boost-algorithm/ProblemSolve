#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>

using namespace std;

const int MAX = 100;
int n, m;
vector<int> v[MAX + 1];
int dist[MAX + 1];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int x, y;

  cin >> n >> x >> y >> m;

  memset(dist, -1, sizeof(dist));
  int parent, child;
 
  while (m--) {
    cin >> parent >> child;
    v[parent].push_back(child);
    v[child].push_back(parent);
  }

  queue<int> q;
  dist[x] = 0;
  q.push(x);
  
  while(!q.empty()) {
    int cur = q.front();
    q.pop();

    for (int i = 0; i < v[cur].size(); i++) {
      int next = v[cur][i];
      if (dist[next] != -1) continue;
      dist[next] = dist[cur] + 1;
      q.push(next);
    }

    if (dist[y] != -1) break;
  }

  cout << dist[y] << '\n';
}

