/**
 * @param {number[]} nums
 * @return {number[]}
 */
var largestDivisibleSubset = function(nums) {
    nums = nums.sort((a,b) => a-b);
    const dp = new Array(nums.length);
    dp.fill(1);
    for (let i=1; i<nums.length; i++) 
        for (let j=0; j<i; j++) {
            if (nums[i] % nums[j] === 0) {
                dp[i] = Math.max(dp[i], dp[j]+1);
            }
        }

    let maxIndex = 0;
    for (let i=0; i<dp.length; i++)
        if (dp[i]>dp[maxIndex]) maxIndex = i;
    const result = [];
    let currentLength = dp[maxIndex];
    let temp = nums[maxIndex];
    for (let i=maxIndex; i>=0; i--) {
        if (temp % nums[i] === 0 && dp[i]===currentLength) {
            result.push(nums[i]);
            temp = nums[i];
            currentLength -= 1;
        }
    }
    return result;
};


// console.log(largestDivisibleSubset([1,2,3,4,8,12]))