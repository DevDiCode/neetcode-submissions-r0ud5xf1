class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        chars = set(ch for word in words for ch in word)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            m = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:m] == w2[:m]:
                return ""
            for j in range(m):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break
        visited = {}  # char: 0=unvisited, 1=visiting, 2=visited
        res = []
        def dfs(ch):
            if visited.get(ch, 0) == 1: return False  # cycle
            if visited.get(ch, 0) == 2: return True   # done
            visited[ch] = 1
            for nei in graph[ch]:
                if not dfs(nei): return False
            visited[ch] = 2
            res.append(ch)
            return True
        for ch in chars:
            if visited.get(ch, 0) == 0:
                if not dfs(ch): return ""
        return "".join(reversed(res))