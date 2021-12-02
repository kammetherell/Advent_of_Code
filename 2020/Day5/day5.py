def binary_decoder(string, one='1',zero='0'):
    string = string.replace(one,'1')
    string = string.replace(zero,'0')
    
    output = int(string, 2)
    
    return output
    
def seat_decoder(seat_string):
    row_str = seat_string[:7]
    col_str = seat_string[7:]
    
    row_int = binary_decoder(row_str, one='B', zero='F')
    col_int = binary_decoder(col_str, one='R', zero='L')
    
    seat_id = row_int * 8 + col_int
    
    return row_int, col_int, seat_id
    
with open("./Day5/input.txt") as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs] 

seat_ids = []

def day5_1():
    max_seat_id = 0
    
    for seat in inputs:
        seat_row, seat_col, seat_id = seat_decoder(seat)
        
        seat_ids.append(seat_id)
        
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    
    return max_seat_id
    
print(day5_1())

def day5_2():
    valid_ids = []
    for r in range(0,128):
        for c in range(0,8):
            seat_id = r * 8 + c
            valid_ids.append(seat_id)
    
    missing_id = [seat for seat in valid_ids if seat not in seat_ids]
    
    return missing_id
    
print(day5_2())