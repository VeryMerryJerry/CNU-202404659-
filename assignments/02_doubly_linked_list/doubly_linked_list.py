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
        self.head.llink = self.head
        self.head.rlink = self.head
