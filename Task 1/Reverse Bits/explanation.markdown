## Explanation
- Here they asked to reverse the bits of a `unsigned integer`.
- `bin(n)` converts the integer n to a `binary string` prefixed with `"0b"`. For example, if n = 5, then bin(n) would return `'0b101'`.
- `bin(n)[2:]` removes the `'0b'` prefix, so `'0b101'` becomes `'101'`.
- `.zfill(32)` ensures that the binary string has exactly `32 bits` by padding with zeros on the left if necessary. For example, `'101'` becomes `'00000000000000000000000000000101'`.
- Then I converted the bit number to integer using `int(a,2)`.
