class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda x: x[1])
        count = 0
        while courses:
            count += 1
            current_course = courses[0]
            courses = [course for course in courses if course[0] > current_course[1]]

        return count