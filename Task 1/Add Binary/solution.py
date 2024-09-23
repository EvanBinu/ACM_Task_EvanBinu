class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        sum = num1+num2
        binary_sum = bin(sum)
        binary_sum = bin(sum)[2:]
        return(binary_sum)