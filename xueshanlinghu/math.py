"""xueshanlinghu.math

The package includes so many handy functions to calculate related to math.
"""

def sum(sumlist):
    total = 0
    for i in sumlist:
        total = total + i
    return total

def mean(meanlist):
    result = round((sum(meanlist) / len(meanlist)),2)
    return result

def median(medianlist):
    medianlist.sort()
    if len(medianlist) % 2 == 0:
        return (medianlist[len(medianlist)//2 - 1] + medianlist[len(medianlist)//2]) / 2
    else:
        return medianlist[(len(medianlist) + 1)//2 - 1]

def sqrt(number):
    return number ** 0.5

def sd(sdlist):
    avg = mean(sdlist)
    var = 0
    for i in sdlist:
        var = var + (i - avg) ** 2
    var = var / len(sdlist)
    result = sqrt(var)
    return result

def var(varlist):
    avg = mean(varlist)
    var = 0
    for i in sdlist:
        var = var + (i - avg) ** 2
    var = var / len(sdlist)
    result = var
    return result
