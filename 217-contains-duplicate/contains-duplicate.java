class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> nums_set= new HashSet<>();

        for (int num: nums) {
            nums_set.add(num);
        }

        return nums_set.size() != nums.length;
    }
}