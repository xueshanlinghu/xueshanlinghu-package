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
