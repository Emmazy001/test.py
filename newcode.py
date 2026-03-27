lst = [3, 8, 5, 2, 9, 1]

def sort(lst):
    for i in range(len(lst) - 1,0,-1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp


sort(lst)
print(lst)

class Learning():
    def __init__(self):
        self.a=25
        self.b=10








