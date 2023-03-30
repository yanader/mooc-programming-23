# Write your solution here
from datetime import datetime

def is_it_valid(pic: str) -> bool:
    if len(pic) != 11 or pic[6] not in ['+','-','A']:
        return False

    pic_day = int(pic[0:2])
    pic_month = int(pic[2:4])
    pic_year = int(pic[4:6])
    if pic[6] == '+':
        century = 1800
    elif pic[6] == '-':
        century = 1900
    elif pic[6] == 'A':
        century = 2000

    try:
        date_check = datetime(century + pic_year, pic_month, pic_day)
    except:
        return False
    
    total = int(pic[0:6] + pic[7:10])
    remainder = total % 31
    check_string = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    if pic[10] != check_string[remainder]:
        return False
    return True
    


if __name__ == "__main__":
    print(is_it_valid('310823A9877'))
