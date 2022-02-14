/*
Find the maximum amount that can be collected by selling movie tickets
Given an integer N and an array seats[] where N is the number of people standing in a line to buy a movie ticket 
and seat[i] is the number of empty seats in the ith row of the movie theater. 
The task is to find the maximum amount a theater owner can make by selling movie tickets to N people. 
Price of a ticket is equal to the maximum number of empty seats among all the rows.

Example:

Input: seats[] = {1, 2, 4}, N = 3
Output: 9

PERSON	EMPTY SEATS	TICKET COST
1	1 	2 	4	4
2	1 	2 	3	3
3	1 	2 	2	2

4 + 3 + 2 = 9

Input: seats[] = {2, 3, 5, 3}, N = 4
Output: 15
comment
*/


def max_amount(seats,tickets,amount=0):
	if tickets == 0:
		return amount
	else:
            seats.sort()
            amount = amount + seats[len(seats)-1]
	    seats[len(seats)-1] = seats[len(seats)-1] - 1
 	    tickets = tickets - 1
	    return max_amount(seats, tickets, amount)
print max_amount(seats = [1,2,4], tickets = 3)
