# Ransomware Playbook
# In rapid7
# Written in Sudocode

def main(step):
    prevention_and_response()
    warnings_for_ransomware_prevention()
    ransomeware_response_actions()



def prevention_and_response():
    goto User_education_training
    goto Reduce_the_attack_surface
    goto Ensure_account_permissions_are_managed_appropriately
    goto Blocking_indicators_of_the_ransomware
    goto Mitigate_spear_phishing
    goto Mitigate_drive_by_attacks
    goto Mitigate_exploitation
    goto Mitigate_replication_through_removable_media
    goto Mitigate_invalid_accounts
    goto Mitigate_execution
    goto Monitor_your_environment_for_process_related_triggers
    goto Implement_early_detection_mechanisms

    goto Removing_infected_systems_from_the_environment
    goto Restore_data_with_no_loss
    goto Issuing_new_assets


def warnings_for_ransomware_prevention():
    goto Ransomware_as_attacker_cover
    goto Don’t_get_caught_by_recency_or_news_bias


def ransomeware_response_actions():

    goto Rebuild_the_system(s)_from_a_known_good_baseline_image
    goto Scan_the_system(s)_with_an_up_to_date_anti-virus_solution
    goto Block_malicious_domain(s)_identified
    goto Terminate_the_malicious_processes
    goto Quarantine_network_traffic_from_the_affected_endpoint(s)
    goto Lock_the_affected_account(s)
    goto Change_password(s)_for_affected_account(s)
    goto Block_malicious_IP_address(es)_identified_(if_applicable)
    goto Identify_and_remove_malicious_email_from_other_inboxes_(if_applicable)
    goto Block_the_sender’s_email_address_(if_applicable)

    goto Remove_local_administrator_rights_from_a_user’s_account
    goto User_awareness_training
    goto Prevent_execution_of_Office_macros_via_Group_Policy
    goto Implement_unique_passwords_for_local_administrator_accounts_(if_applicable)
    goto Implement_application_whitelisting_for_critical_systems_(if_applicable)
    goto Separate_privileged_domain_access_from_a_standard_user_account_(if_applicable)
    goto Review_firewall_and_proxy_policies_(if_applicable)
    goto Harden_systems_by_following_industry_guidelines_(if_applicable)
    goto Prevent_activation_of_OLE_packages_in_Word_documents_(if_applicable)

