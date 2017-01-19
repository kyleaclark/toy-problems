const assert = require('assert')

let fibMap = {}
let fibVal

function fibCalc(fibIndex) {
    if (fibIndex in fibMap) {
        return fibMap[fibIndex];
    }

    if (fibIndex <= 1) {
        return fibIndex;
    }

    fibVal = fibCalc(fibIndex - 1) + fibCalc(fibIndex - 2);
    fibMap[fibIndex] = fibVal;
    return fibVal;
}

console.log('Test Case 1: 0 => 0')
assert.equal(fibCalc(0), 0)

console.log('Test Case 2: 1 => 1')
assert.equal(fibCalc(1), 1)

console.log('Test Case 3: 2 => 1')
assert.equal(fibCalc(2), 1)

console.log('Test Case 4: 3 => 2')
assert.equal(fibCalc(3), 2)

console.log('Test Case 5: 4 => 3')
assert.equal(fibCalc(4), 3)

console.log('Test Case 6: 12 => 144')
assert.equal(fibCalc(12), 144)

console.log('Test Case 7: 12 => 144')
assert.equal(fibCalc(12), 144)

console.log('Test Case 8: 4 => 3')
assert.equal(fibCalc(4), 3)

console.log('Test Case 9: 20 => 6765')
assert.equal(fibCalc(20), 6765)

console.log('Test Case 10: 24 => 46368')
assert.equal(fibCalc(24), 46368)
