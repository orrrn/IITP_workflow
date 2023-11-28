# Data Theft in Incident Response Playbook from Incident Response Consortium
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
        goto large_data_dumps_of_databases_network_shares_or_other_computer_systems
        goto identification_or_publication_of_proprietary_information_outside_the_organization
        goto emails_returned_as_undeliverable_due_to_size_limitations
        goto local_disk_or_network_shares_that_are_near_full_capacity
        goto notification_of_extortion_in_order_to_recover_stolen_data
        goto reporting_of_large_emails_being_sent_by_a_single_user
        goto work_performed_outside_of_normal_business_hours
        goto reports_of_removable_and_or_mobile_devices_being_used_to_copy_data
    endif

    goto categorize_incident
    goto request_packet_capture
    goto conduct_scans

def analyze():
    if define_risk_factors is is_custom:
        goto custom_factors
        risk_factors is custom
    else define_risk_factors is is_standard:
        goto extenral_user_PII_or_other_protected_information_has_been_stolen
        goto internal_user_PII_or_other_protected_information_has_been_stolen
        goto stolen_data_damaging_to_business_operations_or_brand_of_the_organization
        goto PII_or_other_protected_information_has_been_compromised
        goto compliance_requlations_have_been_violated
        goto public_or_personnel_safety_affected
        goto customers_are_affected_by_this_incident
        goto product_goods_services_are_affected_by_this_attack
        goto ability_to_control_record_measure_track_any_significant_amounts_of_inventory_products_cash_revenue_is_lost
        goto there_is_indication_of_who_perfomred_the_data_theft
        goto there_is_internal_knowledge_of_this_incident
        goto there_is_external_knowledge_of_this_incident
        goto identify_worst_case_business_impact_if_unable_to_mitigate_this_attack
        goto identify_business_operations_that_may_be_affected_and_identify_any_alternate_courses
        goto identify_business_implications_of_the_data_theft
        goto identify_additional_technical_implications_of_the_data_theft
        goto determine_risk_of_the_stolen_data_being_released_to_the_public
    endif

    goto determine_path_methods
    goto log_collection
    goto evidence_collection
    goto data_capture
    goto analysis

def contain():
    goto identify_the_systems_that_have_been_affected(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_user_credentials_compromised_or_at_risk(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_method_used_to_steal_data
    goto identify_systems_used_to_steal_data
    goto identify_any_source_attribution_collected(select_database, incident_database, vulnerability_logs, threat_database, system_logs, query_databases, generate_report)
    goto identkfy_lateral_movement_of_compromised_users_throughout_enterprise(view_report,view_record_details, select_records, copy_record_details)
    goto identify_the_tools_used_to_detect_the_attack(SIEM, IDS, firewall, scanners, antivirus, removable_device_monitors)

def eradicate():
    if triage_and_confirm_incident_report is true:
        goto request_system_patch
        goto test_code
        goto contain_malicious_code_sample
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
        goto add_change_remove_affected_system_site_network
        goto perform_data_forensics
        goto determine_method_of_removing_data_from_the_organizations_enterprise_network
    endif

    if monitor_network_traffic_for_ongoing_theft:
        goto create_alert_signatures_for_suspected_data_exfiltration
        goto prepare_to_temporarily_scan_or_block_all_outbound_data_more_than_mb_in_size
        goto implement_device_control_monitoring_and_control_systems
    endif

def recover():
    if recover_systems is true:
        goto reimage
        goto IDS_and_IPS_and_firewall_updates
        goto identify_ways_to_mitifate_further_removal_of_data
    endif

    if incident_remediation is true:
        goto wipe_and_baseline_system
        goto scan_host_with_updated_signature
        goto scan_file_share_with_updated_signature
        goto remove_vulnerabilities_and_update_routers
        goto coordinate_AV_updates_to_be_pushed_upon_release_from_AV_vendor
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
