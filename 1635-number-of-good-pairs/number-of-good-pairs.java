class Solution {
    public int numIdenticalPairs(int[] nums) {
        int total_count = 0;

        Map<Integer, Integer> num_map = new HashMap<>();

        for (int num: nums) {
            int count = num_map.getOrDefault(num, 0);

            total_count += count;

            num_map.put(num, count + 1);
        }
        
        return total_count;
    }
}