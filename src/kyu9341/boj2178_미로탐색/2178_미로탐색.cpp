#include<iostream>
#include<vector>
#include<queue>
#include<cstdio>
#include<cstring>

using namespace std;

const int MAX = 100;
int n, m;
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
int map[MAX + 1][MAX + 1];
int dist[MAX + 1][MAX + 1];
queue< pair<int, int> > q;

void bfs(int sx, int sy) {
  q.push(make_pair(sx, sy));
  dist[sx][sy] = 1;

  while(!q.empty()) {
    int x = q.front().first;
    int y = q.front().second;
    q.pop();

    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];

      if (!(nx >= 0 && ny >= 0 && nx < n && ny < m)) continue;
      if (dist[nx][ny] != -1 || map[nx][ny] != 1) continue;
      q.push(make_pair(nx, ny));
      dist[nx][ny] = dist[x][y] + 1;
    }

    if (dist[n - 1][m - 1] != -1) break;
  }
}

int main() {

  cin >> n >> m;

  memset(dist, -1, sizeof(dist));

  for (int i = 0; i < n; i++) 
    for (int j = 0; j < m; j++) 
      scanf("%1d", &map[i][j]);

  bfs(0, 0);

  cout << dist[n - 1][m - 1] << '\n';
}

// C++ 사용자들 중에 숫자 하나씩을 떼어서 입력받고 싶어서 cin을 쓰다가 미로만 scanf로 입력받는 경우가 있습니다. 이 때에는 절대로 sync_with_stdio(false); 를 해서는 안 됩니다.
