function splitSkill(skill) {
  return skill.split('');
}

function getBeforeSkill(skills) {
  const beforeSkill = {};
  skills.reduce((arr, now) => {
    beforeSkill[now] = JSON.parse(JSON.stringify(arr));
    arr.push(now);
    return arr;
  }, []);
  return beforeSkill;
}

function isValid(tree, beforeSkill) {
  const study = {};
  for (let skill of tree) {
    study[skill] = true;
    if (!beforeSkill[skill]) continue;
    for (let bSkill of beforeSkill[skill]) {
      if (!study[bSkill]) return 0;
    }
  }
  return 1;
}

function solution(skill, skill_trees) {
  const beforeSkill = getBeforeSkill(splitSkill(skill));
  return skill_trees.reduce(
    (sum, tree) => sum + isValid(splitSkill(tree), beforeSkill),
    0
  );
}

console.log(solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA']));
