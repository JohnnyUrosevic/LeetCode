/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows < 2) return s;
    
    let zag = [];
    
    for (let i = 0; i < numRows; i++) {
        zag.push([]);
    }
    
    let result = "";
    let diagonal = false;
    
    let j = 0;
    let counterMax = numRows;
    
    let diagonalLength = numRows - 2;

    for (let i = 0; i < s.length; i++) {
      if (diagonal) {
          zag[numRows - j - 2].push(s[i]);
      }  
      else {
          zag[j].push(s[i]);
      }
        
      j++;
      if ((!diagonal && j === numRows) || (diagonal && j === diagonalLength)) {
          if (numRows != 2)
              diagonal = !diagonal;
          j = 0;
      }
    }
    
    for (let i = 0; i < numRows; i++) {
        for (let j = 0; j < zag[i].length; j++) {
            result += zag[i][j]; 
        }
    }
    return result;
};
