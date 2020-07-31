import requests
from bs4 import BeautifulSoup


class University:
    def __init__(self, name, major, lowest_mark):
        self.name = name
        self.major = major()
        self.lowest_mark = lowest_mark


class Major:
    def __init__(self, major_name, lowest_mark):
        self.major_name = major_name
        self.lowest_mark = lowest_mark



def college_page(rootpage):
    r = requests.get(rootpage)
    r.encoding = 'GBK'
    soup = BeautifulSoup(r.text)
    count1 = count2 = 0
    results = [[]]
    results.append([])
    results.append([])

    for link in soup.find_all('a'):
        if count1 % 3 == 0:
            results[0].append(link.get_text())
            results[2].append('https://www.nm.zsks.cn'+link.get('href'))
        count1 += 1

    for mark in soup.find_all('td', {'class': "report1_4_6"}):
        if count2 % 7 == 3:
            results[1].append(int(mark.get_text()))
        count2 += 1

    # print("共爬取到", len(results[1]), "所一本院校")
    # for i in range(305):
    #     print('院校',results[0][i], '分数线', results[1][i], '链接',results[2][i])

    return results


def majors(url):
    r = requests.get(url)
    r.encoding = 'GBK'
    soup = BeautifulSoup(r.text)
    count1 = count2 = 0
    results = [[]]
    results.append([])

    for mark in soup.find_all('td', {'class': "report1_4_3"}):
        if count2 % 4 == 1:
            results[1].append(int(mark.get_text()))
        count2 += 1

    for name in soup.find_all('td', {'class': "report1_3_1"}):
        if count1 >= 5 and name is not None:
            results[0].append(name.get_text())
        count1 += 1

    print(results[0][0], results[1][0])
    return(results)


def input_estimation():
    low = int(input("输入分数下限"))
    high = int(input("输入分数上限"))
    return (low, high)


def filter(low, high, colleges):
    for i in range (305):
        if colleges[1][i] <= high:
            print(colleges[0][i])
            results = majors(colleges[2][i])
            for i in range(len(results[0])):
                print(results[0][i], results[1][i])
                if results[1][i] >= low and results[1][i] <= high:
                    print(results[0][i], "分数线",results[1][i])



rootpage = 'https://www.nm.zsks.cn/zy_31_2019/B_11.html'

# low, high = input_estimation()
#colleges = college_page(rootpage)
#majors('https://www.nm.zsks.cn/zy_31_2019/3_B_294_11.html')

