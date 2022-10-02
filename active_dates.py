import datetime
from datetime import time



def create_doctor_schedual_date_and_time(sunday: list[time], monday: list[time], tuesday: list[time], wednesday: list[time], thursday: list[time], friday: list[time], saturday: list[time], howManyDays: int):
    today = str(datetime.date.today())
    data = {
        'Sunday': [],
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
    }
    weekdaystimes = [sunday, monday, tuesday,
                     wednesday, thursday, friday, saturday]
    for day in range(howManyDays):

        date_1 = datetime.datetime.strptime(
            today, "%Y-%m-%d") + datetime.timedelta(days=day)
        # print(date_1.strftime('%A'))
        dayName = date_1.strftime('%A')
        if dayName == 'Sunday' and sunday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

        if dayName == 'Monday' and monday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

        if dayName == 'Tuesday' and tuesday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

        if dayName == 'Wednesday'and wednesday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

        if dayName == 'Thursday'and thursday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

        if dayName == 'Friday' and friday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

        if dayName == 'Saturday' and saturday:
            data[dayName] += [date_1.strftime('%Y-%m-%d')]

    final = []
    for daytime in range(len(data.items())):
        dayName = list(data.items())[daytime][0]
        calendarTime = []
        for date1 in list(data.items())[daytime][1]:
            # print(f"{dayName} {date1} {weekdaystimes[daytime]}")

            calendarTime.append({date1: weekdaystimes[daytime]})
        data2 = data
        data2[dayName] = calendarTime
        # final.append({dayName: calendarTime})
        
    return data2

# sunday = ['20:00', '21:15', '22:00', '24:30']
# monday = ['20:00', '21:15', '22:00', '24:30']
# tuesday = ['10:00', '11:00', '13:10', '14:30']
# wednesday = ['10:00', '11:00', '13:10', '14:30']
# thursday = ['10:00', '11:00', '13:10', '14:30']
# friday = ['10:00', '11:00', '13:10', '14:30']
# saturday = ['10:00', '11:00', '13:10', '14:30']

# create_doctor_schedual_date_and_time(sunday=sunday, monday=monday, tuesday=tuesday,
#                                      wednesday=wednesday, thursday=thursday, friday=friday, saturday=saturday, howManyDays=30)


"""
result =>{
   "Sunday":[
      {
         "2022-10-09":[
            "20:00",
            "21:15",
            "22:00",
            "24:30"
         ]
      },
      {
         "2022-10-16":[
            "20:00",
            "21:15",
            "22:00",
            "24:30"
         ]
      },
      {
         "2022-10-23":[
            "20:00",
            "21:15",
            "22:00",
            "24:30"
         ]
      },
      {
         "2022-10-30":[
            "20:00",
            "21:15",
            "22:00",
            "24:30"
         ]
      }
   ],
   "Monday":[
      {
         "2022-10-03":[
            "20:00",
            "21:15",
            "22:00",
            "24:30"
         ]
      },
      {
         "2022-10-10":[
            "20:00",
            "21:15",
            "22:00",
            "24:30"
         ]
      },
      {
         "2022-10-17":[
            "20:00",
            "21:15",
            "22:00",
            "24:30"
         ]
      },
      {
         "2022-10-24":[
            "20:00",
            "21:15",
            "22:00",
            "24:30"
         ]
      },
      {
         "2022-10-31":[
            "20:00",
            "21:15",
            "22:00",
            "24:30"
         ]
      }
   ],
   "Tuesday":[
      {
         "2022-10-04":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-11":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-18":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-25":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-11-01":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      }
   ],
   "Wednesday":[
      {
         "2022-10-05":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-12":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-19":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-26":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      }
   ],
   "Thursday":[
      {
         "2022-10-06":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-13":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-20":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-27":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      }
   ],
   "Friday":[
      {
         "2022-10-07":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-14":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-21":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-28":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      }
   ],
   "Saturday":[
      {
         "2022-10-08":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-15":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-22":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      },
      {
         "2022-10-29":[
            "10:00",
            "11:00",
            "13:10",
            "14:30"
         ]
      }
   ]
}
"""