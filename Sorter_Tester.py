import random
from time import perf_counter
g = open("Testari_in", "r")
T = int(g.readline())
Data = [l.strip().split() for l in g.readlines()]
i = 0
Bubble_Time = []
Count_Time = []
Radix_Time = []
Merge_Time = []
Quick_Time = []
Native_Time = []
g.close()
def sort_checker(LS, i, cod):
    if LS != sorted(LS):
        print("Ceva nu este in regula in timpul testului {} la sortarea {}".format(i, cod))
while i < T:
    N = int(Data[i][0])
    Max = int(Data[i][1])
    L = random.choices(range(1, Max + 1), k=N)
    i += 1
    print("Testul {} are {} numere si {} este maximul posibil".format(i, N, Max))
    def Countsort(LS, Max):
        Max += 1
        counter = [0] * Max
        for nr in LS:
            counter[nr] += 1
        k = 0
        for v in range(Max):
            for n in range(counter[v]):
                LS[k] = v
                k += 1
        return LS
    def Radixsort(LS):
        Max = max(LS)
        n = 1
        while Max // n >= 1:
            k = len(LS)
            counter = [0] * 10
            LS2 = [0] * k
            for v in range(0, k):
                counter[int((LS[v] / n) % 10)] += 1
            for v in range(1, 10):
                counter[v] += counter[v - 1]
            k -= 1
            while k >= 0:
                LS2[counter[int((LS[k] / n) % 10)] - 1] = LS[k]
                counter[int((LS[k] / n) % 10)] -= 1
                k -= 1
            n *= 10
            LS = LS2
        return LS
    def Mergesort(LS):
        if len(LS) > 1:
            m = len(LS) // 2
            s = LS[:m]
            d = LS[m:]
            Mergesort(s)
            Mergesort(d)
            cs = cd = c = 0
            while cs < len(s) and cd < len(d):
                if s[cs] < d[cd]:
                    LS[c] = s[cs]
                    cs += 1
                else:
                    LS[c] = d[cd]
                    cd += 1
                c += 1
            while cs < len(s):
                LS[c] = s[cs]
                cs += 1
                c += 1
            while cd < len(d):
                LS[c] = d[cd]
                cd += 1
                c += 1
        return LS
    def Quicksort(LS):
        if len(LS) <= 1:
            return LS
        pivot = LS[len(LS)//2]
        s = [x for x in LS if x < pivot]
        m = [x for x in LS if x == pivot]
        d = [x for x in LS if x > pivot]
        return Quicksort(s) + m + Quicksort(d)
    def Bubblesort(LS):
        flag = True
        parcurgeri = 0
        while flag is True:
            flag = False
            for i in range(0, len(LS) - parcurgeri - 1):
                if LS[i] > LS[i + 1]:
                    LS[i], LS[i + 1] = LS[i + 1], LS[i]
                    flag = True
            parcurgeri += 1
        return LS

    cod = "Count"
    L2 = L[:]
    start_time = perf_counter()
    LS = Countsort(L2, Max)
    end_time = perf_counter()
    sort_time = end_time - start_time
    sort_checker(LS, i, cod)
    Count_Time.append(sort_time)

    cod = "Radix"
    L2 = L[:]
    start_time = perf_counter()
    LS = Radixsort(L2)
    end_time = perf_counter()
    sort_time = end_time - start_time
    sort_checker(LS, i, cod)
    Radix_Time.append(sort_time)

    cod = "Merge"
    L2 = L[:]
    start_time = perf_counter()
    LS = Mergesort(L2)
    end_time = perf_counter()
    sort_time = end_time - start_time
    sort_checker(LS, i, cod)
    Merge_Time.append(sort_time)

    cod = "Quick"
    L2 = L[:]
    start_time = perf_counter()
    LS = Quicksort(L2)
    end_time = perf_counter()
    sort_time = end_time - start_time
    sort_checker(LS, i, cod)
    Quick_Time.append(sort_time)

    cod = "Bubble"
    L2 = L[:]
    start_time = perf_counter()
    LS = Bubblesort(L2)
    end_time = perf_counter()
    sort_time = end_time - start_time
    sort_checker(LS, i, cod)
    Bubble_Time.append(sort_time)

    start_time = perf_counter()
    L.sort()
    end_time = perf_counter()
    sort_time = end_time - start_time
    Native_Time.append(sort_time)

g = open("Testari_out", "w")
g.write("Numar Teste: {}\n".format(T))
def write_results(s, L, T):
    g.write("Sortarea {} a avut rezultatele urmatoare: ".format(s))
    i = 0
    j = 1
    while T > j:
        g.write("testul {} - {}, ".format(j, L[i]))
        i += 1
        j += 1
    g.write("testul {} - {}.\n".format(j, L[i]))
write_results("Count Sort", Count_Time, T)
write_results("Radix Sort", Radix_Time, T)
write_results("Merge Sort", Merge_Time, T)
write_results("Quick Sort", Quick_Time, T)
write_results("Bubble Sort", Bubble_Time, T)
write_results("nativa", Native_Time, T)
g.close()
print(Count_Time)
print(Radix_Time)
print(Merge_Time)
print(Quick_Time)
print(Bubble_Time)

