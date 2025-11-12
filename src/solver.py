class TopTradingCycleSolver:
    """A solver for the Top Trading Cycle algorithm."""

    def __init__(
            self,
            preferences: list[list[int]],
    ):
        self.preferences = preferences
        self.num_agents = len(preferences)
        self.results = [-1] * self.num_agents
    
    def solve(self) -> list[int]:
        """Executes the Top Trading Cycle algorithm and returns the final allocations."""
        active_agents = list(range(self.num_agents))
        
        while active_agents:
            graph = self._build_graph(active_agents)
            cycle = self._find_cycle(graph)
            
            for agent in cycle:
                top_choice = graph[agent]
                self.results[agent] = top_choice
            
            active_agents = [agent for agent in active_agents if agent not in cycle]
        
        return self.results
    
    def _build_graph(self, active_agents: list[int]) -> dict[int, int]:
        """Builds the directed graph of top choices for active agents."""
        graph = {}
        for agent in active_agents:
            top_choice = self.preferences[agent][0]
            while top_choice not in active_agents:
                self.preferences[agent].pop(0)
                top_choice = self.preferences[agent][0]
            graph[agent] = top_choice
        return graph
    
    def _find_cycle(self, graph: dict[int, int]) -> list[int]:
        """Finds a cycle in the directed graph."""
        visited = set()
        for start in graph:
            if start in visited:
                continue
            current = start
            path = []
            while current not in visited:
                visited.add(current)
                path.append(current)
                current = graph[current]
                if current in path:
                    cycle_start_index = path.index(current)
                    return path[cycle_start_index:]