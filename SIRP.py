import SOA
import pandas as pd
import openpyxl




# filename = './dataset/ics-attack-playbook-list1-v13.1.xlsx'  # mitre ics attack list
# playbook_list_tmp = pd.read_excel(filename, sheet_name="playbook_list")
# pbtable = playbook_list_tmp[['ID', 'playbook name', 'playbook existence']]
# pbtable_non = pbtable.dropna(how="any")
# playbook_list = pbtable_non['playbook existence'].unique()  # extract mitre ics attack name list

filename = './dataset/ics-attack-playbook-list1-v13.1.xlsx' # mitre ics attack list
playbook_list_tmp = pd.read_excel(filename)
pbtable = playbook_list_tmp[['ID', 'playbook name', 'playbook existence']]
pbtable_non = pbtable.dropna(how="any")
playbook_name_list = pbtable_non['playbook name'].unique()  # extract mitre ics attack name list
playbook_exist_list = pbtable_non['playbook existence'] #.unique()
playbook_list = list(zip(playbook_name_list, playbook_exist_list))
print(playbook_list)



def sirp_generate_playbook():
    print("generate_playbook")
    sirp_add_playbook()

def sirp_add_playbook():
    print("add new playbook at playbook list")
    # add new playbook at playbook[] list

def sirp_match_playbook(case):
    print("matching playbooks...")

    # maching playbook lists using for(iterate)

    for i in playbook_list:
        if case[1] == i:
            case[3] = 1 # playbook exists and set classification available
            break
        else:
            case[3] = 0 # playbook does not exists and set classification unavailable

    # maching playbook lists

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
