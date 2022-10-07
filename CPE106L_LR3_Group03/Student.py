"""
File: student.py
Resources to manage a student's name and test scores.
"""


class Student(object):
    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)


    def getName(self):
        """Returns the student's name."""
        return self.name


    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score


    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]


    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)


    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)


    def __str__(self):
        """ReSturns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + \
            " ".join(map(str, self.scores))


    # Write method definitions here
    def __eq__(self, other):
        """Returns true if student names are equal."""
        return self.name==other.name

    def __lt__(self, other):
        """Returns for a<b name of a is lexographical before b."""
        return self.name<other.name

    def __ge__(self, other):
        """Returns for a>b name of a is lexographical before b."""
        return self.name>other.name


def main():
    """A simple test."""
    student = Student("Ken", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)
    student2 = Student("Ken", 6)
    print(student == student2)  
    student3 = Student("John", 6)
    print(student2 > student3) 
    print(student2 < student3)  

if __name__ == "__main__":
    main()