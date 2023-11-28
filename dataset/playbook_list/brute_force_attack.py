# Brute Force Attacks
# In Top Security Playbook from Siemplify 
# Written in Sudocode

def main():
   #enrichment & context
   goto source_IP_address_is_it_internal_or_external
   goto target_IP_and_OS_information

   #inversitgation
   if source_IP_address is internal:
       goto search_of_any_previous_alerts_raised_on_the_entity
       if alerts involve malware_alert:
           goto escalate_Tier2
           goto block_the_traffic_from_the_source_IP
           goto disinfect_the_machine
           goto verify_the_source_of_the_malware
           goto unblock_the_machine_once_no_threats_are_found
    else source_IP_address is external:
        goto search_the_IP_using_IP_reputation_sites

    goto determine_which_data_source_was_used_to_trigger_the_alert
    goto search_network_based_logs
    goto search_host_based_logs

    #containment & remediation
    goto find_out_all_users_that_were_used_in_the_brute_force_attack
    goto notify_the_owners_of_the_lgeitimate_accounts_and_the_owners_of_the_targeted_machines
    goto perform_a_more_thorough_investigation
    if attacker is external_IP:
        goto block_it_and_ensure_that_the_firewall_is_configured_to_prevent_remote_login_attempts
    else attacker is internal_IP:
        goto search_for_any_malware_infections_and_past_malware_alerts
      