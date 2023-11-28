# This Playbook is Successful Phishing Attack abuse playbook
# In exabeam
# Written in Sudocode

def main(step):
    Identify_and_analyze_the_phishing_email()
    understand_the_scope_and_impact_of_the_attack()
    prevention()



def Identify_and_analyze_the_phishing_email():
    goto Identifying_Phishing_email
    goto Analyzing_Phishing_email
    goto Analyzing_Pertinent_details_include_links_attachments_attachment-detonation_behaviors

def understand_the_scope_and_impact_of_the_attack():
    goto check_Were_the_user_credentials_compromised
    goto check_On_which_access_points_of_Internet_presence_can_the_credentials_be_used
    goto check_is_the_user_email_account_now_being_exploited

def prevention():  
    goto Blocking_your_gateway_or_next-gen_firewall - You_can_deny_specific_links_or_the_base_URL
    goto Blocking_email_server_or_scanner - You_can_block_specific_senders_domains_attachment_types


