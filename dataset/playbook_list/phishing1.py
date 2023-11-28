# Phishing - The fraudulent practice of sending emails purporting to be from  reputable companies in order to induce individuals to reveal personal  information, such as passwords and credit card numbers
# In IRM Playbook
# Written in Sudocode

def main():
    preparation()
    identification()
    containment()
    remediation()
    recovery()
    lessons_learnt()

def preparation():
    goto create_a_list_of_all_legitimate_domains_belonging_to_your_company
    goto prepare_one_web_page_hosted_on_your_infrastructure
    goto prepare_and_test_a_clear_deployment_procedure
    goto prepare_takedown_e-mail_forms
    goto implement_active_anti-phishing_solutions
    goto implement_a_staff_phishing_reporting_process
    goto internal_contacts
    goto external_contacts
    goto raise_customer_awareness
    goto raise_business_line_awareness

def identification():
    #phishing detection
    goto monitor_all_your_points_of_contact_closely
    goto deploy_phishing_traps_and_try_to_gather_phishing_from_partners_and_third-parties
    goto review_your_Anti-phishing_report_regularly
    goto investigate_staffs_report_of_suspicious_email
    goto monitor_your_web_logs
    goto check_there_is_no_suspicious_referrer_bringing_people_to_your_website

    goto involve_appropriate_parties
    goto collect_evidence

def containment():
    goto block_the_URL_of_the_attack_everywhere
    goto report_the_fraudulent_e-mail_content
    goto communicate_with_your_customers
    if attack is public:
        goto deploy_the_alert_and_warning_page_with_information_about_the_current_phishing_attack
    goto check_the_source-code_of_the_phishing_website
    goto see_where_the_data_is_exported
    goto watch_how_the_phishing-page_is_built

def remediation():
    goto try_to_contact_the_owner_of_the_website
    goto explain_clearly_the_fraud_to_the_owner
    goto contact_the_hosting_company_of_the_website
    goto send_e-mails_to_the_contact_addresses_of_the_hosting_company
    goto contact_the_e-mail_hosting_company
    if you get no_answer | no_action:
        goto call_back_and_send_e-mails_on_a_regular_basis
        
    if the_takedown_is_too_slow:
        goto contact_a_local_CERT_in_the_involved_country

def recovery():
    goto ensure_that_the_fradulent_pages_and_or_e-mail_address
    goto keep_monitoring_the_fraudulent_URL
    goto remove_the_associated_warning_page_from_your_websites

def lessons_learnt():
    goto report
    goto capitalize