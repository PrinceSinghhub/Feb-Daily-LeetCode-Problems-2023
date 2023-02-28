class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        string = ""
        List = [str(i) for i in num]
        for i in List:
            string += i

        res = str(int(string) + k)

        finAns = [int(i) for i in res]
        return finAnsfree
        return res
