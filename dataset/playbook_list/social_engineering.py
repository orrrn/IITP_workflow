# Social Engineering - the use of deception to manipulate individuals into divulging  confidential or personal information that may be used for fraudulent  purposes
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
    goto raise_user_awareness_and_security_policies
    goto report_any_suspicious_event_to_your_manager
    goto have_a_defined_process_to_redirect_any_“weird”_request_to_a_“red”_phone
    goto prepare_to_handle_conversation_with_social_engineers_to_identify_which_information_could_help_tracking_the_attacker_and_his_goals
    goto check_your_legal_department_to_see_which_actions_are_allowed_and_which_reactions_they_can_handle

def identification():
    goto phone_call
    goto email

def containment():
    #actions for all employees
    if attacker urges you to give_a_phone_number:
        goto use_the_"red_phone_line"_from_your_CERT/CSIRT
        goto give_the_number_with_an_invented_name
        goto call_your_CERT/CSIRT_team_explaining
    if attacker stresss you:
        goto ask_him_to_call_you_back_later
    if attacker want to_reach_someone:
        goto place_on_hold_the_attacker
        goto call_CERT/CSIRT
        goto explain_what_happened
        goto transfer_the_conversation_of_the_attacker_to_CERT/CSIRT
    
    #actions for CERT or incident reponse team
    goto resume_the_coversation_with_the_attacker
    if the_trap_phone_number has been used:
        goto prepare_to_"burn_it"
        goto create_another_one
        goto display_in_the_directoroy
    
def remediation():
    goto alert_the_law_enforcement
    goto discuss_the_problem_in_circles_of_trust_to_know
    goto threathen_the_attacker_with_legal_actions

def recovery():
    goto notify_the_top_management_of_the_actions_and_decisions

def lessons_learnt():
    goto report
    goto capitalize