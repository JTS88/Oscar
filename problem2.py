import collections
from typing import Tuple

# Find the window of k days in the month that had the most appointments
# This solution makes one pass through the input array and one pass through the appointments by day array
# so the time complexity would be O(n + 32)?  Or since the second part is constant time, should it just be O(n)?
# In addition, like problem 1, it is faster than using a hash because it is simple array indexing
# It uses a single array of 32 ints plus a queue of k entries so the space complexity would be O(k + 32)?

appointments = [1, 2, 3, 1, 2, 3, 1, 2, 3, 15, 14, 14, 21, 6, 5, 4, 8, 5, 8, 6, 6, 6, 28, 29, 31, 31, 31, 31, 31, 31, 31, 30, 29]
k = 3


def find_most_in_window(appts: [int], k: int) -> Tuple[int, int]:
    # to optimize this we will start with the fact that months have at most 31 days in them
    # since the days are not zero-based, the array will be 32 entries
    appts_by_day = [0] * 32

    for i in appts:
        # a little bounds checking just to be safe
        if not 1 <= i <= 31:
            print(f'Day {i} out of range!')
            continue

        # increment the number of appointments on that day
        appts_by_day[i] += 1

    max_appointments = 0
    start_of_max_win = 0
    running_total = 0
    dq = collections.deque(maxlen=k)
    for idx, appts_on_day in enumerate(appts_by_day):

        # until the queue is fully populated (to k items) don't pop anything
        if len(dq) == k:
            # decrement the total by the amount that just went out of the window
            running_total -= dq.popleft()

        # keep count of the number of days in the window
        running_total += appts_on_day
        dq.append(appts_on_day)

        if running_total > max_appointments:
            max_appointments = running_total
            start_of_max_win = idx - k + 1

    return start_of_max_win, max_appointments


if __name__ == '__main__':
    result = find_most_in_window(appointments, k)

    print(f'The most appointments in a {k} day period was {result[1]} starting on day {result[0]}')
