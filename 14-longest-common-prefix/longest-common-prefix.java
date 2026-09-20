class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1) {
            return strs[0];
        }

        int min_length = 200;
        for (String str: strs) {
            if (str.length() < min_length) {
                min_length = str.length();
            }
        }

        String common_str = "";
        for(int i = 0; i < min_length; i++) {
            char tmp_char = strs[0].charAt(i); 

            for (int j = 1; j < strs.length; j++) {
                if (strs[j].charAt(i) != tmp_char) {
                    return common_str;
                }
            }
            common_str += tmp_char;
        }

        return common_str;
    }
}