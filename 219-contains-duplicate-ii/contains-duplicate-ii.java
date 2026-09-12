class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> num_map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            
            if (num_map.containsKey(num) && i - num_map.get(num) <= k) {
 
                return true;
            }

            num_map.put(num, i);
        }

        return false;
    }
}