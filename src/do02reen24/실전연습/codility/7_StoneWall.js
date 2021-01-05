const solution = (H) => {
  const queue = [H];
  let block = 0;
  while (queue.length > 0) {
    const h = queue.pop();
    if (h.length === 0) continue;
    const min = Math.min.apply(null, h);
    const remain = h.reduce((arr, cur) => {
      if (cur === min) {
        queue.push(arr);
        return [];
      }
      arr.push(cur);
      return arr;
    }, []);
    queue.push(remain);
    block += 1;
  }
  return block;
};
