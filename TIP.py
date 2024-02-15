import random

import SIRP
import Passive
import Classification_accident
import pandas as pd
import openpyxl
import numpy as np
import os
#terst
#case
# 0번째 IT/OT 스트링
# 1번째 공격벡터-하위내용
# 2번째 공격여부(1이 공격, 0이 일반)
# 3번째 공격분류여부(1이 공격분류 가능, 0이 공격분류 불가능)
# 4번째 playbook 존재 여부(1이 존재, 0이 존재하지 않음)
# 5번째 Risk 숫자 1부터 5
# 6번째 Risk major or minor 여부(1이 major-플레이북 실행 전 추가분석 수행, 0이 minor-playbook 바로 실행)
# 7번째 기존 플레이북 개선 여부(1가능, 0불가능)
# 8번째 공격 대응 성공 여부(1가능, 0실패)
# 9번째 개선사항 유무(1필요, 0불필요)


def tip_process(case):
    print("TIP Process is going..")
    case = ["IT", "Denial of Service", 1, None, 5, None, None, None, None]

    if case[1] != "Normal" or "normal":
        case[2] == 1 # this is attack
    else:
        case[2] == 0 # this is not attack


    print("Classification Accident Process is going..")

    for i in range(len(tip_attack_data())):     # is attack_list check
        if case[1] == tip_attack_data()[i][1]:
            
            case[3] = 1             # attack classificable check (1 is able)
            SIRP.sirp_match_playbook(case)

            if case[4] == 1:   # playbook exist
                tip_accident_risk_eval(case)

                if case[6] == 1:  # this attack risk is major or critical
                    Passive.passive_analyzing(case) # if this attack risk is major, do additional attack analyzing.
                    SIRP.sirp_playbook_can_improve(case) # checking this attack can be handled by using exist playbook(after improving)

                    if case[7] == 1: # can using exist playbook
                        SIRP.sirp_generate_playbook(case) # generate improved playbook

                    elif case[7] == 0: # can not using exist playbook
                        Passive.passive_response_and_documentation(case)
                        Passive.passive_generate_playbook(case)

                    SIRP.sirp_match_playbook(case)
                    SIRP.sirp_play_playbook(case)

                elif case[6] == 0: # this attack risk is minor
                    SIRP.sirp_play_playbook(case)
                    
            elif case[4] == 0: #playbook doesn't exist
                Passive.passive_alert(case)
                Passive.passive_analyzing(case)
                Passive.passive_response_and_documentation(case)      
                Passive.passive_generate_playbook(case)
                SIRP.sirp_match_playbook(case)
                SIRP.sirp_play_playbook(case)

        else:
            case[3] = 0    # attack unclassificable check (0 is unable)
            Passive.passive_alert(case)
            Passive.passive_analyzing(case)
            Passive.passive_response_and_documentation(case)  
            Passive.passive_generate_playbook(case)
            SIRP.sirp_match_playbook(case)
            SIRP.sirp_play_playbook(case)          

    print(case)
    print("TIP Process is finished")

    return case

def tip_accident_risk_eval(case):
    print("Classification Accident Risk and Anaysis Attack Range")


#   how to eval the risk .. based on open source
#   how to eval the risk .. based on open source
#   how to eval the risk .. based on open source
#   how to eval the risk .. based on open source
#   how to eval the risk .. based on open source

    if case[5] <= 2:
        print("This Accident's Risk is Major to Critical")
        case[6] = 1 #if risk is major

    elif 2 < case[5] <= 5:
        print("This Accident's Risk is Minor to Advisory")
        case[6] = 0 #if risk is minor
    else:
        print("The Risk is wrong. This is Error.")
        
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

