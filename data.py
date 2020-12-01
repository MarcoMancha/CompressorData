from datetime import datetime
from datetime import timedelta
import pandas as pd 
import random
import csv

df = pd.read_csv("data.csv",names=["id_variable","name","value","date"]) 
df = df.iloc[1:]

dataset = {}
interstage = 0
status = 0
inlet_pressure = 0
inlet_temperature = 0
discharge_pressure = 0
discharge_temp = 0
stage_1_pressure = 0
stage_1_temp = 0
stage_2_pressure = 0
stage_2_temp = 0
stage_3_pressure = 0
stage_3_temp = 0
stage_4_pressure = 0
stage_4_temp = 0
enclosure = 0
ambient = 0
tiempo = 0
i = 1
ciclo = 1
count = 0
date = ""
new_date = ""
capture = False

failures = []
for x in range(70):
    failures.append(random.randint(75,101))

f = 0

with open('dataset.csv','w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["id", "cycle", "interstage_alarms","inlet_pressure","inlet_temp","discharge_pressure","discharge_temp",
                    "stage_1_pressure", "stage_1_temp","stage_2_pressure", "stage_2_temp","stage_3_pressure", "stage_3_temp","stage_4_pressure", "stage_4_temp",
                    "encolusure_temp","ambient_temp", "minutes_after", "rul"])

    for _, row in df.iterrows():
        if int(row["id_variable"]) == 1:
            status = row["value"]
        elif int(row["id_variable"]) == 4:
            interstage = row["value"]
        elif int(row["id_variable"]) == 25:
            inlet_pressure = row["value"]
        elif int(row["id_variable"]) == 26:
            inlet_temperature = row["value"]
        elif int(row["id_variable"]) == 28:
            discharge_pressure = row["value"]
        elif int(row["id_variable"]) == 29:
            discharge_temp = row["value"]
        elif int(row["id_variable"]) == 32:
            stage_1_pressure = row["value"]
        elif int(row["id_variable"]) == 33:
            stage_1_temp = row["value"]
        elif int(row["id_variable"]) == 34:
            stage_2_pressure = row["value"]
        elif int(row["id_variable"]) == 35:
            stage_2_temp = row["value"]
        elif int(row["id_variable"]) == 36:
            stage_3_pressure = row["value"]
        elif int(row["id_variable"]) == 37:
            stage_3_temp = row["value"]
        elif int(row["id_variable"]) == 38:
            stage_4_pressure = row["value"]
        elif int(row["id_variable"]) == 39:
            stage_4_temp = row["value"]
        elif int(row["id_variable"]) == 41:
            enclosure = row["value"]
        elif int(row["id_variable"]) == 42:
            ambient = row["value"]

        count += 1

        if status != 3:
            capture = True
        
        if capture == True and status == 3 and count >= 16:   
            capture = False
            new_date = datetime.strptime(row["date"], '%Y-%m-%d %H:%M:%S.%f')
            if date != "":
                tiempo = new_date - date
                tiempo = tiempo.total_seconds() / 60
            date = new_date

            rul = failures[f] - ciclo

            writer.writerow([i,ciclo,interstage,inlet_pressure,inlet_temperature,discharge_pressure,discharge_temp,stage_1_pressure,stage_1_temp,
            stage_2_pressure,stage_2_temp,stage_3_pressure,stage_3_temp,stage_4_pressure,stage_4_temp,enclosure,ambient,tiempo, rul])

            ciclo += 1
            if ciclo >= failures[f]:
                rul = failures[f] - ciclo
                if random.choice((True, False)):
                    inlet_pressure_low = 52
                    stage_1_pressure_low = 56
                    enclosure_low = -4
                    interstage = 1
                    
                    writer.writerow([i,ciclo,interstage,inlet_pressure_low,inlet_temperature,discharge_pressure,discharge_temp,stage_1_pressure_low,stage_1_temp,
                    stage_2_pressure,stage_2_temp,stage_3_pressure,stage_3_temp,stage_4_pressure,stage_4_temp,enclosure_low,ambient,tiempo,rul])
                else:
                    inlet_pressure_high = 104
                    discharge_pressure_high = 3800
                    discharge_temp_high = 150
                    stage_1_pressure_high = 450
                    stage_1_temp_high = 325
                    stage_2_pressure_high = 1098
                    stage_2_temp_high = 325
                    stage_3_pressure_high = 2660
                    stage_3_temp_high = 350
                    stage_4_pressure_high = 3800
                    stage_4_temp_high = 350
                    enclosure_high = 140
                    interstage = 1
                    writer.writerow([i,ciclo,interstage,inlet_pressure_high,inlet_temperature,discharge_pressure_high,discharge_temp_high,stage_1_pressure_high,stage_1_temp_high,
                    stage_2_pressure_high,stage_2_temp_high,stage_3_pressure_high,stage_3_temp_high,stage_4_pressure_high,stage_4_temp_high,enclosure_high,ambient,tiempo,rul])
                
                ciclo = 1
                i += 1
                f += 1

            count = 0
            interstage = 0
            inlet_pressure = 0
            inlet_temperature = 0
            discharge_pressure = 0
            discharge_temp = 0
            stage_1_pressure = 0
            stage_1_temp = 0
            stage_2_pressure = 0
            stage_2_temp = 0
            stage_3_pressure = 0
            stage_3_temp = 0
            stage_4_pressure = 0
            stage_4_temp = 0
            enclosure = 0
            ambient = 0

         




