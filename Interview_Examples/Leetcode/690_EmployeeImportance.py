"""
You are given a data structure of employee information,
which includes the employee's unique id, their importance value and their direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3.
They have importance value 15, 10 and 5, respectively.
Then employee 1 has a data structure like [1, 15, [2]],
and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []].

Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id,
you need to return the total importance value of this employee and all their subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.


Note:

One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.

"""

"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):

        #we create a dictioanry/hashmap of the eployees given in the funciton
        dictionary_of_employees = {}

        #for each given empoyess on the list, as assign them by ID, and put the data in the element
        for employee in employees:
            dictionary_of_employees[employee.id] = employee

        #answer for the according employee is :
        answer = 0
        #we make a queue, list, which will be taking the first (0) element from the list, and then assigning
        #the
        queue = [id]
        #BFS  -  we get the employee, adds the importance to the answer, and then we add the subemployees , until queue is empty
        while queue:
            current_employee = queue.pop(0)
            answer += dictionary_of_employees[current_employee].importance
            queue += dictionary_of_employees[current_employee].subordinates
        return answer

# solution 2
"""
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        all_employees = {}
        for employee in employees:
            all_employees[employee.id] = employee

        def get_importance(id):
            employee = all_employees[id]
            total = employee.importance
            for id_val in employee.subordinates:
                total += get_importance(id_val)
            return total

        return get_importance(id) 
"""

if __name__ == "__main__":

    employee2 = Employee(2, 3, [])
    employee1 = Employee(1, 5, [2, 3])
    employee3 = Employee(3, 3, [])

    solution = Solution()
    answer = solution.getImportance([employee1, employee2, employee3], 1)
    print(answer)
