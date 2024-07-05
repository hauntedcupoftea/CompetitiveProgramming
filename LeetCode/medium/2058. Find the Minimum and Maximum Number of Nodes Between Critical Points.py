# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        root = head.next
        idx, distMin, lastIdx = 1, 2**31, -1
        points = []
        while root.next:
            isMax = (root.val > prev.val) and (root.val > root.next.val)
            isMin = (root.val < prev.val) and (root.val < root.next.val)
            if (isMax or isMin):
                points.append(idx)
                if lastIdx != -1:
                    distMin = min(distMin, idx-lastIdx)
                lastIdx = idx
            idx += 1
            prev = root
            root = root.next
        if len(points) <= 1:
            return [-1, -1]
        return [distMin, points[-1]-points[0]]