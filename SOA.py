import Passive
import SIRP


def soa_accident_documetation():
    print("this accident was analyzed by playbook and document this accident")


def soa_accident_improvement():
    print("based on this accident, improve security appliance and analyze corresponding playbook for improve")

    SIRP.sirp_generate_playbook()
    SIRP.sirp_add_playbook()


def soa_analyzing_more_AV(case):
    Passive.passive_analyzing()


