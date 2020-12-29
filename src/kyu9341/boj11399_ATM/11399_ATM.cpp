#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n;

int main() {
  cin >> n;
  vector<int> v(n);
  int sum = 0;

  for (int i = 0; i < n; i++) cin >> v[i];

  sort(v.begin(), v.end());

  int now = 0;
  for (int i = 0; i < n; i++) {
    now = now + v[i];
    sum += now;
  }

  cout << sum << '\n';
}
