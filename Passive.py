import SIRP
import TIP

#case
# 0번째 IT/OT 스트링
# 1번째 공격벡터-하위내용
# 2번째 공격여부(1이 공격, 0이 일반)
# 3번째 공격분류여부(1이 공격분류 가능, 0이 공격분류 불가능)
# 4번째 playbook 존재 여부(1이 존재, 0이 존재하지 않음)
# 5번째 Risk 숫자 1부터 5
# 6번째 Risk major or minor 여부(1이 major-플레이북 실행 전 추가분석 수행, 0이 minor-playbook 바로 실행)
# 7번째 기존 플레이북 개선 여부(1가능, 0불가능)
# 8번째 공격 대응 성공 여부(1가능, 0실패)
# 9번째 개선사항 유무(1필요, 0불필요)

def passive_alert(case):
    print("this accident has to be analyzed passively")
    return case



def passive_analyzing(case):
    print("this accident analyzed passively")
    return case



def passive_response_and_documentation(case):
    TIP.tip_attack_data()
    return case


def passive_generate_playbook(case):
    print("generate playbook based on passive")
    # SIRP.sirp_generate_playbook()
    return case