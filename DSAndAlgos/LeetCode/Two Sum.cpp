#include <iostream>
#include <vector>
#include <algorithm>

class Solution {

    // Put all values into a hash map to lookup possible results immediately

    // While iterating over the vector, check if we already have a matching solution there and return the result immediately 

    // If yes, we have found the complement and return the result

    // If not we store the value and the location in the hashmap

public:

    std::unordered_map<int, int> hashMap= {};
    int pointerleft = 0;

    vector<int> twoSum(vector<int>& nums, int target) {

        for(int pointer = 0; pointer < nums.size(); pointer++) {
            
            auto it = hashMap.find(target - nums.at(pointer));
            if(it != hashMap.end()) {
                return std::vector<int>{hashMap[target - nums.at(pointer)], pointer};
            } else {
                hashMap[nums.at(pointer)] = pointer;
            }
        }
        return std::vector<int>{pointerleft};
    }
};
