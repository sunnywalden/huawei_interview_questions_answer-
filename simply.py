#! /usr/bin/python3

from functools import reduce

"""
链接：https://leetcode.cn/circle/discuss/niKSMZ/
1.字符串分割
给定一个非空字符串S，其被N个‘-’分隔成N+1的子串，给定正整数K，要求除第一个子串外，其余的子串每K个字符组成新的子串，并用‘-’分隔。对于新组成的每一个子串，如果它含有的小写字母比大写字母多，则将这个子串的所有大写字母转换为小写字母；反之，如果它含有的大写字母比小写字母多，则将这个子串的所有小写字母转换为大写字母；大小写字母的数量相等时，不做转换。
输入描述:
输入为两行，第一行为参数K，第二行为字符串S。
输出描述:
输出转换后的字符串。
示例1
输入
3
12abc-abCABc-4aB@
输出
12abc-abc-ABC-4aB-@
说明
子串为12abc、abCABc、4aB@，第一个子串保留，后面的子串每3个字符一组为abC、ABc、4aB、@，abC中小写字母较多，转换为abc，ABc中大写字母较多，转换为ABC，4aB中大小写字母都为1个，不做转换，@中没有字母，连起来即12abc-abc-ABC-4aB-@
"""


def str_formatter(s: str, ct: int):
    s_list = s.split("-")

    # print("0:{}".format(s_list))
    filtered_list = s_list[1:]
    list_factory = [s_list[0]]

    count = 0
    tmp = ""
    count_lower, count_upper = 0, 0
    # print("0-1:{}".format(filtered_list))
    for i in range(len(filtered_list)):
        s_filter = filtered_list[i]
        # print("1:i={} {}".format(i, s_filter))

        for j in range(len(s_filter)):
            s_son = s_filter[j]

            tmp += s_son
            count += 1

            # print("2:{}".format(s_son))
            # print("2-1:tmp {}, c:{}".format(tmp, s_son))
            # 大小写转换
            if s_son.islower():
                count_lower += 1
            elif s_son.isupper():
                count_upper += 1
            else:
                pass

            # 每ct个字符分组
            if (count % ct == 0 or i == len(filtered_list) - 1 and j == len(s_filter) - 1) and count:
                # 字符分组
                if count_lower > count_upper:
                    # print("lower {}".format(tmp))
                    list_factory.append(tmp.lower())
                elif count_lower < count_upper:
                    # print("upper {}".format(tmp))
                    list_factory.append(tmp.upper())
                else:
                    list_factory.append(tmp)
                count_lower, count_upper = 0, 0
                tmp = ""

    return '-'.join(list_factory)


'''
2.组成最大数
题目描述
给定一个由纯数字组成以字符串表示的数值，现要求字符串中的每个数字最多只能出现2次，超过的需要进行删除；

删除某个重复的数字后，其它数字相对位置保持不变。

如”34533″，数字3重复超过2次，需要删除其中一个3，删除第一个3后获得最大数值”4533″

请返回经过删除操作后的最大的数值，以字符串表示。

输入描述
第一行为一个纯数字组成的字符串，长度范围：[1,100000]

输出描述
输出经过删除操作后的最大的数值

作者：不上岸不改名！
链接：https://www.nowcoder.com/discuss/469505923241811968?sourceSSR=search
来源：牛客网
'''


def indexes_2_int(indexes_list: list[int], index_dict: dict):
    indexes_list.sort()

    tmp = ""
    for i in range(len(indexes_list)):
        index = indexes_list[i]
        c = index_dict[index]
        tmp += c

    cur = int(tmp)

    return cur


def max_num(s: str):
    max_n = 0
    count_dict = {}
    char_dict = {}

    # 取得字符统计信息
    for i in range(len(s) - 1):
        c = s[i]
        char_dict[i] = c

        if c not in count_dict.keys() or count_dict[c] is None:
            count_dict[c] = []

        count_dict[c].append(i)
        print("c={},count_dict={}".format(c, count_dict, ))

    # 选取所有字符，重复2个以上的只取2个
    num_indexes = []
    dumplicate_dict = {}
    for k in count_dict.keys():
        k_indexes = count_dict.get(k)
        if len(k_indexes) > 2:
            for j in range(len(k_indexes)):

                for m in range(j + 1, len(k_indexes)):
                    ins = []
                    if k not in dumplicate_dict.keys():
                        dumplicate_dict[k] = []
                    first = k_indexes[j]
                    second = k_indexes[m]
                    # print("k={},first={},second={}".format(k,first,second))
                    ins.append(first)
                    ins.append(second)
                    dumplicate_dict[k].append(ins)
        else:
            num_indexes.extend(k_indexes)

    # print("num_indexes={},\ndumplicate_dict={}".format(num_indexes, dumplicate_dict))
    ## 组成左右抽样结果
    choices = []
    for k in dumplicate_dict.keys():
        indexes_list = dumplicate_dict.get(k)
        for i in range(len(indexes_list)):
            indexes = indexes_list[i]
            if len(choices) < i + 1:
                indexes.extend(num_indexes)
                choices.append(indexes)
            else:
                choices[i].extend(indexes)
                print("3-3:choices={}".format(choices))

    ## 逐一抽样计算如果
    print("4:choices={}".format(choices))
    for i in range(len(choices)):
        choice = choices[i]
        cur = indexes_2_int(choice, char_dict)
        if cur > max_n:
            max_n = cur

    return str(max_n)


'''
4.字符串序列判定
链接：https://www.nowcoder.com/questionTerminal/5382ff24fbf34a858b15f93e2bd85307
来源：牛客网

给定两个字符串 s和 t ，判断 s是否为 t 的子序列。
你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度n ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：时间复杂度O(n) ，空间复杂度O(n) 

输入描述:
共两行，第一行为字符串s,  第二行为字符串t


字符串t的长度 1<=n<=500000


字符串s的长度 1<=m<=100



输出描述:
输出true或者是false，true表示是s是t的子序列，false表示s不是t的子序列
'''


def is_child_str(s: str, t: str):
    index = 0

    res = 'true'
    index = 0
    for i in range(len(s)):
        for j in range(index, len(t)):
            if s[i] == t[j]:
                if i < len(s) - 1 and j == len(t) - 1:
                    res = "false"
                else:
                    # print("c={},i={},j={}".format(s[i],i,j))
                    index = j + 1
                    break
            else:
                if j == len(t) - 1 and s[i] != t[j]:
                    res = 'false'
                    # print(res)

                elif j == len(t) - 1 and i < len(s) - 1:
                    res = "false"

    return res


'''
3.统计射击比赛成绩
【统计射击比赛成绩】给定一个射击比赛成绩单，包含多个选手若干次射击的成绩分数，请对每个选手按其最高3个分数之和进行降序排名，输出降序排名后的选手ID序列。条件如下：
1、一个选手可以有多个射击成绩的分数，且次序不固定。
2、如果一个选手成绩少于3个，则认为选手的所有成绩无效，排名忽略该选手。
3、如果选手的成绩之和相等，则成绩之和相等的选手按照其ID降序排列。输入描述：

输入
输入第一行，一个整数N，表示该场比赛总共进行了N次射击，产生N个成绩分数（2<=N<=100）。
输入第二行，一个长度为N整数序列，表示参与每次射击的选手ID（0<=ID<=99）。
输入第三行，一个长度为N整数序列，表示参与每次射击的选手对应的成绩（0<=成绩<=100）。

输出
符合题设条件的降序排名后的选手ID序列。

示例输入
13
3,3,7,4,4,4,4,7,7,3,5,5,5
53,80,68,24,39,76,66,16,100,55,53,80,55

示例输出
5,3,7,4

作者：DavidSperk
链接：https://www.nowcoder.com/discuss/353150501363589120?sourceSSR=search
来源：牛客网
'''


def score_statics(ids: list[int], scores: list[int]):
    id_scores_dict = {}
    # 成绩按照ID分组，写入字典
    for i in range(len(ids)):
        ID = ids[i]
        id_str = str(ID)
        if id_scores_dict.get(id_str) is None:
            id_scores_dict[id_str] = []
        score = scores[i]
        id_scores_dict[id_str].append(score)

    # 按照ID计算成绩，存入字典（过滤掉不合规的成绩）
    id_score_statics = {}
    score_statics = []
    print("id_scores_dict={}".format(id_scores_dict))
    for id_str in id_scores_dict.keys():
        ID = int(id_str)
        scores = id_scores_dict.get(id_str)
        if len(scores) < 3:
            continue
        scores.sort(reverse=True)
        filtered_scores = scores[:3]
        total_score = reduce(lambda x, y: x + y, filtered_scores)
        if id_score_statics.get(str(total_score)) is None:
            id_score_statics[str(total_score)] = []
            score_statics.append(str(total_score))
        id_score_statics[str(total_score)].append(ID)
        id_score_statics[str(total_score)].sort(reverse=True)

    # 排序输出
    statics_result = []
    score_statics.sort(reverse=True)
    print("score_statics={}".format(score_statics))
    for i in range(len(score_statics)):
        score = score_statics[i]
        ids = id_score_statics[score]
        print("score={},ids={}".format(score, ids))
        statics_result.extend(ids)

    return statics_result


'''
5.数据分类
链接： https://wiki.amoscloud.com/zh/ProgramingPractice/NowCoder/Adecco/Topic0010
题目描述
对一个数据a进行分类，
分类方法是，此数据a(4个字节大小)的4个字节相加对一个给定值b取模，
如果得到的结果小于一个给定的值c则数据a为有效类型，其类型为取模的值。
如果得到的结果大于或者等于c则数据a为无效类型。

比如一个数据a = 0x01010101，b = 3
按照分类方法计算：(0x01 + 0x01 + 0x01 + 0x01) % 3 = 1
所以如果c等于2，则此a就是有效类型，其类型为1
如果c等于1，则此a是无效类型

又比如一个数据a = 0x01010103，b = 3
按分类方法计算：(0x01 + 0x01 + 0x01 + 0x03) % 3 = 0
所以如果c = 2则此a就是有效类型，其类型为0
如果c = 0则此a是无效类型

输入12个数据，
第一个数据为c，第二个数据为b，
剩余10个数据为需要分类的数据

请找到有效类型中包含数据最多的类型，
并输出该类型含有多少个数据

输入描述
输入12个数据用空格分割，
第一个数据为c，第二个数据为b，
剩余10个数据为需要分类的数据。

输出描述
请找到有效类型中包含数据最多的类型，
并输出该类型含有多少个数据。

示例一
输入
3 4 256 257 258 259 260 261 262 263 264 265
输出
3
'''


def num_group(comp_num: int, float_num: int, nums: list[int]):
    result = {}
    group = None
    max_res = 0

    for i in range(len(nums)):
        sum = 0

        num = nums[i]
        byte_num = hex(num)
        num_hex_str = byte_num.lstrip("0x")

        total = len(num_hex_str) / 2 if len(num_hex_str) % 2 == 0 else len(num_hex_str) // 2 + 1
        print("total={}".format(total))
        for j in range(total):
            tmp = hex(num >> (8 * j))
            print("tmp={}, num={}".format(tmp, hex(num)))
            sum += int(tmp.lstrip("0x"))

        res = sum % float_num
        if result.get(res) is None:
            result[res] = 0
        count = result.get(res)
        if res < comp_num:
            result[res] = count + 1

    for k in result.keys():
        if result[k] > max_res:
            max_res = result[k]
            group = k

    return group, max_res


'''
6.5键键盘的输出
链接：https://blog.nowcoder.net/n/c7bb482cddb647b5965c2f55ef13f7da
【5键键盘的输出】有一个特殊的 5键键盘，上面有 a,ctrl-c,ctrl-x,ctrl-v,ctrl-a五个键。
a键在屏幕上输出一个字母 a;
ctrl-c将当前选择的字母复制到剪贴板;
ctrl-x将当前选择的 字母复制到剪贴板，并清空选择的字母;
ctrl-v将当前剪贴板里的字母输出到屏幕;
ctrl-a 选择当前屏幕上所有字母。
注意:
1、剪贴板初始为空，新的内容被复制到剪贴板时会覆盖原来的内容
2、当屏幕上没有字母时，ctrl-a无效
3、当没有选择字母时，ctrl-c和 ctrl-x无效
4、当有字母被选择时，a和ctrl-v这两个有输出功能的键会先清空选择的字母，再进行输出
给定一系列键盘输入，输出最终屏幕上字母的数量。
输入描述:
输入为一行，为简化解析，用数字 12345代表 a,ctrl-c,ctrl-x,ctrl-v,ctrl-a五个键的输入，数字用空格分隔
输出描述:
输出一个数字，为最终屏目上字母的数量。
示例:
输入
111
输出
3
'''
def five_keyboard(inputs: list[int]):
    insert_board = []
    std_out = []
    select_content = ""

    for i in range(len(inputs)):
        input_num = inputs[i]
        if input_num == 1:
            std_out.append("a")
        elif input_num == 2:
            if select_content:
                insert_board.append(select_content)
        elif input_num == 3:
            if select_content:
                insert_board.append(select_content)
                select_content = ""
        elif input_num == 4:
            # if len(insert_board) > 0:
            std_out.extend(insert_board)
        elif input_num == 5:
            select_content = std_out
        else:
            print("非法输入!")
            return 0

    return len(std_out)


'''
7.检查是否存在满足条件的数字组合
给定一个正整数数组检查数组中是否存在满足规则的数组组合

规则： A=B+2C

输入描述

第一行输出数组的元素个数 接下来一行输出所有数组元素，用空格隔开 输出描述 如果存在满足要求的数 在同一行里依次输出 规则里 A/B/C的取值 用空格隔开 如果不存在输出0

示例1： 输入 4 2 7 3 0 输出 7 3 2 说明： 7=3+2*2

备注：

数组长度在3~100之间

数组成员为0~65535

数组成员可以重复

但每个成员只能在结果算式中使用一次，如数组成员为 [0,0,1,5]

0出现两次允许，但结果0=0+2*0不允许 因为算式中使用了3个0

用例保证每组数字里最多只有一组符合要求的解

作者：牛客595136696号
链接：https://www.nowcoder.com/discuss/353150623367503872?sourceSSR=search
来源：牛客网
'''

def check_num_team(nums: list[int]):
    a, b, c = 0, 0, 0

    if len(nums) < 3:
        return a, b, c

    for i in range(len(nums)):
        for j in range(len(nums) - 1, 1, -1):
            max_num, min_num = nums[i], nums[j]
            if nums[j] > max_num:
                max_num = nums[j]
                min_num = nums[i]
            n = max_num - min_num * 2
            m = int((max_num - min_num) / 2) if (max_num - min_num) % 2 == 0 else None
            k1 = max_num + 2 * min_num
            k2 = min_num + 2 * max_num
            # n_check, m_check = False, False
            try:
                index = nums.index(n)
            # 不满足
            except ValueError as e:
                pass
            else:
                if i != index and index != j:
                    a, b, c = max_num, n, min_num
                    print("i={},j={},min={},max={},a={},b={},c={}, n={}".format(i, j, min_num, max_num, a, b, c, n))
                    # n_check = True
                    return a, b, c

            if m:
                try:
                    index = nums.index(m)
                # 不满足
                except ValueError as e:
                    pass
                else:
                    if i != index and index != j:
                        a, b, c = max_num, min_num, m
                        print("i={},j={},min={},max={},a={},b={},c={}, m={}".format(i, j, min_num, max_num, a, b, c, m))
                        return a, b, c

            try:
                index = nums.index(k1)
            # 不满足
            except ValueError as e:
                pass
            else:
                if i != index and index != j:
                    a, b, c = k1, max_num, min_num
                    print("i={},j={},min={},max={},a={},b={},c={}, k1={}".format(i, j, min_num, max_num, a, b, c, k1))
                    # n_check = True
                    return a, b, c

            try:
                index = nums.index(k2)
            # 不满足
            except ValueError as e:
                pass
            else:
                if i != index and index != j:
                    a, b, c = k2, min_num, max_num
                    print("i={},j={},min={},max={},a={},b={},c={}, k2={}".format(i, j, min_num, max_num, a, b, c, k2))
                    # n_check = True
                    return a, b, c

            # 二指针相遇，结束循环
            if j == i + 1:
                break

    return a, b, c


'''
8.多个数组按顺序合并
题目描述：
现在有多组整数数组，需要将他们合并成一个新的数组。合并规则，从每个数组里按顺序取出固定长度的内容合并到新的数组中，取完的内容会删除掉，如果该行不足固定长度或者已经为空，则直接取出剩余部分的内容放到新的数组中，继续下一行。如样例1，获得长度3，先遍历第一行，获得2,5,6；再遍历第二行，获得1,7,4；再循环回到第一行，获得7,9,5；再遍历第二行，获得3,4；再回到第一行，获得7，按顺序拼接成最终结果。

输入描述：
第一行是每次读取的固定长度，长度>0；
第2-n行是需要合并的数组，不同的数组用回车换行分隔，数组内部用逗号分隔。

输出描述：
输出一个新的数组，用逗号分隔。

-------------示例---------------------------------------------------------------------------
输入：
3
2,5,6,7,9,5,7
1,7,4,3,4
4,5,7,1,3,8

输出：
2,5,6,1,7,4,4,5,7,7,9,5,3,4,1,3,8,7
'''


def merge_num_list(n: int, num_lists: list[str]):
    results = []
    nums = []
    max_len = 0

    for i in range(len(num_lists)):
        num_str = num_lists[i]
        num_list = num_str.split(",")
        if len(num_list) > max_len:
            max_len = len(num_list)
        nums.append(num_list)

    count = max_len / n if max_len % n == 0 else max_len // n + 1

    print("count={}, nums={}".format(count, nums))
    for j in range(count):
        for k in range(len(nums)):
            num_k = nums[k]
            if len(num_k) >= (j+1)*n:
                data = num_k[n*j:(j+1)*n]
                results.extend(data)
                # print("j={}, k = {}, data={}".format(j, k, data))
            elif len(num_k) >= n*j:
                data = num_k[n * j:]
                # print("j={}, k = {}, data={}".format(j, k, data))
                results.extend(data)
            else:
                pass

    return ",".join(results)


'''
9.求解连续数列
链接：https://wiki.amoscloud.com/zh/ProgramingPractice/NowCoder/Adecco/Topic0076
题目描述
已知连续正整数数列{K}=K1,K2,K3… Ki的各个数相加之和为S,
i = N (0 < S < 100000, 0 < N < 100000), 求此数列K。

输入描述
输入包含两个参数

连续正整数数列和S
数列里数的个数N
输出描述
如果有解输出数列K，如果无解输出-1

示例一
输入
525 6
输出
85 86 87 88 89 90
'''


def get_sequence(counts: int, n: int):
    result = []

    begin_data = 0
    if n % 2 == 0:
        if counts % (n / 2) != 0:
            return -1
        pair_count = int(counts / (n / 2))
        if pair_count % 2 != 0:
            begin_data = pair_count // 2 - int(n / 2) + 1
        else:
            begin_data = (pair_count/2 - 1) - int(n / 2) + 1
        for i in range(n):
            result.append(begin_data + i)
    else:
        if counts % (n + 1) != 0:
            return -1
        pair_count = int(counts / (n // 2 + 1))
        if pair_count % 2 != 0:
            begin_data = pair_count // 2 - int(n // 2 + 1) + 1
        else:
            begin_data = pair_count/2 - n / 2 + 1
        for i in range(n):
            result.append(begin_data + i)

    return result


'''
10.题目描述
公司用一个字符串来表示员工的出勤信息

absent:缺勒
late: 迟到
leaveearly: 早退
present: 正常上班
现需根据员工出勤信息，判断本次是否能获得出勤奖，能获得出勤奖的条件如下:

缺勤不超过一次，
没有连续的迟到/早退:
任意连续7次考勤，缺勒/迟到/早退不超过3次
输入描述
第一行输入一个整数n，表示有多少个员工

后面n行，每一行输入若干个字符串，表示第i名员工的出勤信息

输出描述
输出n行，每一行表示这名员工能否获得出勤奖，如果可以，则输出“true"，否则输出”false"

示例1
输入：
2
present
present present

输出：
true true

示例2
输入：
2
present
present absent present present leaveearly present absent

输出：
true false

作者：code5bug
链接：https://www.nowcoder.com/discuss/600342118011334656?sourceSSR=search
来源：牛客网
'''


def attendance_data(clock_records: list[str]):
    illegal_records = []

    id_latest_record_dict = {}

    for i in range(len(clock_records)):
        record_str = clock_records[i]
        record = record_str.split(",")

        if len(record) < 5:
            print("record illegal!")
            continue

        ID = record[0]
        time = int(record[1])
        distance = int(record[2])
        real_mathine_id = record[3]
        reg_mathine_id = record[4]

        if id_latest_record_dict.get(ID) is None:
            id_latest_record_dict[ID] = record
        else:
            latest_record = id_latest_record_dict.get(ID)
            latest_time = latest_record[1]
            latest_distance = latest_record[2]
            # 异常数据
            if real_mathine_id != reg_mathine_id:
                print("illegal record with mathine id not matched!")
                illegal_records.append(record_str)
                # continue
            elif time - int(latest_time) < 60 and distance - int(latest_distance) > 5:
                print("illegal record with distances too far away!!")
                illegal_records.append(','.join(latest_record))
                illegal_records.append(record_str)
                # continue
            else:
                pass
    return illegal_records


if __name__ == '__main__':
    # print(str_formatter('12abc-abCABc-4aB@', 3))
    # print(str_formatter('12abc-abCABc-4aB@', 12))

    # print(is_child_str('abc', 'ahbgdc'))
    # print(is_child_str('axc', 'ahbgdc'))

    # print(max_num('34533'))
    # print(max_num('5445795045'))

    # print(score_statics([3,3,7,4,4,4,4,7,7,3,5,5,5], [53,80,68,24,39,76,66,16,100,55,53,80,55]))

    # print(num_group(3, 4, [256, 257, 258, 259, 260, 261, 262, 263, 264, 265]))
    # print(num_group(1, 4, [256, 257, 258, 259, 260, 261, 262, 263, 264, 265]))

    # print(five_keyboard([1,1,1]))

    # print(check_num_team([2, 7, 3, 0]))

    # print(merge_num_list(3, ["2,5,6,7,9,5,7", "1,7,4,3,4", "4,5,7,1,3,8"]))

    # print(get_sequence(525, 6))

    # print(attendance_data(['100000,10,1,ABCD,ABCD', '100000,50,10,ABCD,ABCD']))
    print(attendance_data(['100000,10,1,ABCD,ABCD', '100000,80,10,ABCE,ABCD']))