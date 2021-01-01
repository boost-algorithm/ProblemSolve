const getOddPalindromeLength = (s, idx) => { return loopPalindrome(s, idx-1, idx+1, 1); }
const getEvenPalindromeLength = (s, idx) => {
    if(s[idx] != s[idx+1]) return 0;
    return loopPalindrome(s, idx-1, idx+2, 2);
}

const loopPalindrome = (s, left, right, palindromeCount) => {
    while(left >= 0 && right < s.length) {
        if(s[left--] !== s[right++]) break;
        palindromeCount += 2
    }
    return palindromeCount;
}

const solution = s => {
    let answer = 0;
    for (let i=0; i<s.length; i++) {
        answer = Math.max(answer, getOddPalindromeLength(s, i), getEvenPalindromeLength(s, i));
    }
    return answer;
}