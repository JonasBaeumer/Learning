class Solution {
public:

    // Loop over the array and replace all numbers that are equal to val with 101

    // When done do std::sort

    int removeElement(vector<int>& nums, int val) {

        int deletion_counter = 0;

        for(int i=0; i<nums.size(); ++i) {
            if(nums[i] == val) {
                nums[i] = 101;
                deletion_counter++;
            }
        }
        //sort
        std::sort(nums.begin(), nums.end());
        return nums.size() - deletion_counter;
    }
};
