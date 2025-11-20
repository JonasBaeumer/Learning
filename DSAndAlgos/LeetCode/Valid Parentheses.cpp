class Solution {

public:

    std::vector<char> chars;

    bool isValid(string s) {
        for(const auto& character: s) {
            if (character == '{' || character == '[' || character == '(' ) {
                chars.push_back(character);
            } else {
                if(chars.size() > 0) {
                    if(chars.back() == '{' && character == '}') {
                        chars.pop_back();
                    } else if(chars.back() == '(' && character == ')') {
                        chars.pop_back();
                    } else if(chars.back() == '[' && character == ']') {
                        chars.pop_back();
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        if(chars.size() > 0) {
            return false;
        } 
        return true;
    }
};
