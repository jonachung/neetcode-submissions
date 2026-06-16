class Solution {
    public boolean hasDuplicate(int[] nums) {
        // put numbers in set. If number already present in set, return true. In end, returl false
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (set.contains(num)) {
                return true;
            }
            set.add(num);
        }
        return false;
    }
}