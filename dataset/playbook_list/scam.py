# Spam - A fraudulent or deceptive act, especially armed at defrauding someone or group of their money or other valuables
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
    goto internal_contacts
    goto external_contacts
    goto raise_customer_awareness


def identification():
    goto fraudulent_scam_detection
    goto involve_appropriate_parties
    goto collect_evidence

def containment():
    goto report_the_fradulent_e-mail_content_on_spam_and_fraud_reporting_websites_partners_tools
    goto report_the_fraudulent_e-mail_content
    goto communicate_with_your_customers
    if attack is public:
        goto deploy_the_alert_and_warning_page_with_information_about_the_current_phishing_attack


def remediation():
    if there is fraudulent_web_page_related_to_the_fraud:
        goto try_to_contact_the_owner_of_the_website
    goto contact_the_hosting_company_of_the_website
    goto contact_the_e-mail_hosting_company
    if you get no_answer | no_action:
        goto call_back_and_send_e-mails_on_a_regular_basis
        
    if the_takedown_is_too_slow:
        goto contact_a_local_CERT_in_the_involved_country

def recovery():
    goto ensure_that_the_fradulent_e-mail_address
    goto keep_monitoring_the_fraudulent_websites
    goto remove_the_associated_warning_page_from_your_websites

def lessons_learnt():
    goto report
    goto capitalize