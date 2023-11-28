# Phshing Attack
# In Top Security Playbook from Siemplify 
# Written in Sudocode

def main():
   #enrichment & context
   goto note_the_source_and_destination_IP_address_and_ports
   goto list_all_the_email_address_against_which_the_alerts_were_found
   goto go_through_the_email_content_and_filter_out_all_URLs

   #inversitgation
   goto resolve_all_URLs_to_IPs
   goto check_the_reputation_for_each_IP
   goto analyze_URLs_in_sandboxed_environment

   if any_of_these found:
       goto mark_true_positive
       goto escalate

    #containment & remediation
    if phishing is confirmed:
        goto send_a_security_alert_email_to_entire_organization
    goto block_all_the_malicious_URLs
    goto run_thorough_anti-malware_scans