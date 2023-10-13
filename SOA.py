import Passive
import SIRP

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

def soa_accident_documetation():
    print("this accident was analyzed by playbook and document this accident")


def soa_accident_improvement():
    print("based on this accident, improve security appliance and analyze corresponding playbook for improve")

    SIRP.sirp_generate_playbook()
    SIRP.sirp_add_playbook()


def soa_analyzing_more_AV(case):
    Passive.passive_analyzing()


