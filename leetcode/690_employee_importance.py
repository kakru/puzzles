#/usr/bin/env python3
import unittest

# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:  # iterative
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        empl = {e[0]: Employee(*e) for e in employees}
        # empl = {e.id: e for e in employees}  # LeetCode input format
        importance = 0
        q = [id]  # stack of employees to be counted
        while q:
            e = q.pop()
            importance += empl[e].importance
            q.extend(empl[e].subordinates)
        return importance


class Solution:  # revcursive
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        empl = {e[0]: Employee(*e) for e in employees}
        # empl = {e.id: e for e in employees}  # LeetCode input format
        def dfs(id):
            e = empl[id]
            return (e.importance + sum(dfs(id) for id in e.subordinates))
        return dfs(id)


        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
        expected_output = 11
        output = Solution().getImportance(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
