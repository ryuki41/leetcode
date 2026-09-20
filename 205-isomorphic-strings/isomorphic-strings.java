class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Integer> s_map = new HashMap<>();
        Map<Character, Integer> t_map = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            int s_at = s_map.getOrDefault(s.charAt(i), -1);
            int t_at = t_map.getOrDefault(t.charAt(i), -1);

            if (s_at != t_at) {
                return false;
            }

            s_map.put(s.charAt(i), i);
            t_map.put(t.charAt(i), i);
        }

        return true;
    }
}