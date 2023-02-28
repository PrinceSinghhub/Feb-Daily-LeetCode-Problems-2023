class Solution:
    def convert(self, s, nRows):
        if nRows==1:
            return s
        period= 2*(nRows -1)
        lines=["" for i in range(nRows)]
        d={} # dict remainder:line
        for i in range(period):
            if i<nRows:
                d[i]=i
            else:
	            d[i]=period-i

        for i in range(len(s)):
            lines[ d[i%period] ] +=s[i]

        return "".join(lines)