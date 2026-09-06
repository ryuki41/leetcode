class Solution {
    public int numIdenticalPairs(int[] nums) {
        Map<Integer, Integer> num_map = new HashMap<>();

        int total_count = 0;

        for (int num: nums) {
            int pre_count = num_map.getOrDefault(num, 0);

            total_count += pre_count;

            num_map.put(num, pre_count+1);
        }

        return total_count;
    }
}