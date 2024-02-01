class Solution {
public:

    // Have a loop and a pointer for needle

    // Loop over the string when the first char matches with the first letter of the needle, increase index 

    // If second letter does not match set counter back two 0 and compare again

    int strStr(string h, string s) {
        int m=h.size(), n=s.size(), i=0, j=0, k=0;
        if(m<n) return -1;
        while(i<m && j<n) {
            if(h[i]==s[j]) {i++; j++;}
            else {i=k+1; j=0; k=i;}
        }
        if(j==n) return k;
        else return -1;
    }
};
