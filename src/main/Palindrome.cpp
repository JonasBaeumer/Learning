#include <iostream>
#include <vector>
#include <string>

class Solution {
// Start at the beginning and at the end of the char list. 

// Have to pointers that got forward and backwards

// On each step: Check if both pointers have the same value

// Then: check if the left pointer is <= the right pointer

// If yes, terminate

public:
    bool isPalindrome(int x) {
        string int_as_string = std::to_string(x);
        std::vector<char> charVector(int_as_string.begin(), int_as_string.end());

        auto leftpointer = charVector.begin();
        auto rightpointer = charVector.end() - 1;

        while(leftpointer < rightpointer) {
            if (*leftpointer != *rightpointer) {
                return false;
            } 
            ++leftpointer;
            --rightpointer;
        }
        return true;
    }
};
