# Manuel Ortiz at 2022
# Extracted from: https://leetcode.com/problems/keys-and-rooms/description/


from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        total_rooms = len(rooms)
        queue, keys = deque(), set()
        queue.append(0)
        keys.add(0)
        while queue:
            next_room_key = queue.popleft()
            for key in rooms[next_room_key]:
                if key not in keys:
                    queue.append(key)
                    keys.add(key)
        
        return True if total_rooms == len(keys) else False