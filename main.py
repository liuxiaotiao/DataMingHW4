
import numpy as np


class DTnode:
    def __init__(self):
        self.condition_type
        self.condtion
        self.childrenNode = {}




def Ires(dataset):
    num1 = len(dataset[0]);
    num2 = len(dataset[1]);
    # print(num1, num2)
    num_no_s = 0;
    num_yes_s = 0;
    num_no_b = 0;
    num_yes_b = 0;
    # print(dataset[0])
    for sdata in dataset[0]:
        if sdata[1] == "no":
            num_no_s += 1;
        else:
            num_yes_s += 1;
    for bdata in dataset[1]:
        if bdata[1] == "no":
            num_no_b += 1;
        else:
            num_yes_b += 1;
    # print(num_no_s, num_yes_s, num_no_b, num_yes_b)
    first = 0
    second = 0
    third = 0
    forth = 0
    if (num_no_s != 0) & ((num_no_s + num_yes_s) != 1):
        first = -(num_no_s / (num_no_s + num_yes_s)) * np.log2(num_no_s / (num_no_s + num_yes_s))
    if (num_yes_s != 0) & ((num_no_s + num_yes_s) != 1):
        second = -(num_yes_s / (num_no_s + num_yes_s)) * np.log2(num_yes_s / (num_no_s + num_yes_s))
    if (num_no_b != 0) & ((num_no_b + num_yes_b) != 1):
        third = -(num_no_b / (num_no_b + num_yes_b)) * np.log2(num_no_b / (num_no_b + num_yes_b))
    if (num_yes_b != 0) & ((num_no_b + num_yes_b) != 1):
        forth = -(num_yes_b / (num_no_b + num_yes_b)) * np.log2(num_yes_b / (num_no_b + num_yes_b))
    # print(first, second, third, forth)
    I_res = -num1 * (first + second) / (num1 + num2) - num2 * (third + forth) / (num1 + num2)
    # print(I_res)
    return I_res


def I_res(dataset):
    c = findcategery(dataset)
    num_no = np.zeros(len(c)).tolist()
    num_yes = np.zeros(len(c)).tolist()
    for item in dataset:
        if item[1] == "no":
            for j in range(len(c)):
                if item[0] == c[j]:
                    num_no[j] += 1
        else:
            for j in range(len(c)):
                if item[0] == c[j]:
                    num_yes[j] += 1
    entropy = 0

    for i in range(len(c)):
        if (num_no[i] != 0) & (num_yes[i] != 0):
            entropy += (num_no[i] + num_yes[i]) * ((
                                                           -(num_no[i] * np.log2(
                                                               num_no[i] / (num_no[i] + num_yes[i]))) / (
                                                                   num_yes[i] + num_no[i])) - (
                                                           num_yes[i] * np.log2(
                                                       num_yes[i] / (num_no[i] + num_yes[i]))) / (
                                                           num_yes[i] + num_no[i])) / (
                               sum(num_no) + sum(num_yes))
    # print(num_no, num_yes,entropy)
    return entropy


def findcategery(dataset):
    b = []
    for it in dataset:
        b.append(it[0])
    a = np.unique(b)
    c = []
    for element in a:
        c.append(str(element))
        # print(type(str(element)))
    # print(c)
    return c


def I_play(dataset):
    num_yes = 0
    num_no = 0
    for item in dataset:
        if item[len(item) - 1] == "no":
            num_no += 1
        else:
            num_yes += 1
    p_yes = num_yes / (num_yes + num_no)
    p_no = num_no / (num_yes + num_no)
    return (-p_no * np.log2(p_no)) + (-p_yes * np.log2(p_yes))


def info_gain(dataset):
    Iplay = I_play(dataset)
    num = len(dataset[0])
    entropy = []
    typeset = np.zeros(num - 1).tolist()
    for it in range(num - 1):
        typeset[it] = type(dataset[0][it])
    for i in range(num - 1):
        if isinstance(dataset[0][i], str):
            sI = []
            for item in data:
                m = [item[i], item[num - 1]]
                sI.append(m)
            entropy.append(Iplay - I_res(sI))
        else:
            b = []
            dataset.sort(key=lambda x: x[i], reverse=False)
            for j in range(len(dataset) - 1):
                b.append((dataset[j][i] + dataset[j + 1][i]) / 2)
            searchIres = []
            for n in b:
                first_array = []
                second_array = []
                for item in dataset:
                    m = [item[i], item[num - 1]]
                    if item[i] < n:
                        first_array.append(m)
                    else:
                        second_array.append(m)
                c = [first_array, second_array]
                searchIres.append(Ires(c))
            for y in range(len(searchIres)):
                searchIres[y] += Iplay
            entropy.append(max(searchIres))
    return entropy

# def build_tree():



if __name__ == "__main__":
    data = [['sunny', 85.0, 85.0, 'false', 'no'], ['sunny', 80.0, 90.0, 'true', 'no'],
            ['overcast', 83.0, 86.0, 'false', 'yes'], ['rainy', 70.0, 96.0, 'false', 'yes'],
            ['rainy', 68.0, 80.0, 'false', 'yes'], ['rainy', 65.0, 70.0, 'true', 'no'],
            ['overcast', 64.0, 65.0, 'true', 'yes'], ['sunny', 72.0, 95.0, 'false', 'no'],
            ['sunny', 69.0, 70.0, 'false', 'yes'], ['rainy', 75.0, 80.0, 'false', 'yes'],
            ['sunny', 75.0, 70.0, 'true', 'yes'], ['overcast', 81.0, 75.0, 'false', 'yes'],
            ['overcast', 72.0, 90.0, 'true', 'yes'], ['rainy', 71.0, 91.0, 'true', 'no']]

    # b = []
    # data.sort(key=lambda x: x[1], reverse=False)
    #
    # for i in range(len(data) - 1):
    #     b.append((data[i][1] + data[i + 1][1]) / 2)
    # # print(b)
    #
    # searchIres = []
    # for i in b:
    #     first_array = []
    #     second_array = []
    #     for item in data:
    #         m = [item[1], item[4]]
    #         if item[1] < i:
    #             first_array.append(m)
    #         else:
    #             second_array.append(m)
    #     c = [first_array, second_array]
    #     searchIres.append(Ires(c))
    # print(searchIres)
    #
    #
    #
    # Ip = I_play(data)
    # print(Ip)
    # for i in range(len(searchIres)):
    #     searchIres[i] += 0.940
    # print(searchIres)
    # print(max(searchIres))
    #
    # sI = []

    # for item in data:
    #     m = [item[3], item[4]]
    #     sI.append(m)
    # print(sI)
    # I_res(sI)


    c = info_gain(data)
    print(c)
