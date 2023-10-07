import SIRP
import TIP

def classification_accident_process(case):
    print("Classification Accident Process is going..")
    print(case)

    for i in TIP.tip_attack_data():     # is attack_list check
        if case[1] == i:
            print("this is classificable attack")
            case[2] = 1
            SIRP.sirp_match_playbook(case)
            break
        else:
            #print("this is not attack")
            case[2] = 0

    case = SIRP.sirp_match_playbook(case)


    # if case[3] == 1:
    #     # print("this accident can be clssificated")
    #     result = case[3]
    #     return case[3]
    #
    # else:
    #     # print("this accident can not be classificated")
    #     return case[3]

    return case

def classification_accident_risk(case):
    print("Classification Accident Risk and Anaysis Attack Range")

    if case[4] <= 2:
        print("This Accident's Risk is Major to Critical")

        risk = 1 #if risk is high

    elif 2 < case[4] <= 5:
        print("This Accident's Risk is Minor to Advisory")
        SIRP.sirp_play_playbook(case)

        risk = 0 #if risk is low
    else:
        print("The Risk is wrong. This is Error.")


    return isrisky[case, risk]