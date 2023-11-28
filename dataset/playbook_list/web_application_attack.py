# In responding to a web application compromise incident, also be used for a website defacement incident.
# In Incident Reponse Playbook from FRESCURE
# Written in Sudocode

def main():
    #preparation
    goto determine_the_memebers_of_the_CSIRT
    goto determine_the_extended_CSIRT_members
    goto define_escalation_paths
    goto ensure_logging_levels_for_account_login_system
    goto ensure_logging_for_account_login_system
    goto ensure_that_web_application_backups

    #identification
    if web_application is hosted on_another_service:
        goto contact_the_hosting_sevice_to_report_the_issue
    goto use_the_evidence_that_reulsted_in_notification_of_compromise_to_determine_next_steps
    goto determine_inital_method_of_account_compromise
    if initial_compromise is determined:
        goto use_the_IoCs
    goto review_log_in_account_log_systems
    goto assess_victims_accounts_to_determine
    goto use_the_information_gathered
    if account_compromise has been ruled out:
        goto proceed_to_investigate_potential_web_application_vulnerabilities
    
    #Containment
    if management_or_administrative_account_compromise has been determined:
        goto reset_all_passwords
        goto enable_multi-factor_authentication
        goto disable_or_reset_alternative_authentication
        goto revoke_authentication_tokens
    if external_organization is identified:
        goto notify_the_organization_of_any_compromises_or_concerns
    if malware is discoverd:
        goto preserve_a_sample_of_the_malware
        goto analyze_the_malware
        goto isolate_infected_systems
    goto block_all_associated_IoCs
    goto preserve_a_copy_of_any_existing_web_applicatino_code

    #Eradication
    goto compare_current_web_application_code
    if system were determined:
        goto preserve_artifacts_systems_and_relevant_backups
    goto preserve_any_volatile_data
    goto review_any_monitor_logs
    if all_relevant_data_and_equipment have been preserved:
        goto recovery
    
    #recovery
    goto replace_potentially_compromised_web_application_code
    goto review_current_web_application_code
    goto restore_web_application
    goto restore_impacted_systems_from_a_clean_backup
    goto rebuild_the_machines
    goto remediate_any_vulnerabilities_and_gaps_identified
    goto reset_passwords_for_all_impacted_accounts
    goto create_replacement_accounts_and_leave_the_impacted_accounts
    goto continue_to_monitor_for_amlicious_activity

    #lessons learnd
    goto conduct_a_meeting_after_the_incident
    goto create_and_distribute_an_incident_report
