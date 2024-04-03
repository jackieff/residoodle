BLOCK_DATES_FN = 'data/block_dates_2023.csv'
RESIDENTS_FN = 'data/residents_2022_2023.csv'

GOOGLE_FORM_URL = 'https://forms.gle/eZbazrwhPTAejdck7'

ABOUT_RESIDOODLE = '''
## About this App

Keeping up with your shift schedule is *hard*, and trying to find times to
have meetings or spend time with friends can be even harder.

Thinking of planning a meeting or get together? Pick a range of dates, a 
target time window, and ResiDoodle will do the rest! It automatically pulls
the ShiftAdmin schedule and does its best to guess when people are off service.

Try it below! If you have any questions, you can reach out to Max or leave 
feedback [here](https://forms.gle/LzHDs6e6giXcAT8M8).

## Frequently Asked Questions

**Where does this app get the schedule information?**

It pulls it directly from the ShiftAdmin database. 

**How does it know who is off-service?**

From the block schedule 

**What's the difference between "Day Off" and "Free"?**

A "Day Off" means the resident literally isn't scheduled to work in the ED that day
(though they may be post-night, yay DOMA). "Free" means the resident is scheduled
to work but their shift doesn't overlap the chosen time window.

**Is there anything scheduling-wise that it doesn't include?**

Vacations are considered as "days off" rather than handled differently, and LTJ will 
appear as days off as well. If you have an Ultrasound QA shift scheduled on the same 
day as another shift, the QA will not show up. QA shifts alone will show up as day off.
CES rotations will show up as off-service, but CES individual shifts will load as 
regular shifts.
'''