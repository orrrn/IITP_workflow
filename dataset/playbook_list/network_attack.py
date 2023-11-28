# Network Attack - an attempt to gain unauthorized access to an organization’s network,  with the objective of stealing data or perform other malicious activity
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
    #intrusion detection systems
    goto ensure_that_the_monitoring_tools_are_up_to_date
    goto establish_contacts_with_your_network_and_security_operation_teams
    goto make_sure_that_an_alert_notification_process

    #Network
    goto make_sure_that_an_inventory_of_the_network_access_points
    goto make_sure_that_network_teams_have_up_to_date_network_maps_and_configurations
    goto look_for_potential_unwanted_network_access_points
    goto ensure_that_traffic_management_tools_and_processes_are_operational

    #Baseline traffic
    goto identify_the_baseline_traffic_and_flows
    goto identify_the_business-critical_flows

def identification():
    goto sources_of_detection
    goto record_suspect_network_activity
    goto analyze_the_attack

def containment():
    goto disconnect_the_compromised_area
    goto isolate_the_source_of_the_attack
    goto find_acceptable_mitigation_measures
    goto terminate_unwanted_connections_or_processes
    goto use_firewall_IPS_rules_to_block_the_attack
    goto use_IDS_rules_to_match_with_this_malicious_behaviour_and_inform_technical_staff
    goto apply_ad_hoc_actions

def remediation():
    goto block_the_source
    goto technical_remediation
    goto test_and_enforce

def recovery():
    goto ensure_that_the_network_traffic_is_back_to_normal
    goto re-allow_the_network_traffic
    goto reconnect_sub_areas_together
    goto reconnect_the_area_to_your_local_network
    goto reconnect_the_area_to_the_Internet

def lessons_learnt():
    goto report
    goto capitalize

