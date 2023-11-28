# Insider Threat(Data Leakage)
# In Top Security Playbook from Siemplify 
# Written in Sudocode

def main():
   #enrichment & context
   goto note_the_host_IP
   goto note_the_suspicious_attacker_IP
   goto study_the_rule_against
   goto note_the_outbound_traffic_volume_of_the_host
   goto calculate_extract_average_traffic_per_host

   #inversitgation
   if destination_IP is private:
       if destination_IP can retrieve data_from_source_IP:
           goto mark_false_positive
           goto look_for_any_previous_alerts_of_type
   if the_volume_of_data_from_locak_IP_to_remote_IP is high:
       goto mark_true_positive
       goto escalate
    
    if the_volume_of_data_from_locak_IP is around_average:
        goto mark_false_positive


    #containment & remediation
    if mark is true_positive:
        goto block_the_destination_IP_in_firewall
        goto assess_the_asset_value_based_upon_the_business_criticality_of_data