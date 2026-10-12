public class Solution {
    public int smallestDivisibleDigitProduct(int n, int t) {
        for (int x = n; ; x++) {
            if (digitProduct(x) % t == 0) {
                return x;
            }
        }
    }

    private int digitProduct(int num) {
        int product = 1;
        while (num > 0) {
            product *= (num % 10);
            num /= 10;
        }
        return product;
    }
}