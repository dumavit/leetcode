/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let result = 0;
    const visited = {};
    nums.forEach(number => {
      if (number in visited) {
          result += visited[number];
        visited[number] += 1;
      } else visited[number] = 1;
    })
    
    return result;
};