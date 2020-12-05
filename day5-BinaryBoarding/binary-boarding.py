#jacob pawlak
#binary-boarding.py
#december 5th, 2020
#gooooo blue team!

############### HELPERS ###############

#quick helper to turn the boarding pass into a binary number list
def pass_to_bin(boarding_pass_list):

    bin_pass_list = []
    #noticed after writing a boarding pass down that the format looked like binary,
    # and duhhh the whole thing is about binary trees.. should have seen that one.
    for boarding_pass in boarding_pass_list:
        bin_pass = boarding_pass.replace('B', '1')
        bin_pass = bin_pass.replace('F', '0')
        bin_pass = bin_pass.replace('R', '1')
        bin_pass = bin_pass.replace('L', '0')
        #grab the first part (the row)
        board_row = int('0b' + bin_pass[:-3], 2)
        #grab the second part (the col)
        board_col = int('0b' + bin_pass[-3:], 2)
        #do the weird math they want me to do
        bin_pass_list.append((board_row * 8) + board_col)
        
    return bin_pass_list

#this was the fast and dirty way to find the number that was missing (assuming it was in the bounds anyways)
def my_seat(seat_id_list):

    for seat_id in range(min(seat_id_list), max(seat_id_list)):
        if(seat_id not in seat_id_list):
            return seat_id

############### MAIN () ###############

def main():
    
    #grab the data file
    input_file = open('input.txt', 'r') 
    boaring_passes = []
    [boaring_passes.append(x.strip()) for x in input_file]
    #run the boarding pass -> binary numbers
    bin_pass_list = (pass_to_bin(boaring_passes))
    print(max(bin_pass_list))
    #run the my seat finder
    jacob_seat = my_seat(bin_pass_list)
    print(jacob_seat)

main()