#include <iostream>
#include <unordered_map>

class Solution {

    // Have one pointer

    // Have a key-value map with all roman letters

    // Check if a bigger letter is coming in at n+1

        // If yes deduct the number from the sum

public:

    std::unordered_map<char, int> romanLetters = {
        {'M', 1000},
        {'D', 500},
        {'C', 100},
        {'L', 50},
        {'X', 10},
        {'V', 5},
        {'I', 1}
    };

    int sum = 0;
    size_t pointer = 0;

    int romanToInt(string s) {
        for (; pointer < s.size(); pointer++) {
            auto roman_letter = s.at(pointer);
            if(pointer+1 < s.size()) {
                if(romanLetters[roman_letter] < romanLetters[s.at(pointer+1)]) {
                    sum -= romanLetters[roman_letter];
                    continue;
                }
            }
            sum += romanLetters[roman_letter];
        }
        return sum;
    }
};
