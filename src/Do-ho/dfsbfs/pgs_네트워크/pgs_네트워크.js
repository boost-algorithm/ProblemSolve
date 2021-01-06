const solution = (n, computers) => {
    let answer = 0;
    let visited = new Array(n).fill(false);
    let queue = [];
    const loopArray = [... new Array(n).keys()];
    const isEmpty = () => queue.length !== 0;
    
    const dfs = () => {
        const targetIdx = queue.pop();
        const target = computers[targetIdx]
        loopArray.forEach((idx) => {
            if(visited[idx] || target[idx] === 0) return;
            queue.push(idx);
            visited[idx] = true;
        });
    }
    
    loopArray.forEach((computerID) => {
        if(visited[computerID]) return;
        queue.push(computerID);
        while(isEmpty()) dfs();
        answer++;
    })
    
    return answer;
}