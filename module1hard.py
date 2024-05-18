grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

n1 = sum(grades[0])/len(grades[0])
n2 = sum(grades[1])/len(grades[1])
n3 = sum(grades[2])/len(grades[2])
n4 = sum(grades[3])/len(grades[3])
n5 = sum(grades[4])/len(grades[4])

list_ = list(students)
res = list_.sort()

para = ((list_[0], n1), (list_[1], n2), (list_[2], n3), (list_[3], n4), (list_[4], n5))
ocenki = dict(para)
print(ocenki)
