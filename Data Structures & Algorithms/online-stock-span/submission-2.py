class StockSpanner:

    def __init__(self):
        self.arr = []
        

    def next(self, price: int) -> int:
        self.arr.append(price)
        count = 0
        i = len(self.arr)-1
        while self.arr[i] <= price:
            count += 1
            if i-1<0:
                break
            i -= 1
        return count
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)