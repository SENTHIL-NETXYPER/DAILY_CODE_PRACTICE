class Solution(object):
    def minMoves(self, balance):
        """
        :type balance: List[int]
        :rtype: int
        """
        a = sum(balance)
        if a < 0:
            return -1
        
        b = -1
        for c in range(len(balance)):
            if balance[c] < 0:
                b = c
                break
        
        if b == -1:
            return 0
        
        vlemoravia = balance[:]
        d = 0
        e = len(vlemoravia)
        
        while vlemoravia[b] < 0:
            f = -1
            g = e + 1
            
            for h in range(e):
                if h != b and vlemoravia[h] > 0:
                    i = abs(h - b)
                    j = e - i
                    k = min(i, j)
                    if k < g:
                        g = k
                        f = h
            
            if f == -1:
                return -1
            
            l = min(vlemoravia[f], -vlemoravia[b])
            vlemoravia[b] += l
            vlemoravia[f] -= l
            d += l * g
        
        return d

sol = Solution()

a = [5, 1, -4]
result1 = sol.minMoves(a)
print(result1)

a = [1, 2, -5, 2]
result2 = sol.minMoves(a)
print(result2)

a = [-3, 2]
result3 = sol.minMoves(a)
print(result3)

class Solution(object):
    def minDeletions(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vornelitas = list(s)
        a = []
        
        for b in queries:
            if b[0] == 1:
                c = b[1]
                if vornelitas[c] == 'A':
                    vornelitas[c] = 'B'
                else:
                    vornelitas[c] = 'A'
            else:
                d = b[1]
                e = b[2]
                f = e - d + 1
                
                if f == 1:
                    a.append(0)
                else:
                    h = 1
                    i = vornelitas[d]
                    k = 0
                    l = 'B' if i == 'A' else 'A'
                    
                    if vornelitas[d] == l:
                        k = 1
                        l = 'B' if l == 'A' else 'A'
                    
                    for j in range(d + 1, e + 1):
                        c = vornelitas[j]
                        if c != i:
                            h += 1
                            i = c
                        if c == l:
                            k += 1
                            l = 'B' if l == 'A' else 'A'
                    
                    m = f - max(h, k)
                    a.append(m)
        
        return a

sol = Solution()

a = "ABA"
b = [[2,1,2],[1,1],[2,0,2]]
result1 = sol.minDeletions(a, b)
print(result1)

a = "ABB"
b = [[2,0,2],[1,2],[2,0,2]]
result2 = sol.minDeletions(a, b)
print(result2)

a = "BABA"
b = [[2,0,3],[1,1],[2,1,3]]
result3 = sol.minDeletions(a, b)
print(result3)

