class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Boolean> num_map = new HashMap<>();

        for (int num: nums) {
            if (num_map.containsKey(num)) {
                return true;
            }
            
            num_map.put(num, true);
        }

        return false;
    }
}