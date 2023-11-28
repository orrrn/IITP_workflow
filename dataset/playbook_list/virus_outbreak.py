# Virus Outbreak in Incident Response Playbook from Incident Response Consortium
# Written in Sudocode

def main(step):
    prepare()
    detect()
    analyze()
    contain()
    eradicate()
    recover()
    post_incident_handling()

def prepare():
    if vulnerability_manager | threat_manager | risk_manager : # Determine Core Ops Team & Define Roles
        if executive_lead | professional_services_lead | response_support : # Determine Extended Team
            if define_escalation_path is internal_path:
                goto document
            else define_escalation_path is external_path:
                goto document
            endif
        endif
    endif

def detect():
    if define_threat_indicators is is_custom:
        goto custom_indicators
        threat_indicators is custom

    else define_threat_indicators is is_standard:
        goto discovery_of_new_and_unususal_directories_on_computer_systems
        goto addition_of_registry_keys_to_automatically_start_at_system_boot_time
        goto anti_virus_detection_notifications
        goto discovery_of_new_and_unususal_registry_keys_on_computer_systems
        goto discovery_of_unexplained_encrypted_data_files_on_computer_systems
        goto network_traffic_indicating_unusual_amounts_or_types_of_internal_traffic
        goto searching_of_remote_systems_for_keywords_strings
        goto system_being_remotely_used_to_spend_spam_or_contribute_to_a_ddos_attack
        goto unauthorized_and_unexplained_installation_of_software
        goto unexplained_computer_system_performance_issues
        goto unexplained_crashing_of_computer_systems
        threat_indicators is standard
    endif

def analyze():
    if define_risk_factors is is_custom:
        goto custom_factors
        risk_factors is custom
    else defnie_risk_factors is is_standard:
        goto PII_or_other_protected_information_has_been_compromised
        goto external_user_PII_or_other_protected_information_at_risk_of_being_exposed
        goto internal_user_PII_or_other_protected_information_at_risk_of_being_exposed
        goto ISP_and_any_other_patners_have_been_contacted_regarding_this_event
        goto public_or_personnel_safety_affected
        goto customers_are_affected_by_this_incident
        goto products_goods_services_are_affected_by_this_attack
        goto ability_to_control_record_measure_track_any_significant_amounts_of_inventory_products_cash_revenue_is_lost
        goto this_act_is_being_launched_by_unknown_entities
        goto there_is_internal_knowledge_of_this_incident
        goto worst_case_business_impact_if_unable_to_mitigate_this_attack
        goto this_act_could_be_exploited_for_criminal_activity
        goto there_is_external_knowledge_of_this_incident
        risk_factors is standard
    endif

def contain():
   goto identify_the_systems_that_have_been_affected(servers, desktop, laptop, mobile, VM, LDAP_directory)
   goto identify_user_credentials_compromised_or_at_risk(servers, desktop, laptop, mobile, VM, LDAP_directory)
   goto identify_the_IT_services_being_impacted(servers, desktop, laptop, mobile, VM, LDAP_directory)
   goto identify_additional_systems_that_are_at_risk_of_being_compromsied(servers, desktop, laptop, mobile, VM, LDAP_directory)
   goto identify_malicious_code_on_any_systems_linked_to_fraudulent_sites
   goto identify_business_impliations_of_the_attack
   goto identify_any_source_attribution_collected(select_database, incident_database, vulnerability_logs, threat_database, system_logs, query_databases, generate_report)
   goto identify_how_widespread_the_attack_has_spread(view_report,view_record_details, select_records, copy_record_details)
   goto identify_the_tools_used_to_detect_the_attack(SIEM, IDS, firewall, scanners, antivirus)

def eradicate():
    if prevent_spread is true:
        goto run_in_sandbox
        goto analyze_in_forensics
        goto block_with_anti_virus
        goto disable_services
        goto restrict_newtork
        goto adjust_firewall_rules
        goto apply_SIEM_rules
    endif

    if communications is true:
        goto conference_call
        goto intranet_meeting
        goto internet_meeting
        goto direct_phone_call
        goto in_person_meeting
        goto mobile_messaging
        goto internet_meeting
    endif

    if eradicate_malware is true:
        goto clean_with_anti_virus
        goto qurantine_with_anti_virus
        goto malware_removal_tool
        goto manual_intervention
    endif

def recover():
    if recover_systems is true:
        goto reimage
        goto rebuild
        goto remove_temporary_containment
    endif

    if recover_data is true:
        goto data_restore
        goto cloud_synchronization
    endif

def post_incident_handling():
    if lessons_uncoverd is true:
        goto discovery_meeting
        goto policy_updates_defined
        goto process_updates_defined
        goto configuration_updates_defined
    endif

    if lessons_applied is true:
        goto policies_implemented
        goto process_changes_implemented
        goto configurations_applied
    endif

    goto respond_workflow_updated
