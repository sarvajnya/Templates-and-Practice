def search(pattern, text):
        ans = []
        n = len(text)
        if pattern not in text:
            return []
        i = text.find(pattern)
        ans += [i+1]
        while i<n:
            i = text.find(pattern, i+1, n)
            if i == -1:
                break
            ans += [i+1]
            
        return ans