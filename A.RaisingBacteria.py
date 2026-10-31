#579A

import math


bacteria_num_wanted = int(input(""))
bacteria_num_needed = 0


#we will take num wanted, then take the log_2 and round it down and set it equal to s, next we will subtract s from num wanted, then += 1 to bacteria_num_needed, and we will continue this untill we reach 0

while bacteria_num_wanted > 0:
    s = math.floor(math.log2(bacteria_num_wanted))
    bacteria_num_wanted -= 2 ** s
    bacteria_num_needed += 1
print(bacteria_num_needed)  