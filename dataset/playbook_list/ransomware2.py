# Ransomware
# In Top Security Playbook from Siemplify 
# Written in Sudocode

def main():
   #enrichment & context
   goto verify_the_log_source_and_locate_and_extract_the_actual_suspicious_file

   #inversitgation
   goto search_third_party_source_for_information_on_malware
   goto upload_the_suspicious_binary_to_Virustotal
   goto examine_the_detection_ratio
   
   if detectino_ratio indicates malicious_signature:
       goto escalate_to_tier2
    
    if detection_ratio indicates clean_file:
        goto make_the_case_false_positive
        goto close

   if cases is tier2:
       goto binary_file_analysis
       goto any_infected_files_to_determine_wheter_crticial
       goto vicitims_IP_and_source_IP
       goto initial_information_gathered_about_the_malware
       goto potential_impact_on_victim

    #containment & remediation
    if source_to_the_file:
        goto block
    goto disinfect_the_affected_hosts_that_were_found_during_the_enrichment_of_tier1
    goto determine_the_ransomware_used_to_see_if_recovery_will_be_possiblw
    goto determine_the_source_of_ransomware_infection
    if assest_value is high:
        goto recover_the_data
    else:
        goto reimage_the_machine