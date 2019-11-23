"""
CSc220: Implementation of the Rod Cutting Problem.

This file contains the cut_rod function implemented
with dynamic programming that returns the optimal profit
and where each cut was made to get the optimal profit.

Read the comments to understand the code.

Note:
The rod is represented by the "#" when printing.
So "####" represents a rod of length 4
and "### ##" reprensents a rod of length 5 that was cut up into pieces
3 and 2.

"""


def cut_rod(prices, length):
    """
    Initialize a list called memo of 
    size length + 1 which is filled with negative infinities.
    
    memo[0] = 0 which is the base case 
    of a rod of length 0 having a price of $0.
    """
    
    # Looks scary but is just a list of infinities of size length + 1
    # Entering it in your terminal/command line will looking this
    # >>> memo  
    # => [-inf, -inf, -inf ... , -inf]
    memo = [float("-inf") for _ in range(length+1)]

    # base case
    memo[0] = 0

    """
    This is a list to store where the optimal cut 
    to get the maximum profit was
    made so we can rebuild our solution if we wish to.
    """
    save_solution = [0 for _ in range(length+1)]


    """
    We will iterate a variable l from 1 to length.
    memo[l] will represent the maximum profit we 
    can make off a rod of size l by cutting it up or not cutting it all.
    At every iteration of l we will iterate a 
    variable called cut which is the the size of the cut
    we wish to make to our rod.
    
    if memo[l-cut] + prices[cut] > memo[l]:
        memo[l] =  memo[l-cut] + prices[cut]
    
    meaning if the profit we get 
    from the part we cut off plus
    the maximum profit we get from a rod of size l-cut is greater than
    the current maximum profit we found at l we update memo[l] to the 
    new maximum profit.
    """
    for l in range(1,length+1):
        for cut in range(1,l+1):
            if memo[l-cut] + prices[cut] > memo[l]:
                memo[l] =  memo[l-cut] + prices[cut] # update memo to the new optimal profit found
                save_solution[l] = cut # At a rod of length l the optimal cost 
    return memo[length], save_solution


def print_rod_cut(solution):
	"""
	This function is here to print the optimal solution in
	rod cutting.

	Solution[i] tells you how big the cut was made at a rod of
	length i to get the maximum profit.
	Solution[i-cut] will tell you
	how big the cut was made for a rod of length i-cut to get
	the maximum profit.
	... You can see how this is becoming recursive.
	
	If we keep appending the size of the cuts that were made
	as strings of "#" to a list until i-cut equals 0, then
	we will get the optimal cutting schema for our rod.

	"""
	done = False
	curr = len(solution) - 1
	final_sol = []
	while not done:
		cut = solution[curr]
		final_sol.append("#"*cut)
		curr -= cut
		if curr is 0:
			done = True
	str_sol = " ".join(final_sol)
	print(str_sol)



def main():
	print("Rod cutting problem")
	print("-"*19)
	
	length = 8

	# make sure prices[0] is 0 because a rod of length 0 sells for $0.
	prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

	

	# We get the profit and solution of where cut the rode
	optimal_profit, solution = cut_rod(prices, length)

	print("length of rode = {l}\nprices={p}".format(l=length, p=prices))
	
	# Dont worry about this printing: its just to print the dashes nicely
	string_above = "prices = {p}".format(p=prices)
	len_of_string_above = len(string_above)
	print("-"*len_of_string_above)
	

	# Print the solution
	print("Optimal profit: {profit}".format(profit=optimal_profit))
	print("How the rod is cut up:")
	print_rod_cut(solution)



if __name__ == '__main__':
	main()
