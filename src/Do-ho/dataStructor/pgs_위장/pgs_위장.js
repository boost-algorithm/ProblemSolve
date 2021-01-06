const solution = clothes => {
    const clothesObject = clothes.reduce((acc, [name, kind]) => {
        acc.hasOwnProperty(kind)? acc[kind] += 1 : acc[kind] = 1;
        return acc;
    }, new Object());
    
    return Object.values(clothesObject).reduce((acc, val) => acc *= val + 1, 1) - 1;
}