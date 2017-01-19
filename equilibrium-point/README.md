### Find the Equilibrium Point...

Given an array of random integers. Find the index in the array where the sum of the values on the left side is closest to the sum of the values on the right side.

Test Case 1: `[4, -2, 3, -3, 2, 1]`
The equilibrium point of  yields the following two sets:
`[4, -2], [3, -3, 2, 1]`

Test Case 2: `[-1, 3, -2]`
The equilibrium point yields the following two sets:
`[-1, 3, -2], []`

Test Case 3: `[-1, 3, -3]`
The equilibrium point yields the following two sets:
`[-1], [3, -3]`

Test Case 4: `[100, 3, -20, 47, 71]`
The equilibrium point yields the following two sets:
`[100], [3, -20, 47, 70]`

Test Case 5: `[14, 22, -29, 58, 10042, 25, -1577, 2, 0, 1]`
The equilibrium point yields the following two sets:
`[100], [3, -20, 47, 70]`

Run: `node equilibrium-point.js` to execute the test assertions.
