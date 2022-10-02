

def medicine_slug_to_dict(medicines_names: str, frequencies: str, additional_Infos: str, doctor_full_name: str, clinic_name: str | None, isLengthMatched: bool = False) -> dict:
    frequencies = [int(i) for i in frequencies.split('-')]
    medicines_names = medicines_names.split('-')
    additional_Infos = additional_Infos.split('-')

    result = {"doctor_full_name": doctor_full_name,
              "clinic_name": clinic_name, "medicines": []}

    for i in range(len(medicines_names)):

        result['medicines'] += [{
            "name": medicines_names[i],
            "frequency":frequencies[i],
            "additional_Info":additional_Infos[i]
        }]
    return result


# medicines_names = "باراسيتامول-اموكسوسلين-فازلين"
# frequencies = "3-2-2"
# additional_Infos = "بعد الغداء-بعد العشاء-قبل النوم"

# medicine_slug_to_dict(medicines_names=medicines_names, frequencies=frequencies,
#                       additional_Infos=additional_Infos, doctor_full_name="محمد الاوسي", clinic_name=None)


"""
    result=>{
   "doctor_full_name":"محمد الاوسي",
   "clinic_name":"None",
   "medicines":[
      {
         "name":"باراسيتامول",
         "frequency":3,
         "additional_Info":"بعد الغداء"
      },
      {
         "name":"اموكسوسلين",
         "frequency":2,
         "additional_Info":"بعد العشاء"
      },
      {
         "name":"فازلين",
         "frequency":2,
         "additional_Info":"قبل النوم"
      }
   ]
}
    
"""
