class Solution {
public:
    int reverse(int x) {
        int result = 0;
        int digit = 0;
        while (x != 0){
            if (result > INT_MAX/10) return 0;
            if (result < INT_MIN/10) return 0;
            digit = x%10;
            x = x/10;
            result = result*10+digit;
        }
        
        return result;
    }
};
