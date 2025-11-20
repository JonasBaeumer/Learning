#include <iostream>
#include <string>

class Solution {

    // Go through each string in the vector

    // First string is the longest substring possible

    // Check for each new string if and how many chars of this substring are contained at the beginning

    // If the first char is not similar we can terminate

    // Otherwise the substring can only be as long as the first string or will gradually decrease

    // Worst case all strings in the array are the same

public:
    string longestCommonPrefix(vector<string>& strs){

        if(strs.empty()) return "";

        string current_substring{strs[0]};

        for(auto i = 1; i<size(strs); ++i) {
            for(auto j = 0; j<size(current_substring); ++j) {
                if(strs[i][j] != current_substring[j]) {
                    if(j==0) { 
                        return ""; 
                    } else {
                        current_substring = strs[i].substr(0, j);
                        break;
                    }
                }
            }
        }
        return current_substring;
    }
};
