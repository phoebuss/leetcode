class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] or matrix == [[]] : return []
        top = left = 0
        bottom = len(matrix)-1
        right = len(matrix[0])-1
        res = []

        while True:
            for j in xrange(left, right+1):
                res.append(matrix[top][j])
            top += 1
            if top > bottom: return res

            for i in xrange(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if left > right: return res

            for j in xrange(right, left-1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
            if top > bottom: return res

            for i in xrange(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right: return res
        
