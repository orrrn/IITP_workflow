# Phishing in Incident Response Playbook from Incident Response Consortium
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
        goto emails_returned_my_mail_servers_as_identified
        goto emails_that_have_been_linked_to_external_or_unknown_URLs
        goto identification_of_spoofed_email
        goto emails_that_are_non_returnable_or_non_deliverable
        goto monitoring_of_organization_websites_to_identify_attempts_or_copy_web_content_or_perform_web_scrapping
        goto notification_from_internal_users_of_suspicious_or_fradulent_activity_related_to_emails
        goto notification_from_external_users_or_customers_of_suspicious_or_fraudulent_activity_related_to_emails
        goto notification_from_3rd_parties_of_suspicious_or_fradulent_activity_related_to_emails
        goto notification_from_law_enforcement_suspicious_or_fradulent_activity_related_to_emails
        goto notification_from_ISP_of_increased_amount_of_email_or_web_traffic
        threat_indicators is standard
    endif

    goto categorize_incident
    goto request_packet_capture
    goto conduct_content_scans

def analyze():
    if define_risk_factors is is_custom:
        goto custom_factors
        risk_factors is custom
    else define_risk_factors is is_standard:
        goto internal_user_PII_or_other_protected_information_at_risk_of_being_exposed
        goto external_user_PII_or_other_protected_information_at_risk_of_being_exposed
        goto PII_or_other_protected_information_has_been_compromised
        goto IST_and_any_other_partners_have_been_contacted_regarding_this_event
        goto public_or_personal_safety_affected
        goto customers_are_affected_by_this_incident
        goto products_goods_services_are_affected_by_this_attack
        goto ability_to_control_record_measure_track_any_significant_amounts_of_inventory_products_cash_revenue_has_been_lost
        goto this_act_is_being_launched_by_known_entities
        goto there_is_internal_knowledge_of_this_incident
        goto worst_case_business_impact_if_unable_to_mitigate_this_attack
        goto this_act_could_be_exploited_for_criminal_activity
        goto there_is_external_knowledge_of_this_incident
        risk_factors is standard
    endif

    goto dertermine_patch_methods
    goto log_collection
    goto evidence_collection
    goto data_capture
    goto analysis
    
def contain():
   goto identify_the_systems_that_have_been_affected(servers, desktop, laptop, mobile, VM, LDAP_directory)
   goto identify_user_credentials_compromised_or_at_risk(servers, desktop, laptop, mobile, VM, LDAP_directory)
   goto identify_the_IT_services_being_impacted(servers, desktop, laptop, mobile, VM, LDAP_directory)
   goto identify_additional_systems_that_are_at_risk_of_being_compromsied(servers, desktop, laptop, mobile, VM, LDAP_directory)
   goto identify_malicious_code_on_any_systems_linked_to_fraudulent_sites
   goto identify_business_implications_of_the_attack
   goto identify_any_source_attribution_collected(select_database, incident_database, vulnerability_logs, threat_database, system_logs, query_databases, generate_report)
   goto identify_how_widespread_the_attack_has_spread(view_report,view_record_details, select_records, copy_record_details)
   goto identify_the_tools_used_to_detect_the_attack(SIEM, IDS, firewall, scanners, antivirus, span_filter)

def eradicate():
    if triage_and_confirm_incident_report is true:
        goto request_system_patch_rule_update_or_content_filter_modification
        goto test_implementation
        goto contain_phishing_sample
        goto test_malware_eradication_procedure
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
        goto coordinate_technical_counter_measure_and_url_redirect_with_ISP
        goto coordinate_with_3rd_party_take_down_service
    endif

def recover():
    if recover_systems is true:
        goto reimage
        goto IDS_and_IPS_and_firewall_updates
        goto remove_temporary_containment
        goto email_filter_action
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
