# Suspicious Logins
# In Top Security Playbook from Siemplify 
# Written in Sudocode

def main():
   #enrichment & context
   goto enrich_the_asset
   goto enrich_the_patterns

   #inversitgation
   if volumes are high:
       goto communicate_with_the_user
       goto ask_if_they_are_experiencing
    
    #containment & remediation
    goto assess_user_feedback
    goto reset_passwords
    goto ask_tem_if_the_passwod_is_strong/needs_changing
    goto block_source_IP_at_the_firewall