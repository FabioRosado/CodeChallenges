"""
Calculate the date of meetups.

Typically meetups happen on the same day of the week.  In this exercise, you will take
a description of a meetup date, and return the actual meetup date.

Examples of general descriptions are:

- the first Monday of January 2017
- the third Tuesday of January 2017
- the Wednesteenth of January 2017
- the last Thursday of January 2017

Note that "Monteenth", "Tuesteenth", etc are all made up words. There
was a meetup whose members realized that there are exactly 7 numbered days in a month that
end in '-teenth'. Therefore, one is guaranteed that each day of the week
(Monday, Tuesday, ...) will have exactly one date that is named with '-teenth'
in every month.

Given examples of a meetup dates, each containing a month, day, year, and descriptor 
(first, second, teenth, etc), calculate the date of the actual meetup.
For example, if given "First Monday of January 2017", the correct meetup date is 2017/1/2
"""

import calendar
import datetime

DAYS = {"Monday": 0, "Tuesday": 1, "Wednesday": 2,
        "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}


def meetup_day(year, month, week_day, position):
    """
    Get a standardized date from a piece of text.

    Example:
    Text: "First Monday of January 2017"
    Returns: 2017/1/2
    """
    cal = calendar.Calendar(DAYS[week_day])
    monthly_cal = cal.monthdayscalendar(year, month)
    gen_dates = [monthly_cal[i][0] for i in range(len(monthly_cal))]

    if position == "teenth":
        for i in range(len(gen_dates)):
            if 10 < gen_dates[i] < 20:
                day = gen_dates[i]
    elif position == "last":
        day = gen_dates[-1]
    else:
        week = int(position[0])

        # If the first day of the week is not == 0 we should start
        # counting the week from there
        if gen_dates[0] != 0:
            week -= 1

        day = gen_dates[week]

    return datetime.date(year, month, day)
