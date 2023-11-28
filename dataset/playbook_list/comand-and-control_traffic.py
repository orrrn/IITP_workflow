# Command-and-Control(C2) Traffic
# In Top Security Playbook from Siemplify 
# Written in Sudocode

def main():
   #enrichment & context
   goto list_all_IPs_against_which_alarm_was_raised_for_later_escalation_to_tier2

   #inversitgation
   goto gather_attack_pattern
   goto gather_any_prior_malware_alerts_about_victim_IP
   goto identify_the_CnC_servers


    #containment & remediation
    goto blacklist_all_the_identified_CnC_server_with_firewall
    goto hunt_for_any_backdoors_on_affected_host_and_remove_them
    goto hunt_for_the_origin_of_attack