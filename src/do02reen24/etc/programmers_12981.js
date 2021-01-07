const failUser = (n, index) => {
  let person = index % n;
  let order = Math.floor(index / n) + 1;
  if (person === 0) {
    person = n;
    order -= 1;
  }
  return [person, order];
};

const getLastChar = (word) => word.charAt(word.length - 1);

const solution = (n, words) => {
  const dictionary = {};
  let lastChar = words[0][0];
  for (let index = 0; index < words.length; index += 1) {
    const word = words[index];
    if (lastChar === word[0] && dictionary[word] === undefined) {
      dictionary[word] = true;
      lastChar = getLastChar(word);
      continue;
    }
    return failUser(n, index + 1);
  }

  return [0, 0];
};
