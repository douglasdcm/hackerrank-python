from operator import mod
import pytest

def get_next_mult_of_five(grade):
    i = 0
    next_ = grade
    while i <= 5:
        if mod(next_, 5) == 0:
            return next_
        next_ += 1
        i += 1

def gradingStudents(grades):
    result = []
    min_grade = 38

    for grade in grades:
        if grade < min_grade:
            result.append(grade)
            continue

        next_ = get_next_mult_of_five(grade)
        if (next_ - grade) < 3:
            result.append(next_)
        else:
            result.append(grade)
            
    print(result)
    return result

@pytest.mark.parametrize(
    "grades,exp", [
        ([84, 29, 57], [85, 29, 57]),
        ([73, 67, 38, 33], [75, 67, 40, 33]),
        ([0, 100], [0, 100]),
    ],
)
def test_gradingStudents(grades, exp):
    assert gradingStudents(grades) == exp


def get_less_important(k, contests):
    important = get_only_important(contests)
    important.sort()
    return important[0:k]

def get_more_important(contests):
    contests.sort(reverse=True)
    return contests

def get_only_important(contests):
    important = []
    for c in contests:
        reduce_ = c[0] * c[1]
        if reduce_ > 0:
            important.append(c)
    return important

def luckBalance(k, contests):
    result = None
    total_luck = 0
    to_win = 0

    important = get_only_important(contests)
    more_important = get_more_important(important)
    qtde_more_important = len(more_important)
    if qtde_more_important > k:
        to_win = qtde_more_important - k

    less_important = get_less_important(to_win, contests)

    for c in contests:
        if c in less_important:
            total_luck -= c[0]
        else:
            total_luck += c[0]

    result = total_luck
    print(result)
    return result

@pytest.mark.parametrize(
    "k,contests,exp", [
        (2, [[5,1],[1,1],[4,0]], 10),        
        (1, [[5,1],[1,1],[4,0]], 8),
        (3, [[5,1],[2,1],[1,1],[8,1],[10,0],[5,0]], 29),
        (5, [[13,1],[10,1],[9,1],[8,1],[13,1],[12,1],[18,1],[13,1],], 42),
        (8, [[13,0],[10,0],[9,0],[8,0],[13,0],[12,0],[18,0],[13,0],], 96),
        (5, [[13,0],[10,0],[9,0],[8,0],[13,0],[12,0],[18,0],[13,0],], 96),
        (0, [[13,0],[10,0],[9,0],[8,0],[13,0],[12,0],[18,0],[13,0],], 96),
        (0, [[1,1],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],], 6),
        (1, [[1,1],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],], 8),
        (1, [[2,1],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],], 9),
        (1, [[2,1],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[2,0],], 10),
        (3, [[1,1],[1,1],[1,1],], 3),
        (0, [[1,1],[1,1],[1,1],], -3),
        (1, [[0,1],[0,1],[0,1],], 0),
        (4, [[1,1],[1,1],[1,1],], 3),
        (4, [[1,0],[1,0],[1,0],], 3),
        (0, [[1,1],], -1),
        (1, [[1,1],], 1),
        (2, [[1,1],], 1),
        (0, [[9709,1],
            [9704,1],
            [9080,1],
            [9060,1],
            [9467,1],
            [9847,1],
            [9590,1],
            [9225,1],
            [9304,1],
            [9527,1],
            [9329,1],
            [9962,1],
            [9928,1],
            [9525,1],
            [9491,1],
            [9993,1],
            [9829,1],
            [9153,1],
            [9936,1],
            [9899,1],
            [9312,1],
            [9862,1],
            [9610,1],
            [9502,1],
            [9522,1],
            [9359,1],
            [9617,1],
            [9431,1],
            [9757,1],
            [9292,1],
            [9875,1],
            [9041,1],
            [9626,1],
            [9656,1],
            [9893,1],
            [9442,1],
            [9369,1],
            [9282,1],
            [9117,1],
            [9245,1],
            [9841,1],
            [9715,1],
            [9778,1],
            [9150,1],
            [9738,1],
            [9699,1],
            [9642,1],
            [9517,1],
            [9407,1],
            [9675,1],
            [9918,1],
            [9031,1],
            [9369,1],
            [9935,1],
            [9868,1],
            [9934,1],
            [9660,1],
            [9931,1],
            [9273,1],
            [9168,1],
            [9404,1],
            [9017,1],
            [9288,1],
            [9532,1],
            [9700,1],
            [9291,1],
            [9126,1],
            [9782,1],
            [9545,1],
            [9076,1],
            [9346,1],
            [9018,1],
            [9732,1],
            [9032,1],
            [9992,1],
            [9630,1],
            [9952,1],
            [9885,1],
            [9328,1],
            [9419,1],
            [9705,1],
            [9611,1],
            [9440,1],
            [9907,1],
            [9303,1],
            [9449,1],
            [9876,1],
            [9335,1],
            [9723,1],
            [9698,1],
            [9823,1],
            [9070,1],
            [9258,1],
            [9102,1],
            [9370,1],
            [9788,1],
            [9725,1],
            [9811,1],
            [9474,1],
            [9602,1]],-953782)
    ],
)
def test_luckBalance(k, contests, exp):
    assert luckBalance(k, contests) == exp

def is_sorted(s):
    new_s = sort_string(s)
    return s == new_s

def test_is_sorted():
    s1 = 'abde'
    s2 = 'bace'
    assert is_sorted(s1) is True
    assert is_sorted(s2) is False


def sort_string(s):
    alpha = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]  

    arr = []
    for c in s:
        arr.append(alpha.index(c))
    arr.sort()   
    return ''.join([alpha[c] for c in arr])

def test_sort_string():
      
    exp = "acde"
    s = "cdea"
    assert sort_string(s) == exp


def gridChallenge(grid):
    result = "NO"
    arr = []
    for s in grid:
        arr.append(sort_string(s))

    brr = []
    for i in range(len(arr)):
        col_str = ""
        for j in range(len(arr[0])):
            col_str += arr[j][i]
        brr.append(col_str)

    for s in brr:
        if is_sorted(s):
            result = "YES"
        else:
            result = "NO"
            break

    print(result)
    return result

@pytest.mark.parametrize(
    "input,exp", [
        (['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'], "YES"),
        (['abc', 'ade', 'efg'], "YES"),
        (['abc', 'wxy', 'efg'], "NO"),
    ],
)
def test_gridChallenge(input, exp):
    assert gridChallenge(input) == exp

def timeConversion(s):

    result = None
    base = 12
    hour, min_, sec = s.replace("PM", "").replace("AM", "").split(":")
    hour = int(hour)
    if hour == 12:
        hour = 0
    if "PM" in s:
        result = f"{base + hour}:{min_}:{sec}"

    if "AM" in s:
        result = f"0{hour}:{min_}:{sec}"

    print(result)
    return result

@pytest.mark.parametrize(
    "input,exp", [
        ("07:05:45PM", "19:05:45"),
        ("07:05:45AM", "07:05:45"),
        ("12:00:00AM", "00:00:00"),
        ("12:01:00AM", "00:01:00"),
        ("12:00:00PM", "12:00:00"),
        ("12:01:00PM", "12:01:00"),
    ],
)
def test_timeConversion(input, exp):
    assert timeConversion(input) == exp

def birthdayCakeCandles(candles):
    # Write your code here

    tallest = candles[0]
    for n in candles:
        if tallest < n:
            tallest = n

    count = 0
    for n in candles:
        if n == tallest:
            count += 1
    result = f'{count}'
    print (result)
    return result

@pytest.mark.parametrize(
    "input,exp", [
        ([3, 2, 1, 3], "2"),
    ],
)
def test_birthdayCakeCandles(input, exp):
    assert birthdayCakeCandles(input) == exp

def miniMaxSum(arr):
    outcome = []
    for i in range(len(arr)):
        sum_ = 0
        for j in range(len(arr)):
            if i != j:
                sum_ += arr[j]
        outcome.append(sum_)

    min_ = outcome[0]
    for i in range(len(outcome)):
        n = outcome[i]
        if n < min_:
            min_ = n

    max_ = outcome[0]
    for i in range(len(outcome)):
        n = outcome[i]
        if max_ < n:
            max_ = n

    result = f"{min_} {max_}"
    print(result)
    return result

@pytest.mark.parametrize(
    "input,exp", [
        ([1,3,5,7,9], "16 24"),
        ([1,2,3,4,5], "10 14"),
    ],
)
def test_miniMaxSum(input, exp):
    assert miniMaxSum(input) == exp

def staircase(n):
    # Write your code here
    outcome = ""
    for i in range(n):
        outcome += "{}#{}".format(" " * (n-1 - i), "#" * i)
        if i < n-1:
            outcome += "\n"
    print(outcome)
    return outcome

@pytest.mark.parametrize(
    "input,exp", [
        (6, """     #
    ##
   ###
  ####
 #####
######"""),
    (1, "#"),
    (2, " #\n##"),
    ],
)
def test_staircase(input, exp):
    assert staircase(input) == exp

def plusMinus(arr):
    decimal = 6
    size = len(arr)
    negative = len([n for n in arr if n < 0])
    positive = len([n for n in arr if n > 0])
    zero = len([n for n in arr if n == 0])
    outcome = [round(positive/size, decimal),round(negative/size, decimal),round(zero/size, decimal)]
    print (outcome[0])
    print (outcome[1])
    print (outcome[2])
    return outcome


@pytest.mark.parametrize(
    "arr,exp", [
        ([-4, 3, -9, 0, 4, 1], [0.500000,0.333333,0.166667]),
        ([1, 1, 0, -1, -1], [0.400000,0.400000,0.200000]),
    ],
)
def test_plauMinus(arr,exp):
    assert plusMinus(arr) == exp

def calc_d2(arr):
    d = 0
    i = -len(arr[0]) + 1
    for line in arr:
        j = 0
        for v in line:
            print(-i,j)
            if -i == j:
                d += v
            j += 1
        i += 1
    return d

def calc_d1(arr):
    d1 = 0
    i = 0
    for line in arr:
        j = 0
        for v in line:
            if i == j:
                d1 += v
            j += 1
        i += 1
    return d1

def diagonalDifference(arr):
    # Write your code here    
    return abs(calc_d1(arr) - calc_d2(arr))

def test_calc_d2():
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9],
    ]
    exp = 17
    act = calc_d2(arr)
    assert act == exp

def test_calc_d1():
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9],
    ]
    exp = 15
    act = calc_d1(arr)
    assert act == exp

def test_diagonalDifference():
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9],
    ]
    exp = 2
    act = diagonalDifference(arr)
    assert act == exp


def aVeryBigSum(ar):
    # Write your code here
    result = 0
    for el in ar:
        result += el
    return result

def test_aVeryBigSum():
    arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    exp = 5000000015
    act = aVeryBigSum(arr)
    assert act== exp

def compareTriplets(a, b):
    # Write your code here
    result = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            result[0] += 1
        if a[i] < b[i]:
            result[1] += 1
    return result

@pytest.mark.parametrize(
    "a,b,exp", [
        ([1, 2, 3], [3, 2, 1], [1,1]),
        ([17, 28, 30], [99, 16, 8], [2,1]),
        ([5, 6, 7], [3, 6, 10], [1,1]),
    ],
)
def test_compareTriplets(a, b, exp):
    # a = [1, 2, 3]
    # b = [3, 2, 1]
    # exp = [1,1]
    act = compareTriplets(a,b)
    assert act == exp

def simpleArraySum(ar):
    # Write your code here
    result = 0
    for el in ar:
        result += el
    return result

def test_simple_arr_sum():
    exp = 31
    arr = [1, 2, 3, 4, 10, 11]
    act = simpleArraySum(arr)
    assert act == exp