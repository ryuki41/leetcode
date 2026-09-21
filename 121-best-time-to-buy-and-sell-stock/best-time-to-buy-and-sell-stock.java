class Solution {
    public int maxProfit(int[] prices) {
        int max_price = prices[prices.length -1];
        // pricesのn番目以降の最小値
        Map<Integer, Integer> max_prices = new HashMap<>();

        for (int i = prices.length -1; i > 0; i--) {
            if (prices[i] > max_price) {
                max_price = prices[i];
            }
            max_prices.put(i, max_price);
        }

        int max_profit = 0;

        for (int j = 0; j < prices.length -1; j++) {
            int profit =  max_prices.get(j+1) - prices[j];

            if (max_profit < profit) {
                max_profit = profit;
            }
        }

        return max_profit;
    }
}