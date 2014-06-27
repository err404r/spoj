#!/usr/bin/python
# -*- coding: utf-8 -*-

# N - branches count - i
# M - leaves count - j 


#Read value of M and N from stdin and convert it to integer
[N, M] = map( int, raw_input().split())

leaves_branches_matrix = []
for j in range(0, M):
    leaves_branches_matrix.append( map( int, raw_input().split() ) )

branch_resistance =  map( int, raw_input().split())

branch_number = int( raw_input() ) - 1
while( branch_number != -1 ):
    branch_resistance[branch_number] -= 1
    if( branch_resistance[branch_number] < 1 ):
        for j in leaves_branches_matrix:
            j[ branch_resistance[branch_number] ] = 0
    branch_number = int( raw_input() ) - 1

fallen_leaves_counter = 0
for j in leaves_branches_matrix:
    if( sum(j) == 0 ):
        fallen_leaves_counter = fallen_leaves_counter + 1

print M-fallen_leaves_counter, fallen_leaves_counter


