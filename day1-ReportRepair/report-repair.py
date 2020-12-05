#jacob pawlak
#report-repair.py
#december 5th, 2020
#gooooo blue team!

############### IMPORTS ###############


############### HELPERS ###############



############### MAIN () ###############

def main():

    input_file = open('input.txt', 'r')
    expense_report = []
    [expense_report.append(int(x.strip())) for x in input_file]
    print(expense_report)
    solution = -1
    for i in range(0, len(expense_report) - 1):

        subset_report = expense_report[i+1:]


    return

main()