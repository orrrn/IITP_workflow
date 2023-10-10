import random

import Classification_accident
import pandas as pd
import openpyxl
import numpy as np
import os

def tip_process(case):
    print("TIP Process is going..")

    if case[1] != "Normal" or "normal":
        case[1] == 1 # this is attack
    else:
        case[1] == 0 # this is not attack

    Classification_accident.classification_accident_process(case)

    case = ["IT", "Exploitation for Privilege Escalation=", 1, None, 5, None, None, None]

    print("TIP Process is finished")

    return case


def tip_attack_data():
    filename = 'C:/Users/jis99/PycharmProjects/dataset/ics-attack-v13.1.xlsx'  #mitre ics attack list
    attack_list1 = pd.read_excel(filename, sheet_name="techniques")
    table = attack_list1[['ID', 'name']]
    table_non = table.dropna(how="any")
    attack_list = table_non['name'].unique()                                   #extract mitre ics attack name list

    print("data related security threat was collected")
    # collect data related security threat
    return attack_list


