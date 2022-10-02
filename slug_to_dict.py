
def slugifiedStringToDict(*args:list[str], isLengthMatched: bool)->dict:

    keys = [i[0] for i in args]
    values = [x.split('-') for x in [i[1] for i in args]]


    if len({len(i) for i in values}) != 1 and isLengthMatched:
        return ("all items must have the same length")
    
    result = {}
    for oneKey in range(len(keys)):
        result[keys[oneKey]] = values[oneKey]
    print(result)
    return result
        



medicines_names = ['medicines', "باراسيتامول-اموكسوسلين-فازلين"]
frequencies = ['frequencies', "3-2-2"]
taking_times = ["taking times", "بعد الغداء-بعد العشاء-قبل النوم"]

slugifiedStringToDict(medicines_names,frequencies,taking_times ,isLengthMatched=True)

"""
result => {
   "medicines":[
      "باراسيتامول",
      "اموكسوسلين",
      "فازلين"
   ],
   "frequencies":[
      "3",
      "2",
      "2"
   ],
   "taking times":[
      "بعد الغداء",
      "بعد العشاء",
      "قبل النوم"
   ]
}
"""