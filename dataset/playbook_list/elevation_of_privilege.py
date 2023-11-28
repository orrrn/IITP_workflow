# Elevation of Privilege in Incident Response Playbook from Incident Response Consortium
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
        goto review_and_maintain_timeline
    endif

    interview = interviews(user,manager,physical_security,key_stakeholders)

    if interview is internal_path:
        goto document(internal_path)
    else interview is external_path:
        goto document(external_path)
    endif


def detect():
    if define_threat_indicators is is_custom:
        goto custom_indicators
        goto two_factor_or_multi_factor
        threat_indicators is custom

    else define_threat_indicators is is_standard:
        goto user_access_to_systems_outside_of_normal_business_hours
        goto increased_user_logins_to_a_computer_systems
        goto logins_to_multiple_systems_with_same_administrative_user_credentials
        goto access_to_a_computer_system_through_abnormal_ports_or_protocols
        goto exfiltration_of_data_off_of_a_computer_system
        goto installation_or_configuratino_of_unauthorized_software_or_services
        goto suspicious_network_traffic_being_initiated_from_the_internal_network
        goto user_is_unable_to_log_into_account
        goto unexplained_use_of_disabled_or_dormant_user_accounts
        goto unexplained_escalation_of_privileges_of_user_accounts
        goto unexplained_system_failures_or_restarts
        goto unexplained_emails_from_user_accounts
        goto unexplained_modifications_to_system_settings
        goto unexplained_modifications_or_destruction_of_user_files
        goto unauthorized_creation_of_new_user_accounts
        goto alerting_from_firewall_and_intrusion_detection_systems
        goto notification_from_outside_organizations    
        threat_indicators is standard
    endif

    goto categorize_incident
    goto request_packet_capture
    goto conduct_scans

def analyze():
    if define_risk_factors is is_custom:
        goto custom_indicators
        risk_factors is custom
    else define_risk_factors is is_standard:
        goto public_or_personnel_safety_affected
        goto customers_are_affected_by_this_incident
        goto employees_are_affected_by_this_comrpomise
        goto products_goods_services_are_affected_by_this_compromise
        goto ability_to_control_record_measure_track_any_significant_amounts_of_inventory_products_cash_revenue_has_been_lost
        goto this_act_is_being_launched_by_known_entities
        goto there_is_internal_knowledge_of_this_incident
        goto there_is_external_knowledge_of_this_incident
        goto worst_case_business_impact_if_unable_to_mitigate_this_attack
        risk_factors is standard
    endif

    goto determine_path_methods
    goto log_collection
    goto evidence_collection
    goto data_capture
    goto analysis


def contain():
    goto identify_the_systems_that_have_been_accessed_or_are_at_risk(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_systems_to_be_taken_off_line_due_to_compromise(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_systems_locked_out_due_to_repeated_login_attempts(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_systems_with_outage_or_degradation_of_services(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_user_accounts_compromised_or_modified
    goto identify_IT_services_impacted
    goto identify_unauthorized_tools_used_to_access_systems_or_user_accounts(select_database, incident_database, vulnerability_logs, threat_database, system_logs, query_databases, generate_report)
    goto identify_any_source_attribution_collected(view_report,view_record_details, select_records, copy_record_details)
    goto identify_the_tools_used_to_detect_the_attack(SIEM, IDS, firewall, scanners, antivirus, network_monitoring_tools)

def eradicate():
    if triage_and_confirm_incident_report is true:
        goto request_system_patch
    endif

    if communications is true:
        goto direct_phone_call
        goto conference_call
        goto intranet_meeting
        goto internet_meeting
        goto in_person_meeting
        goto mobile_messaging
    endif

    if eradicate_malware is true:
        goto add_cahnge_remove_affected_systems_site_network
        goto perform_data_forensics
        goto determine_level_of_access_to_identified_system
    endif

    if deploy_network_collection_sensors_to_capture_traffic_for_further_analysis is true:
        goto determine_any_lateral_movement_between_systems_within_the_network
    endif

def recover():
    if recover_systems is true:
        goto reimage
        goto IDS_and_IPS_and_firewall_updates
        goto determine_alternate_network_ingress_and_egress_solutions_if_malware_causes_DoS
    endif

    if incident_remediation is true:
        goto scan_host_with_updated_signature
        goto scan_file_share_with_updated_signature
        goto remove_vulnerabilities_and_update_routers
    endif
    
def post_incident_handling():
    if incident_review is true:
        goto is_electronic_personal_health_information_compromised
        goto is_sensitive_government_information_compromised
    endif

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