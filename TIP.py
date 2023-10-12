import random

import SIRP
import Classification_accident
import pandas as pd
import openpyxl
import numpy as np
import os


def tip_process(case):
    print("TIP Process is going..")

    if case[1] != "Normal" or "normal":
        case[2] == 1 # this is attack
    else:
        case[2] == 0 # this is not attack

    case = ["IT", "Denial of Service", 1, None, 5, None, None, None, None]

    print("Classification Accident Process is going..")

    for i in range(len(tip_attack_data())):     # is attack_list check
        if case[1] == tip_attack_data()[i][1]:
            # print(case[1])
            # print(tip_attack_data()[i][1])
            case[3] = 1             # attack classificable check (1 is able)
            SIRP.sirp_match_playbook(case)
            break
        else:
            case[3] = 0    # attack unclassificable check (0 is unable)

            # print("this is the length of list")
            # print(case[1])
            # print("--------------------------------------------")
            # print(tip_attack_data()[i][1])
            # print("this is not classificable attack")
            # print("this " + case[1] + "is not classified as" + i)

    print("TIP Process is finished")

    return case


def tip_attack_data():
    filename = './dataset/ics-attack-v13.1.xlsx'  #mitre ics attack list
    attack_list_tmp = pd.read_excel(filename, sheet_name="techniques")
    att_table = attack_list_tmp[['ID', 'name', 'description', 'created', 'last modified', 'version', 'tactics']]
    att_table_non = att_table.dropna(how="any")
    attack_id_list = att_table_non['ID'].unique()
    attack_name_list = att_table_non['name'].unique()                      #extract mitre ics attack name list
    # attack_description_list = att_table_non['description'].unique()
    attack_created_list = att_table_non['created'].unique()
    attack_last_modified_list = att_table_non['last modified'].unique()
    attack_version_list = att_table_non['version'].unique()
    attack_tactics_list = att_table_non['tactics'].unique()        
    # attack_list = [[ID, name, created, last_modifed, version, tactics] for ID, name, created, last_modifed, version, tactics in zip(attack_id_list, attack_name_list, attack_created_list, attack_last_modified_list, attack_version_list, attack_tactics_list)]
    attack_list = [[ID, name] for ID, name in zip(attack_id_list, attack_name_list)]
    # print("data related security threat was collected")
    # collect data related security threat
    return attack_list

