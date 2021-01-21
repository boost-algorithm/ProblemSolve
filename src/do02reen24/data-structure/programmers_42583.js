class Bridge {
  constructor(weight, remain) {
    this.weight = weight;
    this.remain = remain;
  }

  getRemain() {
    return this.remain;
  }

  subRemain() {
    this.remain--;
  }
}

function sumBridge(bridge) {
  return bridge.reduce((sum, now) => (sum += now.weight), 0);
}

function solution(bridge_length, weight, truck_weights) {
  let time = 1;
  let index = 0;
  const bridges = [];
  while (index < truck_weights.length) {
    const remain = weight - sumBridge(bridges);
    if (remain >= truck_weights[index]) {
      bridges.push(new Bridge(truck_weights[index], bridge_length));
      index++;
    }
    time++;
    bridges.forEach((bridge) => bridge.subRemain());
    if (bridges[0].getRemain() === 0) bridges.shift();
  }
  return time + bridge_length - 1;
}
