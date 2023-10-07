import SIRP
import TIP


def passive_alert():
    print("this accident has to be analyzed passively")



def passive_analyzing():
    print("this accident analyzed passively")



def passive_response_and_documentation():
    TIP.tip_attack_data()
    passive_generate_playbook()



def passive_generate_playbook():
    print("generate playbook based on passive")
    SIRP.sirp_generate_playbook()