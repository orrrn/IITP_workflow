# This is a sample Python script.
import Classification_accident
import Passive
import SIRP
import SOA
import TIP
import csv

data = list()
f = open("C:/Users/jis99/PycharmProjects/csv/ICS_MITRE_ATT&CK.csv", "r")
reader = csv.reader(f)
data = list(reader)

print(data[0])

case = [None, None, 1, None, None, None, None, None]
# 0번째 IT/OT 스트링
# 1번째 공격벡터-하위내용
# 2번째 공격여부(1이 공격, 0이 일반)
# 3번째 공격분류여부(1이 공격분류 가능, 0이 공격분류 불가능)
# 4번째 Risk 숫자 1부터 5
# 5번째 기존 플레이북 개선 여부(1가능, 2불가능, 3디폴트(초기화))
# 6번째 공격 대응 성공 여부(1가능, 2불가능, 3디폴트(초기화))
# 7번째 개선사항 유무(1필요, 2불필요, 3디폴트(초기화))

# TIP derive state of case 1
case = TIP.tip_process(case)

if Classification_accident.classification_accident_process(case)[2] == 1:
    print("this accident can be clssificated")
    if SIRP.sirp_match_playbook(case)[3] == 1: # if it is 1, playbook exists
        isrisk_res = Classification_accident.classification_accident_risk(case)

        if isrisk_res[2] == 1: #this accident is critical or major
            print("this accidenmt is critical and major")

        else:
            result = SIRP.sirp_play_playbook(case) # result[case, playbook, isworked]

            if result[2] == 1:
                print("playbook is worked!")
                SOA.soa_accident_documetation()
                SOA.soa_accident_improvement()

            else:
                print("playbook is not worked")


else:
    print("this accident can not be clssificated")
    Passive.passive_alert()
    Passive.passive_analyzing()
    Passive.passive_response_and_documentation()




# Accident(Attack) classification










