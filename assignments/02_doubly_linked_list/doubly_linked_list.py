#         ←────────→       ←────────→
# ┌──────┐        ┌──────┐        ┌──────┐
# │  10  │        │  20  │        │  30  │
# └──────┘        └──────┘        └──────┘
# 양방향으로 이동할 수 있는 연결 리스트 -> 이중 연결리스트

#      DListNode
# ┌─────────────────┐
# │      data       │
# │                 │
# │ llink     rlink │
# └───┬─────────┬───┘
#     │         │
#     ↓         ↓
#  이전 노드   다음 노드

# Data -> 이 노드가 저장하는 값
# llink -> 왼쪽(previous) 노드에 대한 참조
# rlink -> 오른쪽(next) 노드에 대한 참조

# DListNode 하나는 이중 연결 리스트의 노드 하나를 나타냄
# self는 현재 생성되거나 다루고 있는 DListNode 객체를 나타냄
# 각 노드는 data, llink, rlink 속성을 가짐


class DListNode:
    def __init__(self, data=None):
        self.data = data
        self.llink = None  # 처음에는 이전 노드가 없으므로 None
        self.rlink = None


# 작동하는지 테스트
# node = DListNode(10)

# print(node.data)
# print(node.llink)
# print(node.rlink)


class DoublyLinkedList:
    def __init__(self):
        self.head = DListNode()
        self.head.llink = self.head  # head의 왼쪽 링크가 자기 자신을 가리키게 함
        self.head.rlink = self.head  # head의 오른쪽 링크가 자기 자신을 가리키게 함


# DListNode()를 하나 생성해서 head로 사용
# 하지만 데이터가 없으므로 기본값 Data=None이 들어감

# <예시>
#  head
#   ↓
#  ┌───────────────┐
#  │ data = None   │
#  │ llink = None  │
#  │ rlink = None  │
#  └───────────────┘

# <헤드 노드>
# head는 실제 데이터 예)10, 20, 30 등을 저장하기 위한 노드가 아님
# 삽입, 삭제 코드를 간단하게 할 목적으로 만들어진 노드
# 헤드포인터와는 구별 필요
# 공백상태에서는 헤드 노드만 존재

# 리스트가 비어 있으면
# head.llink → head
# head.rlink → head

# 자기 자신을 가리키는 이유는 Page 23 ~ 24 코드는 원형 이중 연결 리스트 구조이기 때문

#    ┌──────────────────────────┐
#    ↓                          │
#  head ⇄ [10] ⇄ [20] ⇄ [30] ──┘
#    ↑                          │
#    └──────────────────────────┘
# 헤드를 기준으로 한 바퀴 돌아옴
