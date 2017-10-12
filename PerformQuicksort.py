#!/usr/bin/env python3

from random import randint

def choose_pivot(a,pivot_option):
    #Choose a pivot in one of three ways: first element is pivot, last element is pivot, or the median of the first, last and middle element is pivot.
    
    if (pivot_option == 'first'):
        pivot_index = 0
    elif (pivot_option == 'last'):
        pivot_index = len(a) - 1
    elif (pivot_option == 'median-of-three'):
        middle_index = (len(a)-1)//2
        if (a[0]>a[middle_index]>a[-1]) or (a[0]<a[middle_index]<a[-1]):
            pivot_index = middle_index
        elif (a[middle_index]<a[0]<a[-1]) or (a[middle_index]>a[0]>a[-1]):
            pivot_index = 0
        else:
            pivot_index = len(a)-1
    return pivot_index

def partition_array(a):
    #Partition the array about the pivot (which is the first entry of a).
    pivot = a[0]
    i = 1
    for j in range(1,len(a)):
        if (a[j]<pivot):
            a[j], a[i] = a[i], a[j]
            i = i+1

    a[0], a[i-1]= a[i-1], a[0]
    return a, i-1

def quick_sort(a,pivot_option):
    #Quicksort the array a by first choosing a pivot, then partitioning the array and finally recursively calling quicksort on the left and right partitions.
    
    if (len(a)==1):
        return a
    pivot_index = choose_pivot(a,pivot_option)

    a[0], a[pivot_index] = a[pivot_index], a[0]
    a, pivot_position = partition_array(a)

    if (pivot_position == 0):
        la = a[0:1]
    else:
        la = a[0:pivot_position]

    if (pivot_position == len(a)-1):
        ra = a[pivot_position:]
    else:
        ra = a[pivot_position+1:]

    la = quick_sort(la,pivot_option)
    ra = quick_sort(ra,pivot_option)

    if (pivot_position == 0):
        a[0:1] = la
    else:
        a[0:pivot_position] = la

    if (pivot_position == len(a)-1):
        a[pivot_position:] = ra
    else:
        a[pivot_position+1:]= ra
    return a

if __name__ == "__main__":
    length_a = 1000
    range_a = 10000
    a=[randint(0,range_a) for _ in range(0,length_a)]
    
    a_sorted = quick_sort(a,'median-of-three')
    print(a_sorted)

