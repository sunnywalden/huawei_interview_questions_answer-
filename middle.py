#!/usr/bin/python3

'''
1.字符个数统计
描述:
编写一个函数，计算字符串中含有的不同字符的个数。字符在 ASCII 码范围内( 0~127 ，包括 0 和 127 )，换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
例如，对于字符串 abaca 而言，有 a、b、c 三种不同的字符，因此输出 3 。

数据范围：
1≤n≤500
输入描述：
输入一行没有空格的字符串。

输出描述：
输出 输入字符串 中范围在(0~127，包括0和127)字符的种数。

示例1
    输入：
        abc

    输出：
        3

示例2
    输入：
        aaa

    输出：
        1
'''


def count_char(s: str):
    chars = set()

    for i in range(len(s)):
        c = s[i]

        if 0 + ord('a') <= ord(c) <= 127 + ord('a'):
            chars.add(c)

    return len(chars)


'''
2.截取字符串
描述
输入一个字符串和一个整数 k ，截取字符串的前k个字符并输出

数据范围：字符串长度满足 
1≤n≤1000  ， 
 
1≤k≤n 
输入描述：
1.输入待截取的字符串

2.输入一个正整数k，代表截取的长度

输出描述：
截取后的字符串

示例1
输入：
abABCcDEF
6

输出：
abABCc

示例2
输入：
bdxPKBhih
6

输出：
bdxPKB
'''


def str_x(s: str, n: int):
    res = ""
    for i in range(len(s)):
        if i < n:
            res += s[i]

    return res


'''
3.查找组成一个偶数最接近的两个素数
描述
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。

数据范围：输入的数据满足 
4≤n≤1000 
输入描述：
输入一个大于2的偶数

输出描述：
从小到大输出两个素数

示例1
输入：
20

输出：
7
13

示例2
输入：
4

输出：
2
2
'''


def find_closer_prime_num(n: int):
    def check_sushu(n: int):
        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    # n = int(input())

    # minus_dict = {}
    a, b = 0, 0
    min_minus = n
    for i in range(1, n):
        if not check_sushu(i):
            continue

        minus = n - i
        if not check_sushu(minus):
            continue

        if minus >= i:
            minus_i = minus - i
        else:
            minus_i = i - minus
        # print("i={}, minus={},minus_i={}".format(i, minus, minus_i))
        # minus_dict[minus_i] = [i, minus]

        if minus_i < min_minus:
            min_minus = minus_i
            a, b = i, minus
            if a > b:
                a, b = b, a
            # print("min_minus={}, minus_i={},\n a={},b={}".format(min_minus, minus_i, a , b))

    return a, b


'''
4.统计字符
描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。

数据范围：输入的字符串长度满足 
1≤n≤1000 

输入描述：
输入一行字符串，可以有空格

输出描述：
统计其中英文字符，空格字符，数字字符，其他字符的个数

示例1
输入：
1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\][
输出：
26
3
10
12

'''


def count_char(s: str):
    # s = input()

    alpha_num, space_num, digit_num, others_num = 0, 0, 0, 0
    for i in range(len(s)):
        c = s[i]
        if c.isdigit():
            digit_num += 1
        elif c.isalpha():
            alpha_num += 1
        elif c == " ":
            space_num += 1
        else:
            others_num += 1

    print("{}\n{}\n{}\n{}".format(alpha_num, space_num, digit_num, others_num))
    return alpha_num, space_num, digit_num, others_num


if __name__ == '__main__':
    # print(str_x('abABCcDEF', 6))
    # print(str_x('bdxPKBhih', 6))

    # print(find_closer_prime_num(20))
    # print(find_closer_prime_num(4))

    # print(count_char('1qazxsw23 edcvfr45tgbn hy67uj \nm,ki89ol.\\/;p0-=\\]['))
    pass

