/**
 * Initialize your data structure here.
 */
var RandomizedSet = function() {
    this.direct_dict = {};
    this.invert_dict = {};
    this.elem_count = 0;
};

/**
 * Inserts a value to the set. Returns true if the set did not already contain the specified element. 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if (val in this.direct_dict) return false;
    this.direct_dict[val] = this.elem_count
    this.invert_dict[this.elem_count] = val;
    this.elem_count += 1;
    return true;
};

/**
 * Removes a value from the set. Returns true if the set contained the specified element. 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    const valIndex = this.direct_dict[val];
    if (!Number.isFinite(valIndex)) return false;
    this.invert_dict[valIndex] = this.invert_dict[this.elem_count-1];
    this.direct_dict[this.invert_dict[valIndex]] = valIndex;
    delete this.direct_dict[val];
    delete this.invert_dict[this.elem_count -1];
    this.elem_count -= 1;
    return true;
};

/**
 * Get a random element from the set.
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    const index = Math.floor(Math.random()*this.elem_count);
    return this.invert_dict[index];
};

/** 
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */