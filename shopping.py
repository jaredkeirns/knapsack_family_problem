# Jared Keirns
# CS 325 HW3
# A program that reads a file containing data on a store and family members. It runs a knapsack function that determines
# what the maximum value each member could have based on item weight and

outputFile = open("results.txt", "w+")      # The file that will be used for results.


def max(x, y):
    """
    A function that returns the maximum of two integers. To be used with the shopping function.
    """
    if x > y:
        return x
    return y


def shopping(weight, weight_array, vals, n):
    """
    A knapsack function that calculates the maximum value a person could gather from a store, based on their
    specific weight capacity.
    """
    items = []      # A list that will contain the members total and the items used to attain it.
    totals = [[0 for x in range(weight + 1)] for x in range(n + 1)]     # A knapsack matrix.

    for i in range(n + 1):
        for w in range(weight + 1):
            if i == 0 or w == 0:
                totals[i][w] = 0
            elif weight_array[i - 1] <= w:      # Below is the knapsack algorithm, with the prices, item weights.
                totals[i][w] = max(vals[i - 1] + totals[i - 1][w - weight_array[i - 1]], totals[i - 1][w])
            else:
                totals[i][w] = totals[i - 1][w]
    total = totals[n][weight]       # The family member's maximum value, stores it at the beginning of the array.
    items.append(total)

    w = weight
    for i in range(n, 0, -1):       # Below is used to determine what items were used.
        if total <= 0:
            break   # If the items have been found.
        if total == totals[i - 1][w]:
            continue
        else:
            items.append(weight_array[i - 1])        # Adds items and deducts their weights.
            total = total - vals[i - 1]
            w = w - weight_array[i - 1]

    return items        # Returns an array where the first item is the total and the rest are the specific items.


test_case_num = 0
array = []
st = open("shopping.txt")       # Reads the shopping.txt file
values = st.read()
str_out = ""
for elements in values:
    if elements != "\n":     # Reads until there is a line break.
        array.append(elements)
    else:
        array.append(" ")  # Appends characters and spaces to a list.

loc = 0
while array[loc] != " ":
    str_out += array[loc]
    del array[loc]
del array[loc]
tests = int(str_out)  # Has determined the number of test cases.
str_out = ""

while tests > 0:            # Loop for each test case.

    test_case_num += 1
    while array[loc] != " ":
        str_out += array[loc]
        del array[loc]
    items = int(str_out)        # Has determined the number of items.
    del array[loc]

    price_array = []  # Used to track the price of items in order they appear in the document.
    weight_array = []  # Used to track the weight of items in order they appear in the document.
    str_out = ""

    while items > 0:
        while array[loc] != " ":
            str_out += array[loc]
            del array[loc]
        price = int(str_out)
        price_array.append(price)    # Stores item price.
        str_out = ""
        del array[loc]
        while array[loc] != " ":
            str_out += array[loc]
            del array[loc]
        weight = int(str_out)
        weight_array.append(weight)     # Stores item weight.
        items -= 1
        str_out = ""
        del array[loc]

    while array[loc] != " ":
        str_out += array[loc]
        del array[loc]
    members = int(str_out)
    del array[loc]          # Has determined the number of family members.

    members_array = []  # Used to track the family members.
    carry_weight_array = []     # Used to track what each member can carry.
    member_count = 0
    str_out = ""

    while members > 0:
        while len(array) > 0 and array[loc] != " ":
            str_out += array[loc]
            del array[loc]
        carry_weight = int(str_out)
        members_array.append(member_count)          # Used with the 'cwa' array to track member carry weight.
        carry_weight_array.append(carry_weight)
        str_out = ""
        members -= 1
        member_count += 1
        if len(array) > 0:
            del array[loc]

    num = 0
    fin_array = []
    max_val = 0

    while member_count > 0:         # Extracting carry weight and member number.
        carry_weight = carry_weight_array[0]
        del(carry_weight_array[0])
        del(members_array[0])
        n = len(price_array)
        member_count -= 1
        array_2 = shopping(carry_weight, weight_array, price_array, n)      # Runs the knapsack algorithm for each.
        i_total = array_2[0]            # Takes the member's total out of the list and adds it to the family's total.
        del array_2[0]
        max_val += i_total
        num += 1
        for item in array_2:        # Gets the item numbers from the weights.
            i = weight_array.index(item)
            fin_array.append(i + 1)
        fin_array.append(" ")
        out_str = ""

    outputFile.write("Test Case " + str(test_case_num) + '\n')          # Writes the data into the results.txt file.
    outputFile.write("Total Price " + str(max_val) + '\n')
    outputFile.write("Member Items" + '\n')
    r = len(fin_array)
    i = 1
    j = 0
    while num > 0:
        outputFile.write(str(i) + ": ")
        while fin_array[j] != " ":
            outputFile.write(str(fin_array[j]) + " ")
            j += 1
        outputFile.write('\n')
        num -= 1
        i += 1
        j += 1

    outputFile.write('\n')
    outputFile.write('\n')

    tests -= 1      # Will loop back when each test case is completed and written in the file.

