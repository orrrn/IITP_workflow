# Cloud Misconfigurations
# In Top Security Playbook from Siemplify 
# Written in Sudocode

def main():
   #enrichment & context
   goto enrich_the_asset
   goto enrich_the_owner
   goto enrich_the_risk

   #inversitgation
   goto decide_whether_to_act_on_different_aspects
    
    #containment & remediation
    goto contain_the_access
    goto recovery
