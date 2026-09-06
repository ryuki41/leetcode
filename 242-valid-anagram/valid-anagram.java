class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> s_count = new HashMap<>();
        Map<Character, Integer> t_count = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            int tmp_s_count = s_count.getOrDefault(s.charAt(i), 0);
            s_count.put(s.charAt(i), tmp_s_count+1);
            int tmp_t_count = t_count.getOrDefault(t.charAt(i), 0);
            t_count.put(t.charAt(i), tmp_t_count+1);
        }

        return s_count.equals(t_count);
    }
}