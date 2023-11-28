# This Playbook covers the steps to take when phishing.
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
    else:
        goto identify_IOCs
        goto scan_enterprise
        goto what_was_accessed
        goto upate_scope
        if all_affected_endpoints_ID:
            goto send_communication
            contain()
        else:
            goto scope_validation
            go back to analyze()

def contain():
    goto block_C2_email_traffic
    goto action_taken_by_user
    if malware_infection_occured:
        goto run_malware_playbook
    else:
        goto delete_emails
        goto close_monitoring
        if all_affected_endpoinst contained:
            recover()
        else:
            if new_IOC discoverd:
                analyze()
            else:
                go back to contain()

def recover():
    goto update_defenses
    if all_affected_endpoints_ID:
        recover()
    else:
        goto data_collection
        go back to recover()

def post_incident():
    goto incident_review
    goto update_mode_of_operations
    goto review_defensive_posture
    goto user_awareness_training
    goto calcuate_incident_cost
    stop()