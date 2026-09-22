class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] s_array = s.split(" ");

        if (s_array.length != pattern.length()) {
            return false;
        }

        Map<Character, String> char_map = new HashMap<>();
        Map<String, Character> word_map = new HashMap<>();
        
        for (int i=0; i < s_array.length; i++) {
            String word = s_array[i];
            Character c = pattern.charAt(i);

            if (word_map.containsKey(word) && word_map.get(word) != c) {
                return false;
            }

            if (char_map.containsKey(c) && !char_map.get(c).equals(word)) {
                return false;
            }

            word_map.put(word, c);
            char_map.put(c, word);
        }

        return true;
    }
}