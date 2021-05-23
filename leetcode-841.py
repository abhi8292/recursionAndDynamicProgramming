class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        room = [0] * len(rooms)

        def bfs():
            visited = [0]

            while visited:
                src = visited.pop(0)
                if room[src] != 1:
                    visited = visited + rooms[src]

                    room[src] = 1

        bfs()

        print(room)

inp = [[1,3],[3,0,1],[2],[0]]

Solution().canVisitAllRooms(inp)


