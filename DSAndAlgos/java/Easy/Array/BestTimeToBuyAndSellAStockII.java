package Easy.Array;



public class BestTimeToBuyAndSellAStockII {

    // Exercise at https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

    public int maxProfit(int[] prices) {
        int profit = 0;
        // Step 1: Loop over the Array to find first lowest value before increase
        int buyPrice = Integer.MAX_VALUE;
        for(int i=0; i<prices.length; i++) {
            if(prices[i] < buyPrice) { // An even cheaper buy price was available
                buyPrice = prices[i];
            } else if(prices[i] > buyPrice) { // Profit can be locked in
                profit += prices[i] - buyPrice;
                buyPrice = prices[i];
            }
        }
        return profit;
    }

    public static void main(String[] args) {
        int[] test = new int[]{7,1,5,3,6,4};
        BestTimeToBuyAndSellAStockII testB = new BestTimeToBuyAndSellAStockII();
        System.out.println(testB.maxProfit(test));
    }

}
