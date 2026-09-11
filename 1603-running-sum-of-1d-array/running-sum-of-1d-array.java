class Solution {
    public int[] runningSum(int[] nums) {
        int[] sum_arr = new int[nums.length];

        sum_arr[0] = nums[0];

        for (int i = 1; i < nums.length; i++) {
            sum_arr[i] = sum_arr[i-1] + nums[i];
        }

        return sum_arr;
    }
}