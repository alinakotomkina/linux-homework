#!/usr/bin/python3
expression=[2.5,7.1,0.8,5.4,9.2,3.0]
def filter_expression(values, threshold):
    a=[]
    for i in range(len(values)):
        if values[i]>threshold:
            a.append(values[i])
    return a
print(filter_expression(expression,5.0))


