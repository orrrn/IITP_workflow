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

print(data[2])

case = data[2]

# TIP derive state of case 1
case = TIP.tip_process(case)
print(case)

if case[2] == 1:
    print("this accident can be clssificated")
    if SIRP.sirp_match_playbook(case)[3] == 1: # if it is 1, playbook exists
        isrisk_res = Classification_accident.classification_accident_risk(case)

        if isrisk_res[1] == 1: #this accident is critical or major
            print("this accidenmt is critical and major")
            print(isrisk_res[0])
            print(isrisk_res[1])
        else:
            print("isit?")
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










