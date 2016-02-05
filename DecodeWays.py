class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s == '0': return 0

        strlen = len(s)
        res = 1
        self.fibo_sum = [0, 1, 2, 4]
        ifast = 0

        while ifast < strlen:
            if s[ifast] != '1' and s[ifast] != '2':
                if s[ifast]=='0':
                    return 0
                ifast += 1
                continue
            islow = ifast
            ifast += 1

            while ifast < strlen:
                if s[ifast] == '1' or s[ifast] == '2':
                    ifast += 1
                    continue
                digit = ord(s[ifast])-ord('0')
                if digit!=0 and (s[ifast-1]=='1' or digit<7):
                    seglen = ifast-islow+1
                elif digit == 0:
                    seglen = ifast-islow-1
                else:
                    seglen = ifast-islow
                break

            if ifast == strlen:
                seglen = ifast-islow
            listlen = len(self.fibo_sum)
            if seglen > listlen:
                for i in xrange(listlen-1, seglen):
                    self.fibo_sum.append(2*self.fibo_sum[i] - self.fibo_sum[i-2])
            if seglen != 0:
                res *= 1+self.fibo_sum[seglen-1]
            ifast += 1

        return res

