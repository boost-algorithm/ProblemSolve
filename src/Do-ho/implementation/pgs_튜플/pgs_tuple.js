const removeBracket = s => {
    const re = /[0-9]+(,[0-9]+)*/g;
    return s.match(re);
}

const compareFunction = (prev, curr) => prev.length - curr.length;

const parseStr = s => {
    const strWithOutBracket = removeBracket(s);
    const parsed = strWithOutBracket.reduce((acc, cur) => {
        acc.push(cur.split(','));
        return acc;
    }, [])
    return parsed.sort(compareFunction);
}

const solution = s => {
    const parsedArr = parseStr(s);
    const answer = parsedArr.reduce((acc, cur) => {
        const filterItem = cur.filter((item) => !acc.includes(item));
        acc.push(filterItem[0]);
        return acc;
    }, []).map(item => parseInt(item))
    return answer;
}