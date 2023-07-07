from typing import Tuple

# Find the day of the month that had the most appointments
# This solution makes one pass through the input array so the time complexity would be O(n)
# In addition, it is faster than using a hash because it is simple array indexing
# It uses a single array of 32 ints so the space complexity would be O(1) because it uses constant space

appointments = [15, 14, 14, 21, 6, 5, 4, 8, 5, 8, 6, 6, 6, 31, 31, 31, 31, 31, 31, 31, 31]


def find_most(appts: [int]) -> Tuple[int, int]:
    # to optimize this we will start with the fact that months have at most 31 days in them
    # since the days are not zero-based, the array will be 32 entries
    appts_by_day = [0] * 32
    busiest_day = 0
    max_appointments = 0

    for i in appts:
        # a little bounds checking just to be safe
        if not 1 <= i <= 31:
            print(f'Day {i} out of range!')
            continue

        # increment the number of appointments on that day
        appts_by_day[i] += 1

        # see if it sets a new max
        if appts_by_day[i] > max_appointments:
            max_appointments = appts_by_day[i]
            busiest_day = i

    return busiest_day, max_appointments


if __name__ == '__main__':
    result = find_most(appointments)

    print(f'The most appointments was {result[1]} on day {result[0]}')
