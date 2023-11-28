# Worm Infection - a standalone malware computer program that replicates itself in order to spread to other computers
# In IRM Playbook
# Written in Sudocode

from _typeshed import IdentityFunction
import typing_extensions


def main():
    preparation()
    identification()
    containment()
    remediation()
    recovery()
    lessons_learnt()

def preparation():
    goto define_actors
    goto make_sure_that_analysis_tools_are_up
    goto make_sure_to_have_architecture_map_of_your_networks
    goto perform_a_continuous_security_watch_and_inform_the_people

def identification():
    goto detection_the_infection
    goto identify_the_infection
    goto assess_the_perimeter_of_the_infection

def containment():
    goto disconnect_the_infected_area_from_the_internet
    goto isolate_the_infected_area
    goto allow_it_after_ensuring
    goto neutralize_the_propagation_vectors

def remediation():
    goto identify
    goto test
    goto deploy

def recovery():
    goto reopen_the_network_traffic
    goto reconnect_sub_areas_together
    goto reconnect_mobile_laptos_to_the_area
    goto reconnect_the_area_to_your_local_network
    goto reconnect_the_area_to_the_Internet

def lessons_learnt():
    goto report
    goto capitalize