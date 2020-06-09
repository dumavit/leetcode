/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    for (const char of t) {
        if (s[0] === char) s = s.substr(1)
        if (!s) return true;
    }
    return !s;
};