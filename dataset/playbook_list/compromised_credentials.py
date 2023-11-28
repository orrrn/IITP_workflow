# In responding to credential_theft_incident
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
    goto use_the_evidance
    goto determine_inital_method_of_account_compromise
    goto search_for_phishing_emails
    goto search_for_emails_with_links
    goto search_the_users_web_history
    goto search_for_potential_malware
    if method_of_initial_compromised is determined:
        goto use_the_IoCS
    goto review_logs_in_account_login_systems
    goto assess_vicitim_accouonts
    goto use_the_information

    #containment
    goto reset_all_passwords
    goto enable_multi_factor_authentication
    goto disable_user_accounts
    goto revoke_authentication_token
    if external_organization is identified:
        goto notify_the_organization_of_any_compromise_or_concerns
        goto block_their_related_domains_from_sending_email
    if malware is discoverd:
        goto preserve_a_sample
        goto analyze_the_malware
        goto isolate_infected_systems
        goto block_all_associated_IoCs_in_email_system
    
    #eradication
    goto preserve_artifacts_systems_and_relevant_backups
    goto preserve_any_volatile_data
    if all_relevant_data_and_equipment have been preserved:
        goto replace_or_rebuild_systems
    
    #recoveory
    goto restore_impacted_systems
    goto rebuild_the_machine_from_a_known_good_images
    goto remediate_any_vulnerabilities_and_gaps_identified
    goto reset_passwords_for_all_impacted_accounts
    goto continue_to_monitor

    
    #lessons learnd
    goto conduct_a_meeting_after_the_incident
    goto create_and_distribute_an_incident_report