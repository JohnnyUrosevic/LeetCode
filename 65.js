/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    var regex = /^[+-]?((\d+\.?\d*)|(\.\d+))(([eE][+-]?)?\d+)?$/
    
    return regex.test(s.trim());
};
