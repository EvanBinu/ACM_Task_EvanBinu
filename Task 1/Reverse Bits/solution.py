class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:].zfill(32)        
        a = b[::-1]        
        a = int(a, 2)
        return a