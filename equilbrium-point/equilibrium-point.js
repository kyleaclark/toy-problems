const assert = require('assert')

function findEquilbriumPoint(arr) {
    let totalSum,
        lowestDiffIndex,
        lowestDiffSum = null,
        leftSum = 0,
        rightSum = 0,
        sumUp = 0

    totalSum = arr.reduce(function (prev, curr) {
        return prev + curr
    })

    arr.forEach(function (item, index) {
        leftSum += item
        rightSum = totalSum - leftSum

        let sideDiff = Math.abs(leftSum - rightSum)

        if (lowestDiffSum === null || sideDiff < lowestDiffSum) {
            lowestDiffSum = sideDiff
            lowestDiffIndex = index
        }
    })

    return lowestDiffIndex
}

const numberList1 = [4, -2, 3, -3, 2, 1]
const point1 = findEquilbriumPoint(numberList1) + 1 // for slicing the array
const testCase1 = {
  leftSide: numberList1.slice(0, point1),
  rightSide: numberList1.slice(point1)
}

const numberList2 = [-1, 3, -2]
const point2 = findEquilbriumPoint(numberList2) + 1 // for slicing the array
const testCase2 = {
  leftSide: numberList2.slice(0, point2),
  rightSide: numberList2.slice(point2)
}

const numberList3 = [-1, 3, -3]
const point3 = findEquilbriumPoint(numberList3) + 1 // for slicing the array
const testCase3 = {
  leftSide: numberList3.slice(0, point3),
  rightSide: numberList3.slice(point3)
}

const numberList4 = [100, 3, -20, 47, 71]
const point4 = findEquilbriumPoint(numberList4) + 1 // for slicing the array
const testCase4 = {
  leftSide: numberList4.slice(0, point4),
  rightSide: numberList4.slice(point4)
}

const numberList5 = [14, 22, -29, 58, 10042, 25, -1577, 2, 0, 1]
const point5 = findEquilbriumPoint(numberList5) + 1 // for slicing the array
const testCase5 = {
  leftSide: numberList5.slice(0, point5),
  rightSide: numberList5.slice(point5)
}

console.log('testCase1 : ', testCase1)
assert.deepEqual(testCase1.leftSide, [4, -2])
assert.deepEqual(testCase1.rightSide, [3, -3, 2, 1])

console.log('testCase2 : ', testCase2)
assert.deepEqual(testCase2.leftSide, [-1, 3, -2])
assert.deepEqual(testCase2.rightSide, [])

console.log('testCase3 : ', testCase3)
assert.deepEqual(testCase3.leftSide, [-1])
assert.deepEqual(testCase3.rightSide, [3, -3])

console.log('testCase4 : ', testCase4)
assert.deepEqual(testCase4.leftSide, [100])
assert.deepEqual(testCase4.rightSide, [3, -20, 47, 71])

console.log('testCase5 : ', testCase5)
assert.deepEqual(testCase5.leftSide, [14, 22, -29, 58])
assert.deepEqual(testCase5.rightSide, [10042, 25, -1577, 2, 0, 1])
