# Improper Computer Usage in Incident Response Playbook from Incident Response Consortium
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
        threat_indicators is custom

    else define_threat_indicators is is_standard:
        goto excessive_amount_of_web_browising_traffic_or_downloads
        goto identification_of_large_emails_being_sent_or_received_by_a_user
        goto increase_in_spam_delivered_to_users_email_account
        goto notification_from_other_employees_partners_or_vendors
        goto unexplained_malware_adware_spyware_or_virus_infections_on_computer_systems
        goto use_of_unauthorized_communications_methods_or_netwokrs_protocols
        goto web_filtering_alerts_of_access_or_attempted_access_to_unauthorized_websites
        threat_indicators is standard
    endif

    goto categorize_incident
    goto request_packet_capture
    goto conduct_content_scans


def analyze():
    if define_risk_factors is is_custom:
        goto custom_indicators
        risk_factors is custom
    else define_risk_factors is is_standard:
        goto internal_user_PII_or_other_protected_information_has_been_stolen
        goto external_user_PII_or_other_protected_information_has_been_stolen
        goto PII_or_other_protected_information_been compromised
        goto public_or_personnel_safety_affected
        goto customers_are_affected_by_this_incident
        goto products_goods_services_are_affected_by_this_compromise
        goto ability_to_control_record_measure_track_any_significant_amounts_of_inventory_products_cash_revenue_has_been_lost
        goto there_is_internal_knowledge_of_this_incident
        goto there_is_external_knowledge_of_this_incident
        goto worst_case_business_impact_if_unable_to_mitigate_this_attack
        goto system_has_been_affected
        goto data_has_been_compromised
        goto IT_services_are_impacted
        goto vulnerability_or_services_have_been_exploited
        risk_factors is standard
    endif

    goto determine_path_methods
    goto log_collection
    goto evidence_collection
    goto data_capture
    goto analysis


def contain():
    goto identify_the_systems_that_have_been_affected(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_user_credentials_compromised_or_at_risk(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_any_malicious_code_on_any_systems(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_types_of_network_protocols_being_utilized(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_means_and_methods_used_by_the_suspected_offender
    goto identify_any_persons_that_may_have_received_data_from_suspect
    goto determine_where_residual_data_may_remain_related_to_this_suspected_offense(select_database, incident_database, vulnerability_logs, threat_database, system_logs, query_databases, generate_report)
    goto identify_any_undiscoverd_suspicious_files_programs_or_data(view_report,view_record_details, select_records, copy_record_details)
    goto identify_the_tools_used_to_detect_the_misuse(SIEM, IDS, firewall, scanners, antivirus, network_monitoring_tools)


def eradicate():
    if triage_and_confirm_incident_report is true:
        goto request_network_configuration_updates
        goto request_endpoint_policy_updates
    endif

    if HR_employee_communications is true:
        goto direct_phone_call
        goto conference_call
        goto intranet_meeting
        goto internet_meeting
        goto in_person_meeting
        goto mobile_messaging
    endif

    if eradicate_malware is true:
        goto warn_the_employess
        goto add_change_remove_affected_system_site_network
        goto perform_data_forensics
    endif


def recover():
    if recover_systems is true:
        goto reimage
        goto IDS_and_IPS_and_firewall_updates
        goto apply_network_monitoring_system_updates
    endif

    if incident_remediation is true:
        goto wipe_and_baseline_system
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

