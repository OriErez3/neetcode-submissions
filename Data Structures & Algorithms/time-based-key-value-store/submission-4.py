class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append([value,timestamp])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keystore:
            return ""
        ans = self.keystore[key]
        l,r = 0, len(ans)-1
        ret = ""
        while l<=r:
            m = (l+r)//2
            if ans[m][1] <= timestamp:
                ret = ans[m][0]
                l = m+1
            else:
                r = m-1
        return ret
        
