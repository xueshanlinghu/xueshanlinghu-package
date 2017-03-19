#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""xueshanlinghu.math

The package includes so many handy functions to calculate related to math.

这个包包含了许多趁手的函数，可以用于数学的各种计算。
"""

def sum(sumlist):
    '''
    calculate the sum of the list, you need to give a list of numbers.

    计算list中元素的和，你需要定义一个满含数字的list。
    '''
    total = 0
    for i in sumlist:
        total = total + i
    return total

def mean(meanlist):
    '''
    calculate the mean of the list, you need to give a list of numbers.

    计算list中元素的算术平均数，你需要定义一个满含数字的list。
    '''
    result = round((sum(meanlist) / len(meanlist)),2)
    return result

def median(medianlist):
    '''
    calculate the median of the list, you need to give a list of numbers.

    计算list中元素的中位数，你需要定义一个满含数字的list。
    '''
    medianlist.sort()
    if len(medianlist) % 2 == 0:
        return (medianlist[len(medianlist)//2 - 1] + medianlist[len(medianlist)//2]) / 2
    else:
        return medianlist[(len(medianlist) + 1)//2 - 1]

def sqrt(number):
    '''
    calculate the square root of the number, you need to give number.

    计算一个数的平方根，你需要定义一个数字。
    '''
    return number ** 0.5

def sd(sdlist):
    '''
    calculate the standard deviation of the list, you need to give a list of numbers.

    计算list中元素的标准差，你需要定义一个满含数字的list。
    '''
    avg = mean(sdlist)
    var = 0
    for i in sdlist:
        var = var + (i - avg) ** 2
    var = var / len(sdlist)
    result = sqrt(var)
    return result

def var(varlist):
    '''
    calculate the variance of the list, you need to give a list of numbers. The degree of freedom is n.

    计算list中元素的方差，你需要定义一个满含数字的list。自由度为n。
    '''
    avg = mean(varlist)
    var = 0
    for i in sdlist:
        var = var + (i - avg) ** 2
    var = var / len(sdlist)
    return var

def AAD(AADlist):
    '''
    calculate the average absolute deviation(mean absolute deviation) of the list, you need to give a list of numbers.

    计算list中元素的平均绝对差，你需要定义一个满含数字的list。
    '''
    avg = mean(AADlist)
    sum = 0
    for i in AADlist:
        sum = sum + abs(i - avg)
    res = sum / len(AADlist)
    return res

def z_score_normal(zlist, type = 0):
    '''
    calculate the z-score normalization of the list elements, you need to give a list of numbers. The default setting for type is 0, meaning that the approach of the calculation is using the standard devidation.

    The formula is (vi-vmean)/sdv. If you want to use the mean absolute deviation instead of standard deviation, you can set the type argument to 1.

    计算list中每一个元素使用z分数规范化后的值，你需要定义一个满含数字的list。第二个type参数默认为0，默认使用标准差来进行计算。

    公式为(vi-vmean)/sdv，list元素减去平均值再除以标准差。如果你想使用平均绝对差来代替标准差的话，请设置type参数为1。
    '''
    avg = mean(zlist)
    if type == 1:
        addv = ADD(zlist)
        for i in range(len(zlist)):
            zlist[i] = (zlist[i] - avg) / addv
    elif type == 0:
        sdv = sd(zlist)
        for i in range(len(zlist)):
            zlist[i] = (zlist[i] - avg) / sdv

    return zlist

def cov(clistA, clishB):
    '''
    calculate the covariance of two list, you need to give two same length lists to this function.

    计算两个list的协方差，你需要传递两个等长的list。
    '''
    avgA = mean(clistA)
    avgB = mean(clishB)
    lengthA = len(clistA)
    sum = 0
    for i in range(lengthA):
        sum = sum + (clistA[i] - avgA) * (clishB[i] - avgB)
    res = sum / lengthA
    return res

def corr_coef(colistA, colistB):
    '''
    For numeric attributes, we can evaluate the correlation between two attributes, A and B, by computing the correlation coefficient (also known as Pearson’s product moment coefficient, named after its inventer, Karl Pearson).

    If r A,B is greater than 0, then A and B are positively correlated. If the resulting value is equal to 0, then A and B are independent and there is no correlation between them.If the resulting value is less than 0,then A and B are negatively correlated. The length of these two list should be the same.

    对于数字属性，我们可以评价A和B之间的关系程度，通过计算他们的关系系数（相关系数）（也叫皮尔逊积差系数，以它的发明者Karl Pearson来命名）。

    如果得到的系数rAB大于0，那么A和B正相关。如果结果等于零，那么A与B独立，它们之间没有关系。如果结果小于0，那么A和B负相关。这两个list的元素个数应该一致。
    '''
    sdA = sd(colistA)
    sdB = sd(colistB)
    res = cov(colistA, colistB)
    res = res / (sdA * sdB)
    return res

def which_close(num, min_num, max_num):
    '''
    Compare the distance between num argument and min, max argument, return the closer one as result. If the distances are the same, then return the min one.

    比较一个数字跟最大最小数字的距离，返回更接近的数字（返回的内容一定是最大或者最小值参数其中之一）。如果距离相等，则默认返回最小值。
    '''
    dis_min = abs(num - min_num)
    dis_max = abs(num - max_num)
    if dis_min <= dis_max:
        return min_num
    else:
        return max_num

def bin(binlist, bin_size, bin_type = 0):
    '''
    Divide the binlist into different bin according to the type.
    The bin_size augument you can define the size of the bin, but the length of the binlist should divide the bin_size to get a integer with no remainder.
    The default for bin_type is 0, meaning that partition by equal-frequency bins only.
    For this argument, you have several choices as below:
    (1) bin_type = 0, equal-frequency bins.
    (2) bin_type = 1, partition then smooth by mean bins.
    (3) bin_type = 2, partition then smooth median bins.
    (4) bin_type = 3, partition then smooth boundaries bins.

    将binlist中的元素根据选择的分箱类型放到不同的箱子里面。
    bin_size参数表示要分箱的箱子大小，但是需要注意，binlist的元素个数应该被定义的size整除。
    默认的bin_type为0，为只使用等频率分箱。
    对于这个参数，你有以下几种选择：
    （1）bin_type = 0，等频率分箱。
    （2）bin_type = 1，等频率分箱后根据平均值分箱。
    （3）bin_type = 2，等频率分箱后根据中位数分箱。
    （4）bin_type = 3，等频率分箱后根据边界数分箱。
    '''
    lenlist = len(binlist)
    if lenlist % bin_size != 0:
        return "The length of the binlist should divide the bin_size to get a integer with no remainder.binlist的元素个数应该被定义的size整除。"
    binlist.sort()
    i = 0
    j = 0
    if bin_type == 0:
        while i < lenlist:
            new_bin = []
            while len(new_bin) < bin_size:
                new_bin.append(binlist[i])
                i = i + 1
            j = j + 1
            print("bin" + str(j) + ":" + str(new_bin))
    elif bin_type == 1:
        while i < lenlist:
            new_bin = []
            while len(new_bin) < bin_size:
                new_bin.append(binlist[i])
                i = i + 1
            avg = round(mean(new_bin))
            for each in range(bin_size):
                new_bin[each] = avg
            j = j + 1
            print("bin" + str(j) + ":" + str(new_bin))
    elif bin_type == 2:
        while i < lenlist:
            new_bin = []
            while len(new_bin) < bin_size:
                new_bin.append(binlist[i])
                i = i + 1
            med = median(new_bin)
            for each in range(bin_size):
                new_bin[each] = med
            j = j + 1
            print("bin" + str(j) + ":" + str(new_bin))
    elif bin_type == 3:
        while i < lenlist:
            new_bin = []
            while len(new_bin) < bin_size:
                new_bin.append(binlist[i])
                i = i + 1
            max_new_bin = max(new_bin)
            min_new_bin = min(new_bin)
            for each in range(bin_size):
                new_bin[each] = which_close(new_bin[each], min_new_bin, max_new_bin)
            j = j + 1
            print("bin" + str(j) + ":" + str(new_bin))
    bin_num = lenlist // bin_size
    return "The amount of the bins are " + str(bin_num)

def bin_equal_width(binlist, bin_num):
    '''
    Divide the binlist into different bin according to the bin_num.
    The bin_num augument you can define the amount of the bins.

    将binlist中的元素根据箱子的数量放到不同的箱子里面。
    bin_num参数表示要分的箱子的数量。
    '''
    binlist.sort()
    max_binlist = max(binlist)
    bin_length = len(binlist)
    num_now = max_binlist
    while num_now % bin_num != 0:
        num_now = num_now + 1
    bin_size = num_now // bin_num
    i = 1
    k = 0
    while i <= bin_num:
        j = 0
        new_bin = []
        while j < bin_length:
            if binlist[j] >= (i - 1) * bin_size and binlist[j] < i * bin_size:
                new_bin.append(binlist[j])
            j = j + 1
        k = k + 1
        print("bin" + str(k) + ":" + str(new_bin))
        i = i + 1
    return "The amount of the bins are " + str(bin_num)
