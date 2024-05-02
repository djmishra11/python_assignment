"""

Create a class 'Time' and initialize it with hours and minutes.
Create a method addTime() which should take two Time objects and add them.

 E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)

Create another method displayTime() which should print the time.
Also, create a method displayMinute() which should display the total minutes in the Time.
 E.g.- (1 hr 2 min) should display 62 minutes.

"""

class Time:

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other_time):
        total_minutes = self.hours * 60 + self.minutes + other_time.hours * 60 + other_time.minutes
        new_hours, new_minutes = divmod(total_minutes, 60)
        return Time(new_hours, new_minutes)

    def displayTime(self):
        print(f"{self.hours} hr {self.minutes} min")

    def displayMinutes(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")


time1 = Time(hours=2, minutes=50)
time2 = Time(hours=1, minutes=20)

result = time1.addTime(time2)
result.displayTime()  
result.displayMinutes() 
