# This Playbook covers the steps to take in case of Data Loss / Data Breach.
# In Incident Response Playbook From Syntax IR Playbook
# Written by Sudocode

def preparation():
    goto create_and_maintain_a_list_of_all_domains
    goto create_and_maintain_a_list_of_all_peoples
    goto create_email_templates_to_notify_all_employee
    goto create_email_templates_to_connect_hosting_companies
    goto create_email_templates_to_inform_third_party
    goto ensure_that_mail_anti_malware_and_spam_and_phish
    goto ensure_that_users_know_how_to_report
    goto ensure_that_detection_exists
    goto perform_firedrill
    goto review_threat_intellgence
    goto ensure_appropriate_access

def detect():
    start()
    goto identify_threat_indicators_using_alerts_and_notifications
    goto identify_risk_factors_using_common_and_Org_specific
    goto data_collection
    goto categorize
    if ransomware:
        goto ransomware_playbook
    else:
        goto triage
        if false positive:
            stop()
        else:
            analyze()

def analyze():
    goto verify
    if critical_incident:
        goto run_critical_playbook
    goto identify_IOCS
    if malware involve:
        goto run_malware_playbook
    goto what_was_accessed
    goto update_scope
    if all_affected_accounts_and_domain:
        if we need external_help:
            if we need technical_help:
                goto contact_IR_Pro
            if we need legal_help:
                goto contact_breach_coach
        goto root_cause_analysis
        goto send_communication
        contain()
    else:
        goto scope_validation
        go back to analyze()

def contain():
    if compromised_credential:
        goto rotate_password
    if compromised_lost_MFA:
        goto revoke_and_replace_token
    if customer_data:
        goto contact_customers
    if data_posted_to_internet:
        goto ask_onwer_to_remove_data
    if insider_threat:
        goto inform_HR_and_disable_accounts
    if attacker have access:
        goto malware_playbook
    else:
        goto close_monitoring
        if all_affected_data_lost_addressed:
            goto recover
        else:
            if new_data_lost discoverd:
                goto analyze
            else:
                go back to contain()

def recover():
    goto rebuild_systems
    goto vulnerability_scan
    goto update_defenses
    goto restore_service
    if all_affected_endpoints_ID:
        goto post_incident()
    else:
        goto data_collection
        go back to recover()

def post_incident():
    goto incident_review
    goto update_mode_of_operations
    goto review_defensive_posture
    goto build_new_detection
    goto modify_base_images
    goto user_awareness_training
    goto calculate_incidents_cost