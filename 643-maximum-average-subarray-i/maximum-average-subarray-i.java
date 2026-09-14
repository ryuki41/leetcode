class Solution {
    public double findMaxAverage(int[] nums, int k) {
        // maxの初期値を計算
        int max = 0;
        for(int i = 0; i < k; i++) {
            max += nums[i];
        }

        int cur_total = max;
        for(int j = k; j < nums.length; j++) {
            cur_total += nums[j];
            cur_total -= nums[j-k];
            if (cur_total > max) {
                max = cur_total;
            }
        }

        double max_f = max;
        return max_f / k;
    }
}