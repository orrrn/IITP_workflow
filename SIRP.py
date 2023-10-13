import SOA
import Passive
import TIP
import pandas as pd
import openpyxl


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

    return playbook_list


def sirp_generate_playbook(case):
    print("generate_playbook")

    return case

#     return case

# def sirp_add_playbook(case):
#     print("add new playbook at playbook list")
#     return case
#     # add new playbook at playbook[] list

def sirp_match_playbook(case):
    print("matching playbooks...")

    # maching playbook lists using for(iterate)

    for i in range(len(sirp_playbook_data())):
        if case[1] == sirp_playbook_data()[i][1]:
            case[4] = 1 # playbook exists
            break

        else:
            case[4] = 0 # playbook does not exists

    # maching playbook lists
    
    return case

def sirp_play_playbook(case):
    print("play this playbook..")
    # finding playbook
    
    if sirp_playbook_worked(case)[8] == 1:
        print("playbook was worked!")

    elif sirp_playbook_worked(case)[8] == 0:
        print("playbook was not worked")
        print("Additional anlyzing attack vector")
        Passive.passive_alert(case)
        Passive.passive_analyzing(case)
        Passive.passive_response_and_documentation(case)

    else:
        print("Error")

    return case


def sirp_playbook_worked(case):
    print("check the playbook worked!")
    
    return case


def sirp_playbook_can_improve(case): #check is playbook can be improve for response accident
    print("check existed playbook can improve")
    # result = SOA.soa_analyzing_more_AV(case)
    return case
