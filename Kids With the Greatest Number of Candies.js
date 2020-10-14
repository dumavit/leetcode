/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    const greatestNumber = candies.reduce((acc, curr) => curr > acc? curr: acc, 0);
    return candies.map(candiesNumber => candiesNumber+extraCandies>= greatestNumber);
};