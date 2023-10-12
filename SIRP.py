import SOA
import pandas as pd
import openpyxl




# filename = './dataset/ics-attack-playbook-list1-v13.1.xlsx'  # mitre ics attack list
# playbook_list_tmp = pd.read_excel(filename, sheet_name="playbook_list")
# pbtable = playbook_list_tmp[['ID', 'playbook name', 'playbook existence']]
# pbtable_non = pbtable.dropna(how="any")
# playbook_list = pbtable_non['playbook existence'].unique()  # extract mitre ics attack name list

def sirp_playbook_data():
    filename = './dataset/ics-attack-playbook-list1-v13.1.xlsx' # mitre ics attack list
    playbook_list_tmp = pd.read_excel(filename)
    pb_table = playbook_list_tmp[['ID', 'playbook name', 'playbook existence']]
    pb_table_non = pb_table.dropna(how="any")
    playbook_ID_list = pb_table_non['ID'].unique()
    playbook_name_list = pb_table_non['playbook name'].unique()  # extract mitre ics attack name list
    playbook_exist_list = pb_table_non['playbook existence'].unique()
    playbook_list = [[ID, playbook_name, playbook_existence] for ID, playbook_name, playbook_existence in zip(playbook_ID_list, playbook_name_list, playbook_exist_list)]

    # playbook_list = list(zip(playbook_name_list, playbook_exist_list))

    return playbook_list

# def tip_attack_data():
#     filename = './dataset/ics-attack-v13.1.xlsx'  #mitre ics attack list
#     attack_list_tmp = pd.read_excel(filename, sheet_name="techniques")
#     att_table = attack_list_tmp[['ID', 'name', 'description', 'created', 'last modified', 'version', 'tactics']]
#     att_table_non = att_table.dropna(how="any")
#     attack_id_list = att_table_non['ID'].unique()
#     attack_name_list = att_table_non['name'].unique()                      #extract mitre ics attack name list
#     # attack_description_list = att_table_non['description'].unique()
#     attack_created_list = att_table_non['created'].unique()
#     attack_last_modified_list = att_table_non['last modified'].unique()
#     attack_version_list = att_table_non['version'].unique()
#     attack_tactics_list = att_table_non['tactics'].unique()        
#     # attack_list = [[ID, name, created, last_modifed, version, tactics] for ID, name, created, last_modifed, version, tactics in zip(attack_id_list, attack_name_list, attack_created_list, attack_last_modified_list, attack_version_list, attack_tactics_list)]
#     attack_list = [[ID, name] for ID, name in zip(attack_id_list, attack_name_list)]
#     # print("data related security threat was collected")
#     # collect data related security threat
#     return attack_list



def sirp_generate_playbook():
    print("generate_playbook")
    sirp_add_playbook()

def sirp_add_playbook():
    print("add new playbook at playbook list")
    # add new playbook at playbook[] list

def sirp_match_playbook(case):
    print("matching playbooks...")

    # maching playbook lists using for(iterate)

    for i in range(len(sirp_playbook_data())):
        if case[1] == sirp_playbook_data()[i][1]:
            case[4] = 1 # playbook exists and set classification available
            break
        else:
            case[4] = 0 # playbook does not exists and set classification unavailable

    # maching playbook lists

    for i in range(len(sirp_playbook_data())):     # is attack_list check
        if case[1] == sirp_playbook_data()[i][1]:
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

def sirp_play_playbook(case):
    print("play this playbook..")
    # finding playbook
    playbook = None
    isworked = 1 # if isworked is 1 means response using playbook is worked, or not is 0

    result = [case, playbook, isworked]

    return result[case, playbook]



def sirp_check_isplaybook_can_improve(case): #check is playbook can be improve for response accident
    result = SOA.soa_analyzing_more_AV(case)
