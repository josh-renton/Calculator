import math
from bisect import bisect_left


def multipleIndexFinder( iterable, search_item ):
    x = 0
    search_item_found_at = []
    for i in iterable:
        if i == search_item:
            search_item_found_at.append( x )
        x += 1

    return search_item_found_at

def findOccurenceNearest( array, target ):
    pos = bisect_left( array, target )
    if pos == 0:
        return array[0]
    if pos == len(array):
        return array[-1]
    before = array[pos - 1]
    after = array[pos]
    if after - target < target - before:
       return after
    else:
       return before

def findBrackets( calculation ):



    if '(' in calculation:
        total_len = len( calculation )
        print total_len / 2
        lbracket_indices = multipleIndexFinder( iterable=calculation, search_item='(' )
        rbracket_indices = multipleIndexFinder( iterable=calculation, search_item=')' )
        print lbracket_indices
        print rbracket_indices

        print findOccurenceNearest( lbracket_indices, total_len / 2)
        print findOccurenceNearest( rbracket_indices, total_len / 2)
        



    return calculation











def solveCalculation( input_calculation ):

    result = findBrackets( input_calculation )



    return result



    # def applyBODMAS( translated_calculation ):
    #     print string

    #     output_list = [ string ]
        
    #     return output_list


    # def resolveCalculation( list_of_calculations ):

    #     print list_of_calculations

