class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create two frequency dictionaries for ransomNote and magazine
        # loop through ransomNote and check if letter is in magazine and if frequencies match
        # if they don't return false
        # in end return true

        magazineFrequency = defaultdict(int)
        noteFrequency = defaultdict(int)

        for c in ransomNote:
            noteFrequency[c] += 1

        for j in magazine:
            magazineFrequency[j] += 1

        #print(noteFrequency)
        #print(magazineFrequency)

        for key, value in noteFrequency.items():
            if key not in magazineFrequency:
                return False
            if magazineFrequency[key] < value:
                return False

        return True