'''DESCRIPTION: 
Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first 
half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;

For n = 239017, the output should be
isLucky(n) = false.

'''

def isLucky(n):
    number = str(n)
    total_first_half = 0
    total_second_half = 0
    
    for i in range(0, len(number):
        if i < len(number)//2:
            total_first_half += int(n[i])
        total_second_half += int(n[i])
    
    if total_first_half == total_first_half:
        return True
    return False