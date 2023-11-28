# DoS - A Distributed Denial Of Service that makes the targeted services  unavailable for its legitimate users by flooding the network with  illegitimate traffic
# In IRM Playbook
# Written in Sudocode

def main():
    preparation()
    identification()
    containment()
    remediation()
    recovery()
    lessons_learnt()

def preparation():
    #intenret service provider support
    goto contact_your_ISP
    goto subscribe_to_a_redundant_internet_connection
    goto subscribe_to_an_Anti_DDoS_service_provider
    goto establish_contacts_with_your_ISP_and_law_enforcement_entities

    #Inventory
    goto create_a_whitelist_of_the_IP_addresses_and_protocols
    goto document_your_IT_infrastructure_details

    #Network Infrastructure
    goto design_a_good_network_infrastructure
    goto distribute_your_DNS_servers_and_other_critical_services
    goto harden_the_configuration_of_network_OS_and_application_components
    goto baseline_your_current_infrastructures_performance
    goto consider_purchasing_specialized_DDoS_mitigation_products
    goto confirm_DNS_TTL_seetings
    goto consider_settting-up_a_backup

    #Internal Contacts
    goto establish_contacts_for_your_IDS_firewall_systems_and_network_teams
    goto collaborate_with_the_business_lines
    goto involve_your_BCP/DR_planning_team

def identification():
    #analse the attack
    goto understand_the_logical_flow_of_the_DDoS_attack
    goto identify_the_infrastructure_components
    goto understand_if_you_are_the_target_of_the_attack
    goto review_the_load_and_log_files
    goto identify_what_aspects_of_the_DDoS_traffic
    goto create_a_NIDS_signature

    #Involve internal and external actors
    goto contact_your_internal_temas
    goto contact_your_ISP_to_ask_for_help
    goto notify_your_company_executive_and_legal_teams

    #Check the background
    goto find_out_whether_the_company_received_an_extortion_demand
    goto search_if_anyone_would_have_any_interest
    
def containment():
    if bottleneck is feature_of_an_application:
        goto temporarily_disable_that_feature
    goto attempt_to_throttle_or_block_DDoS_traffic
    goto terminate_unwanted_connections_or_processes
    goto switch_to_alternate_sites_or_networks_using_DNS_or_another_mechanism
    goto set_up_an_alternate_communicatinos_channel
    goto route_traffic_through_a_traffic-scrubbing_service_or_product
    goto configure_egress_filters_to_block_the_traffic_your_systems
    goto try_to_buy_time_with_the_fraudster

def remediation():
    goto contact_your_ISP_and_make_sure_that_it_enfores_remediation_measures
    if DDoS_sponsors have been identified:
        goto consider_involoving_law_enforcement

def recovery():
    goto assess_the_end_of_the_DDoS_condition
    goto rollback_the_mitigation_measures


def lessons_learnt():
    goto report
    goto capitalize
