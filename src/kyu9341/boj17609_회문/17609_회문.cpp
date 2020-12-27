#include<iostream>

using namespace std;

int t;

int checkPalindrome(string str) {
  int len = str.size();
  int left = 0;
  int right = len - 1;

  int leftPoint;
  int rightPoint;

  bool leftCheck = false;
  bool rightCheck = false;

  while (left < right) {
    if (str[left] != str[right]) {
      if (rightCheck && leftCheck) return 2;

      if (!rightCheck && !leftCheck) {
        leftPoint = left;
        rightPoint = right;
        if (left < right - 1) right--;
        rightCheck = true;
        continue;
      }

      if (rightCheck) {
        left = leftPoint;
        right = rightPoint;
        if (left + 1 < right) left++;
        leftCheck = true;
        continue;
      }

    }
    left++;
    right--;
  }
  if (leftCheck || rightCheck) return 1;
  return 0;
}

int main() {
  ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

  string str;

  cin >> t;
  cin.ignore();

  while(t--) {
    cin >> str;
    cout << checkPalindrome(str) << '\n';
  }
}

/* 
풀이
좌측 끝과 우측 끝에서 한칸씩 중앙으로 이동하며 회문인지 판별
-> 좌측 포인터와 우측 포인터 값이 같지 않다면 먼저 우측 포인터를 한칸 더 이동시킨다.
-> 이후에 계속 진행하였을 때, 회문이라면 유사회문으로 판단
-> 이후에 다시 값이 다른다면, 처음 값이 달랐던 지점으로 이동하여 왼쪽 포인터만 한칸 더 이동시킨다.
-> 이번에도 다시 값이 다르다면, 이 문자열은 회문도, 유사회문도 아님
-> 계속 진행하였을 때, 회문이라면 유사회문으로 판단
*/
