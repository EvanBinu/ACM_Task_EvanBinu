## Explanation

- Here we have to find the number that appears `once` using `bit manipulation` all other numbers appears `3 times`.
- I initiales the variables `one` and `two`.
- `Iterated` through the list `nums` and `XOR`ed each element with one and `AND`ed the `Negation` of two with it, likewise for the variable two.
- By doing this the variable that appears `once` will be `one` and we can return that.
