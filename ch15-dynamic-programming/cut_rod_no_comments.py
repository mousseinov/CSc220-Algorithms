"""
CSc220: Implementation of the Rod Cutting Problem.

"""


def cut_rod(prices, length):
    memo = [float("-inf") for _ in range(length+1)]
    memo[0] = 0
    save_solution = [0 for _ in range(length+1)]
    for l in range(1,length+1):
        for cut in range(1,l+1):
            if memo[l-cut] + prices[cut] > memo[l]:
                memo[l] =  memo[l-cut] + prices[cut]
                save_solution[l] = cut
    return memo[length], save_solution


def print_rod_cut(solution):
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

	prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
	optimal_profit, solution = cut_rod(prices, length)

	print("length of rod = {l}\nprices = {p}".format(l=length, p=prices))
	

	# Dont worry about this, it's just for nice printing.
	string_above = "prices = {p}".format(p=prices)
	len_of_string_above = len(string_above)
	print("-"*len_of_string_above)
	

	print("Maximum Profit: ${profit}".format(profit=optimal_profit))
	print("How the rod is cut up:")
	print_rod_cut(solution)



if __name__ == '__main__':
	main()
