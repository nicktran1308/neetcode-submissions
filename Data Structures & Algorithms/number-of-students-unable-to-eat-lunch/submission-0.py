class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zeros = students.count(0)
        ones = students.count(1)

        for s in sandwiches:
            if s == 0 and zeros > 0:
                zeros -= 1
            elif s == 1 and ones > 0:
                ones -= 1
            else:
                break
        return zeros + ones



# Time: O(n) - students.count 2 times
# Space: O(1) 

        

        
