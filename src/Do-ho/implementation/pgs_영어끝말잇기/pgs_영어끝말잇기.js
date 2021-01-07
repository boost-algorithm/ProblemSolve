const solution = (n, words) => {
    let [people, order] = [0, 0];
    let prevText = null;
    let wordSet = [];
    const isNotPrevTextNull = () => prevText !== null;
    const isNotMatchWord = (word) => prevText[prevText.length - 1] !== word[0];
    const isContainWordSet = (word) => wordSet.includes(word);
    
    for (let i=0; i<words.length; i++) {
        const word = words[i];
        if(isNotPrevTextNull() && (isNotMatchWord(word) || isContainWordSet(word))) {
            people = (i % n) + 1;
            order = Math.floor(i / n) + 1;
            break;
        }
        prevText = word;
        wordSet.push(word);
    }
    
    return [people, order];
}