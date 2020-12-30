#include<iostream>
#include<vector>

using namespace std;

int day, cake;

int main() {
  int A, B;

  cin >> day >> cake;
  vector< pair<int, int> > d(day + 1);

  d[1] = make_pair(1, 0);
  d[2] = make_pair(0, 1);

  for (int i = 3; i <= day; i++) {
    d[i].first = d[i - 1].first + d[i - 2].first;
    d[i].second = d[i - 1].second + d[i - 2].second;
  }

  for (int i = 1; i <= cake; i++) {
    int cntA = d[day].first;
    int cntB = d[day].second;

    if ((cake - cntA * i) % cntB == 0) {
      A = i;
      B = (cake - cntA * A) / cntB;
      break;
    }
  }

  cout << A << '\n' << B << '\n';
}


