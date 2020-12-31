const getLongestPalindrome = (left, right, arrFromStr) => {
  let maxLength = 0;
  const isInRange = (left, right) => left >= 0 && right < arrFromStr.length;

  while (isInRange(left, right)) {
    if (arrFromStr[left] !== arrFromStr[right]) return maxLength;

    maxLength = right - left + 1;
    left -= 1;
    right += 1;
  }

  return maxLength;
};

const solution = s => {
  let maxLength = 0;
  const arrFromStr = [...s];

  const checkLength = (_, index) => {
    const odd = getLongestPalindrome(index, index, arrFromStr);
    const even = getLongestPalindrome(index, index + 1, arrFromStr);
    maxLength = Math.max(maxLength, Math.max(odd, even));
  };

  arrFromStr.forEach(checkLength);

  return maxLength;
};

(() => {
  const inputs = ['abcdcba', 'abacde'];

  inputs.forEach(input => console.log(solution(input)));
})();
