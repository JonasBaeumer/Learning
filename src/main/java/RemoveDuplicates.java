public class RemoveDuplicates {

    public int removeDuplicates(int[] nums) {

        int arrayLength = nums.length;
        // will be reduced by 1 everytime a duplicate is found

        for (int i = 0; i < arrayLength; i++) {
            for (int j = i; j < arrayLength; j++) {
                int pointer1 = nums[i];
                int pointer2 = nums[j];
                if (pointer1 == pointer2 && i != j) {
                    arrayLength-=1;
                    // Move the values that come afterwards forward
                    for(int l = j; l<arrayLength; l++) {
                        if(l < nums.length-1) nums[l] = nums[l+1];
                        j -= j;
                        // No need to care about the last element because output can be "cut down"
                        // with last arraylength
                    }
                }
            }
        }
        return arrayLength;
    }

}
