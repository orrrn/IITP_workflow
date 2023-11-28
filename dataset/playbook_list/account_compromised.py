# This Playbook covers the steps to take when accounts are compromised.
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
    goto identify_and_obtain_the_services
    goto define_threat_and_risk_indicators_and_alerting_pattern

def detect():
    start()
    goto identify_threat_indicators_using_alerts_and_notifications
    goto identify_risk_factors_using_common_and_Org_specific
    goto data_collection
    goto triage
    if false positive:
        stop()
    else:
        analyze()

def analyze():
    goto verify
    goto list_of_affected_credentials
    goto level_of_access_and_prviledge
    if critical_incident:
        goto critical_playbook
    if domain_compromised:
        goto disable_trust_with_infected_domain
    if live_threat_actor:
        goto monitor_closely_all_systems
    if we have backup:
        goto ensure_backups_are_protected
    goto log_analysis
    if password reused:
        goto update_scope
    if TOTP stored in pass_manager:
        goto update_scope
    if MFA compromised:
        goto update_scope
    if data exfiltrated:
        goto data_loss_playbook
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
        goto update_scope
        goto scope_validation
        go back to analyze()

def contain():
    goto disable_accounts
    goto reset_password
    goto powerdown_NON_encrypted_systems
    goto restrict_priviledges
    goto remove_cashed_credentials
    goto contain_endpoint
    goto block_network_traffic
    if all_affected_endpoints_contained:
        goto recover()
    else:
        if new_IOC_discoverd:
            analyze()
        else:
            goto update_scope
            go back to contain()

def recover():
    goto update_defenses
    goto change_all_passwords
    goto remove
    goto rebuild_systems
    goto restore_data
    goto audit_internet_facing_services
    if all_affected_endpoints_contained:
        goto post_incident()
    else:
        go back to recover()

def post_incident():
    goto incident_review
    goto update_policies_and_procedures
    goto review_defensive_posture
    goto update_and_upgrade_defences
    goto build_new_detections
    goto modify_base_image
    if incident cause by human:
        goto user_awareness_training
    goto calculate_incident_cost
    stop()