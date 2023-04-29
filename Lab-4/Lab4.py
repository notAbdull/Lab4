# ----- Abdullah alsuhaibani - 439102222-----#
# ----- Program 1 -----#
class Course:

    def __init__(self, cd, ca, co, sn):
        self.Code = cd
        self.Capacity = ca
        self.Core = co
        self.StudentsNo = sn

    def __str__(self):
        return self.Code + ',' + str(self.Capacity) + ','+ str(self.Core) + ',' + str(self.StudentsNo)


# ----- Program 2 -----#
    c = ("439102222.txt")
    import Course

    s1 = course.Course('IS324', 80, True, 78)
    s2 = course.Course('CS111', 180, True, 180)
    s3 = course.Course('IS481', 50, False, 31)
    s4 = course.Course('SE434', 50, False, 39)
    s5 = course.Course('CE443', 50, False, 24)
    s6 = course.Course('CS227', 180, True, 150)
# ----- Program 3 -----#
    Data = [s1, s2, s3, s4, s5, s6]
# ----- Program 4 -----#

    def num_Core(list):
        count = 0

        for c in list:
            if c.Core == True:
                count = count + 1

        return count

    def num_IS_Core(list):
        count = 0

        for c in list:
            if c.Code[0: 2] == 'IS' and c.Core == True:
                count = count + 1

        return count

    def course_Search(list, core, rate):
        for c in list:
            if c.Core == core and ((c.StudentsNo / c.Capacity) * 100) >= rate:
                print(c)
    print("The number of core courses: " + str(num_Core(Data)))

    print("\nThe number of IS courses which are core: " + str(num_IS_Core(Data)))
    print()


    course_Search(Data, False, 70)
# ----- Program 5 -----#
    import logging

    def num_core(list):
        count = 0
        for c in list:
            if c.core:
                count += 1
        return count

    logging.basicConfig(filename='seLog.log', level=logging.DEBUG)

    list = [Course(core=True), Course(core=False), Course(core=True)]
    result = num_core(list)
    logging.debug('Number of core courses: {}'.format(result))

    logging.warning('This is a warning message')
    logging.error('This is an error message')
# ----- Program 6 -----#
    import re

    def buildIndex(Text):
        words = re.findall(r'\b\w+\b', Text)

        word_counts = {}

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        return word_counts

    Text = "KSU is a University in Riyadh , Riyadh is a big city"
    mydict = buildIndex(Text)
    print(mydict)
# ----- Program 7 -----#
    mySet = set([19, 7, 29, 30, 40, 9, 15, 25])

    def find_Last_Three(set):
        e = tuple(sorted(set, reverse=True))
        print(f'{e[len(e) - 1]} , {x[len(e) - 2]} , {e[len(e) - 3]}')

    print(find_Last_Three(mySet))
