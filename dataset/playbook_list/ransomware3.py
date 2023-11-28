# This Playbook covers various type of Ransom we could be faced with. The most common being Ransomware but we try to also account for other types.
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
    goto triage
    if false positive:
        stop()
    else:
        analyze()

def analyze():
    goto verify
    if different_than_ransomware:
        if it is DDoS:
            goto DDoS_playbook
        else:
            goto critical_playbook
    else:
        if live_threat_actor:
            goto contain_and_eradicate_found_IOC/IoA
        if we have backups:
            goto ensure_backups_are_protected
        if infected_AD trusted:
            goto disable_trust_with_infected_domain
        goto identify_threat_actor_ransom_family
        goto identify_affected_system_types
        if we pay ransom:
            goto make_payment_arrangements
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
    goto block_system_to_systems_communications
    goto stop_backups
    goto powerdown_NON_encrypted_systems
    goto disconnect_share_drives
    if malware infection:
        goto run_malware_playbook
    goto active_directory_clean_up
    goto monitor_closely
    if all_affected_endpoints contained:
        recover()
    else:
        if new_IOC discoverd:
            analyze()
        else:
            goto update_scope
            go back to contain()


def recover():
    goto rebuild_systems
    goto change_All_passwords
    goto remove
    goto rebuild_systems
    goto restore_data
    if all_affected_endpoints_ID:
        post_incident()
    else:
        go back to recover()

def post_incident():
    goto incident_review
    goto update_mode_of_operations
    goto review_defensive_posture
    goto update_and_upgrade_defences
    goto build_new_detection
    goto modify_base_images
    if incident cause by_human:
        goto user_awareness_training
    goto calculate_incidents_cost
    stop()
