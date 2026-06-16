class Solution {
    public boolean isAnagram(String s, String t) {
        // create two hashmaps for s and t for frequency count
        // before that u can check if lengths are the same 

        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> countT = new HashMap<>();
        HashMap<Character, Integer> countS = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            countS.put(s.charAt(i), countS.getOrDefault(s.charAt(i), 0) + 1);
            countT.put(t.charAt(i), countT.getOrDefault(t.charAt(i), 0) + 1);
        }

        if (countS.equals(countT)) {
            return true;
        }
        return false;
    }
}
