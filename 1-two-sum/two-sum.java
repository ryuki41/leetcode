class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> num_map = new HashMap<>();
        
        int[] res = new int[2];
        
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int target_num = target - num;

            if (num_map.containsKey(target_num)) {
                res[0] = num_map.get(target_num);
                res[1] = i;
                break;
            }

            num_map.put(num, i);
        }

        return res;
    }
}