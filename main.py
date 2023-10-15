# This is a sample Python script.
import Classification_accident
import Passive
import SIRP
import SOA
import TIP
import csv
import json

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

# with open("C:/Users/jis99/PycharmProjects/dataset/attack-stix-data-master/ics-attack/ics-attack-13.1.json", "r") as json_file:
#     ics_attack_data = json.load(json_file)
#     print(json.dumps(ics_attack_data, indent="\t"))



# print("1. Test of Workflow Model Acceptance")
# print("2. Test of Security Accident Response Automation")
# print("3. Test of Detection of Blended Attack using SOAR")
#
# testcase = input('Input test number : ')
#
# if testcase == '1':
#     print("Workflow Model Acceptance")
#
# elif testcase == '2':
#     print("Security Accident Response Automation")
#
# else:
#     print("Detection of Blended Attack using SOAR")

# f = open("C:/Users/jis99/PycharmProjects/dataset/ICS_MITRE_ATT&CK.csv", "r")
# reader = csv.reader(f)
# data = list(reader)햣

case = [None, None, None, None, None, None, None, None]
# 0번째 IT/OT 스트링
# 1번째 공격벡터-하위내용
# 2번째 공격여부(1이 공격, 0이 일반)
# 3번째 공격분류여부(1이 공격분류 가능, 0이 공격분류 불가능)
# 4번째 playbook 존재 여부(1이 존재, 0이 존재하지 않음)
# 5번째 Risk 숫자 1부터 5
# 6번째 기존 플레이북 개선 여부(1가능, 2불가능, 3디폴트(초기화))
# 7번째 공격 대응 성공 여부(1가능, 2불가능, 3디폴트(초기화))
# 8번째 개선사항 유무(1필요, 2불필요, 3디폴트(초기화))

# print(SIRP.sirp_playbook_data())
# TIP derive state of case 1
case = TIP.tip_process(case)





# if Classification_accident.classification_accident_process(case)[2] == 1:
#     print("this accident can be clssificated")
#     if SIRP.sirp_match_playbook(case)[3] == 1: # if it is 1, playbook exists
#         isrisk_res = Classification_accident.classification_accident_risk(case)

#         if isrisk_res[2] == 1: #this accident is critical or major
#             print("this accidenmt is critical and major")

#         else:
#             result = SIRP.sirp_play_playbook(case) # result[case, playbook, isworked]

#             if result[2] == 1:
#                 print("playbook is worked!")
#                 SOA.soa_accident_documetation()
#                 SOA.soa_accident_improvement()

#             else:
#                 print("playbook is not worked")


# else:
#     print("this accident can not be clssificated")





# Accident(Attack) classification