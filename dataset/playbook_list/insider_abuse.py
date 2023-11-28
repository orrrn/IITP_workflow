# Insider Abuse - deliberate abuse of the organization's systems by an authorized user
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
    goto contacts

def identification():
    #technical identification
    goto alerts_from_a_SIEM_or_correlation_tools
    goto alerts_from_an_IDS/IPS_detecting_an_intrusion

    #human identification
    goto mangement
    goto control_and_risk_compliance
    goto colleages
    goto external_parties

def containment():
    goto involve_people
    goto meeting
    goto privilege_lowering
    goto authorization_freeze
    goto remote_access
    goto seizure

    #case 1: abnormal activity
    if nothing_malicious_or_fraudulent is confirmed:
        goto forensics_investigation_on_the_computing_devices
        goto log_investigation_on_different_audit_trails_components
    
    #case 2: malicious / fraudulent activity
    if malicious_or_fraudulent_behavior is confirmed:
        goto think_about_file_a_complaint_against_the_suspected_insider
    goto provide_the_legal_team_or_law_enforcement_officier
    if collateral_damages can result from abuse:
        goto contain_the_incident_impacts_before_making_it_public
    
def remediation():
    goto take_disciplinary_action_against_the_malicious_employee
    goto remove_all_his/her_credentials
    goto delete_all_fictitious_or_fraudulent_operations_made_by_insider
    goto review_all_programs_or_scripts

def recovery():
    if incident has not been made public:
        goto warn_all_the_impacted_stakeholders_and_required_authorities
    goto warn_your_employees_or_some_local_teams

def lessons_learnt():
    goto report
    goto capitalize