class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        key=deque(rooms[0])
        visited=[0]
        while key:
            idx=key.popleft()
            if idx not in visited:
                key.extend(rooms[idx])
                visited.append(idx)
        if len(visited)==len(rooms):
            return True
        return False