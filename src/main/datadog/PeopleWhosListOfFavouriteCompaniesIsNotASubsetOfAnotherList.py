class Solution:

    def isSubset(self, a, b):
        for x in a:
            if x not in b:
                return False
        return True

    # Runtime: O(n^2 * k)
    # Spacetime: O(n)
    # Solution is too slow -> Must be optimized 
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        equal_list = []

        for i, fav_comp_list in enumerate(favoriteCompanies):
            for j, other_comp_list in enumerate(favoriteCompanies):
                if i != j:
                    fav_comp_list.sort()
                    other_comp_list.sort()
                    # Check if fav_comp_list is subset
                    if self.isSubset(fav_comp_list, other_comp_list):
                        equal_list.append(i)
                        break
        
        print(equal_list)
        
        return [i for i in range(len(favoriteCompanies)) if i not in equal_list]
