from src.solver import TopTradingCycleSolver

def main():
    num_agents = input("Enter number of agents: ")
    preferences = []
    for i in range(1, int(num_agents)+1):
        while True:
            prefs = input(f"Enter preferences for agent {i} (space-separated indices): ")
            prefs_list = [int(x) - 1 for x in prefs.split()]
            if len(prefs_list) != int(num_agents):
                print(f"Error: Agent {i} must have exactly {num_agents} preferences.")
            elif set(prefs_list) != set(range(int(num_agents))):
                print(f"Error: Preferences for agent {i} must include all items exactly once.")
            else:
                break

        preferences.append(prefs_list)
    
    solver = TopTradingCycleSolver(preferences)
    results = solver.solve()
    print("Final allocations:")
    for agent, allocation in enumerate(results):
        print(f"Agent {agent + 1} gets item {allocation + 1}")


if __name__ == "__main__":
    main()