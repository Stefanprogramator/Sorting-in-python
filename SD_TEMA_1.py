import random
import copy
from datetime import datetime


# BubbleSort ------------------------------
def bubble_sort(v):
    for i in range(len(v)):
        for j in range(len(v)-i-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
    return v


# CountSort ------------------------------
def count_sort(v):
    count = [0 for _ in range(max(v)+1)]
    srt = []
    for i in v:
        count[i] += 1
    for i in range(max(v)+1):
        for j in range(count[i]):
            srt.append(i)
    return srt


# MergeSort ------------------------------
def merge_sort(v):
    if len(v) <= 1:
        return v
    else:
        mid = len(v) // 2
        l = merge_sort(v[:mid])
        r = merge_sort(v[mid:])
        return merge(l, r)


def merge(l, r):
    i = j = 0
    merged = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1

    merged.extend(l[i:])
    merged.extend(r[j:])

    return merged


# QuickSort ------------------------------
def median_of_medians(v):
    if len(v) <= 5:
        return sorted(v)[len(v)//2]
    else:
        subliste = [sorted(v)[i:i+5] for i in range(0, len(v), 5)]
        mediane = [s1[len(s1)//2] for s1 in subliste]
        return median_of_medians(mediane)


def median_of_three_random(v):
    y = [random.choice(v) for _ in range(3)]
    med = sorted(y)[1]
    return med


def quick_sort(v):

    less = []
    equal = []
    greater = []

    if len(v) > 1:

        pivot = median_of_three_random(v)

        for el in v:
            if el < pivot:
                less.append(el)
            if el == pivot:
                equal.append(el)
            if el > pivot:
                greater.append(el)

        return quick_sort(less) + equal + quick_sort(greater)

    else:
        return v


# RadixSort ------------------------------
def count_sort_for_radix(arr, max_value, get_index):
    counts = [0] * max_value

    for a in arr:
        counts[get_index(a)] += 1

    for i, c in enumerate(counts):
        if i == 0:
            continue
        else:
            counts[i] += counts[i - 1]

    for i, c in enumerate(counts[:-1]):
        if i == 0:
            counts[i] = 0
        counts[i + 1] = c

    ret = [None] * len(arr)

    for a in arr:
        index = counts[get_index(a)]
        ret[index] = a
        counts[get_index(a)] += 1

    return ret


def digit(n, d):
    for i in range(d-1):
        n //= 10
    return n % 10


def nr_cifre(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i


def radix_sort(v, max_value):
    num_digits = nr_cifre(max_value)

    for d in range(num_digits):
        v = count_sort_for_radix(v, max_value, lambda a: digit(a, d+1))
    return v


# Verificare --------------------------------

def verify(v, sortat, n):

    if len(sortat) == n:
        for _ in range(n - 1):
            if sortat[_] > sortat[_ + 1]:
                return False
    else:
        return False

    if sortat != sorted(v):
        return False

    return True


lines = int(input("Numarul de teste este: "))
afile = open("teste.txt", "w")

for j in range(lines):
    line = []
    for i in range(int(input('Cate numere are testul? : '))):
        line.append(random.randint(1, 1000))
    for x in line:
        afile.write(str(x) + " ")
    afile.write('\n')


afile.close()

teste = open("teste.txt")

for test in teste:
    test1 = [int(i) for i in test.split()]
    n = len(test1)

    copie = copy.deepcopy(test1)
    start = datetime.now()
    vector = bubble_sort(copie)
    start = datetime.now() - start
    if verify(test1, vector, n) is True:
        print("BubbleSort a sortat cu succes testul cu ", n, " timpul necesar fiind ", start)

    copie = copy.deepcopy(test1)
    start = datetime.now()
    vector = count_sort(copie)
    start = datetime.now() - start
    if verify(test1, vector, n) is True:
        print("CountSort a sortat cu ", n, " timpul necesar fiind ", start)

    copie = copy.deepcopy(test1)
    start = datetime.now()
    vector = merge_sort(copie)
    start = datetime.now() - start
    if verify(test1, vector, n) is True:
        print("MergeSort a sortat cu ", n, " timpul necesar fiind ", start)

    copie = copy.deepcopy(test1)
    start = datetime.now()
    vector = quick_sort(copie)
    start = datetime.now() - start
    if verify(test1, vector, n) is True:
        print("QuickSort a sortat cu ", n, " timpul necesar fiind ", start)

    copie = copy.deepcopy(test1)
    start = datetime.now()
    vector = radix_sort(copie, max(copie))
    start = datetime.now() - start
    if verify(test1, vector, n) is True:
        print("RadixSort a sortat cu cu ", n, " timpul necesar fiind ", start)

    copie = copy.deepcopy(test1)
    start = datetime.now()
    vector = sorted(copie)
    start = datetime.now() - start
    if verify(test1, vector, n) is True:
        print("Sortarea nativa a sortat cu cu ", n, " timpul necesar fiind ", start)
