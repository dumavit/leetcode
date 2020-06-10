/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left=0, right = nums.length;
    
    while (left <= right) {
        const median = Math.floor((right+left)/2);
        if (nums[median] === target) return median;
        if (nums[median]<target)  left = median+1;  
         else right = median-1
    }
    return left;
};