## Explanation
- In this problem they have asked to find the `bitwise AND` the range of numbers.
- Here we have to find the `common prefix`.
- To do this we initial a variable `cnt` to `count the number of shifts`.
- We put a `while loop` with the condition if the left and right extreme is equal.
- With this we can find out the `common prefix`. 
- After that we shift the left extreme to the left with the cnt variable to get the `bitwise AND`.
### Example
- left = 26  
- right = 30


- bit left  = 11010 
- bit right = 11110

1. **First iteration**:
    - `left = 11010` (26)
    - `right = 11110` (30)
    - Shift both `left` and `right` one bit to the right:
    - `left >>= 1` → `1101` (13)
    - `right >>= 1` → `1111` (15)
    - `cnt = 1`


2. **Second iteration**:
    - `left = 1101` (13)
    - `right = 1111` (15)
    - Shift both `left` and `right` again:
    - `left >>= 1` → `110` (6)
    - `right >>= 1` → `111` (7)
    - `cnt = 2`

3. **Third iteration**:
    - `left = 110` (6)
    - `right = 111` (7)
    - Shift both again:
    - `left >>= 1` → `11` (3)
    - `right >>= 1` → `11` (3)
    - `cnt = 3`

4. **Now, `left == right`** (both are `3`), so the loop exits.

5. **Restore the common prefix**:
    - `left << cnt = 3 << 3 = 24` (because `11000` in binary is 24).

Thus, the bitwise AND of all numbers in the range `[26, 30]` is `24`.




