# This playbook is meant to assist in the event of a business email compromise (BEC) event. Phishing scams and BEC incidents are the number one way that ransomware attacks can break through defenses and cripple a business. This playbook gives you a step-by-step guide in responding to a BEC incident. 
# In Incident Reponse Playbook from FRESCURE
# Written in Sudocode

def main():
    #preparation
    goto determine_the_memebers_of_the_CSIRT
    goto determine_the_extended_CSIRT_members
    goto define_escalation_paths
    goto ensure_logging_levels_for_email_system_components
    goto ensure_logging_for_email_system_components

    #identification
    goto use_the_evidence_that_resulted_in_notification_of_compromise
    goto determine_inital_method_of_account_compromise
    if method_of_initial_compromise is determined:
        goto use_the_IOC
    goto review_logs_in_email_systems
    goto access_victim_email_accounts
    goto search_impacted_systems

    #Containmnet
    goto reset_all_passwords
    goto revoke_authentication_token_for_all_identified_victim_accounts
    if external_organization is identified:
        goto notify_the_organization_of_any_compromises_or_concerns
        goto block_their_related_domains
    if malware is discoverd:
        goto preserve_a_sample_of_the_malware
        goto analyze_the_malware
        goto isolate_infected_systems
    goto block_all_associated_IoCs_in_email_systems
    goto block_all_associated_IoCs_in_endpoint_protection_system

    #Eradication
    goto preserve_artifacts_systems_and_relevant_backups
    goto preserve_any_volatile_data
    if all_relevant_data_and_equipment have been preserved:
        goto replace_or_rebuild_system
    
    #recovery
    goto remediate_any_vulnerabilities
    goto reset_passwords_for_all_impacted_accounts
    goto create_replacement_accounts_and_leave_the_impacted_accounts
    goto continue_to_monitor_for_malilcious_activity
    if financial loss:
        goto consult_cybersecurity_insurance
    
    #Lessons Learned
    goto conduct_a_meeting_after_the_incident
    goto create_and_distribute_an_incident_report_to_relevant_parties
