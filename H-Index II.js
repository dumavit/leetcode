/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    if (!citations.length) return 0;
    let left = 0;
    let right = citations.length-1;
    while (left <= right) {
        const medium = Math.round((left+right)/2);
        if (medium + citations[medium]>=citations.length)
            right=medium-1
        else left = medium+1;
    }
    return citations.length - left;
};

hIndex([])
hIndex([0])
hIndex([1])