# Incident Response Playbook - Ransomware Infection
# In DFIR Playbook
# Written in Sudocode

def safeguard():
    goto mature_patch_management
    goto endpoint_protection
    goto network_segmentation
    goto backup_strategy
    goto restrict_administrative_accounts
    goto security_applicances

    #endpoint_hardening
    goto use_endpoint_hardening_checklists
    goto remove_old_and_unpatched_systems
    goto disable_SMBv1_and_SNMP_and_Windows_script_host_and_office_macro
    goto make_sure_to_retrict_communication
    goto disable_USB
    goto enable_windows_applocker
    goto enable_microsoft_defender_controller_folder_access
    goto enable_system_logging
    goto disable_WSH

    goto vulnerability_management
    goto restrict_access_to_management_interfaces
    goto awareness_trainings
    goto VPN

def preparation():
    goto network_orchestration_tools
    goto IoC_scans_for_network_traffic_and_hosts
    goto network_segmentation_and_quarantine
    goto central_log_management
    goto enhance_your_logging
    goto network_and_business_knowledge
    goto mock_incidents
    goto ransom_payment_policy
    goto upfront_decisions
    goto user_and_service_desk_awareness
    goto insurance

def detection_and_discovery():
    goto ransomware_notes
    goto encrypted_files
    goto unusual_high_load
    goto anti-virus_or_IDS_events
    goto beacon_file_monitoring
    goto user_reports
    goto network_traffic
    goto abused_accounts
    goto unusual_executables_or_processes
    goto documentation

def containment_and_mitigation():
    goto reset_or_lock_compromised_accounts
    goto secure_uninfected_systems
    goto encapsulation_of_infected_subnets_and_systems
    goto pausing_of_infected_or_potential_infected_VMs
    goto shutdown_of_infected_or_potential_infected_systems
    goto disconnect_shared_drives
    goto restrict_or_disable_internet_connection_for_infected_segments
    goto check_back_up_availability
    goto secure_needed_data
    goto communication_internal_and_external
    goto documentation

def analysis():
    goto determine_the_ransomware_malware_type
    goto determine_the_attack_vector
    goto gather_information_about_the_malware_that_was_deployed_and_their_damage_potential
    goto determine_the_scope_of_the_attack
    goto timeline
    goto check_for_backdoors
    goto documentation

def remediation():
    goto close_the_attack_vector
    goto patching
    goto IoC_search_the_whole_infrastructure
    goto remove_backdoors_and_other_malware_from_the_systems
    goto adjust_firewall_IDS_AV
    goto documentation

def recovery():
    goto rebuild_or_cleanse_infected_systems_in_a_new_network_zone
    goto rebuild_the_domain
    goto recover_data_from_known_good_backups
    if no other way can be found:
        goto pay_the_ransom
    goto address_collateral_damage
    goto ensure_that_network_traffic_is_back_to_normal
    goto documentation

def post_morten():
    goto review_the_incident_response_process
    goto discuss_security_enhancements
    goto conduct_external_reviews
    goto determine_incident_cost
