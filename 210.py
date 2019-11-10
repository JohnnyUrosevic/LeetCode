import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        eligible_classes = []
        number_of_prereqs = collections.defaultdict(int)
        adjacency_list = collections.defaultdict(list)
        order = []

        for edge in prerequisites:
            number_of_prereqs[edge[0]] += 1
            adjacency_list[edge[1]].append(edge[0])
        
        for i in range(numCourses):
            if number_of_prereqs[i] == 0:
                eligible_classes.append(i)

        taken = 0
        while eligible_classes:
            taken += 1
            class_to_take = eligible_classes[-1]
            order.append(class_to_take)
            eligible_classes.pop()

            for subsequent in adjacency_list[class_to_take]:
                number_of_prereqs[subsequent] -= 1
                if number_of_prereqs[subsequent] == 0:
                    eligible_classes.append(subsequent)
        
        if taken != numCourses:
            return []
        
        return order
