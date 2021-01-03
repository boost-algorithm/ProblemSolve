const getCombinationNumber = (object) => {
  let combination = 1;
  for (const key in object) {
    const itemLength = object[key].length + 1;
    combination *= itemLength;
  }
  return combination;
};

const solution = (clothes) => {
  const closet = {};
  clothes.forEach(([cloth, clothType]) => {
    closet[clothType]
      ? closet[clothType].push(cloth)
      : (closet[clothType] = [cloth]);
  });

  return getCombinationNumber(closet) - 1;
};
