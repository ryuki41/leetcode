class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();

        for (int num1: nums1) {
            set1.add(num1);
        }

        for (int num2: nums2) {
            set2.add(num2);
        }

        List<Integer> answer1 = new ArrayList<>();
        List<Integer> answer2 = new ArrayList<>();

        for (int s1: set1) {
            if (!set2.contains(s1)) {
                answer1.add(s1);
            }
        }

        for (int s2: set2) {
            if (!set1.contains(s2)) {
                answer2.add(s2);
            }
        }

        List<List<Integer>> answer = new ArrayList<>();
        answer.add(answer1);
        answer.add(answer2);

        return answer;
    }
}