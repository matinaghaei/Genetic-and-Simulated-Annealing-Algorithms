from node import Node
from state import State
from search import Search

if __name__ == '__main__':
    number_of_nodes = int(input("number of nodes: "))
    number_of_neighbours = int(input("number of neighbours: "))
    print("enter neighbours:")
    neighbours = []
    for i in range(number_of_neighbours):
        arr = input()
        neighbours.append(list(map(int, arr.split())))
    scheduling_method = int(input("scheduling method: "))
    alpha = float(input("alpha: "))
    initial_time = int(input("initial time: "))

    State.set_number_of_nodes(number_of_nodes)
    State.set_neighbours(neighbours)
    Node.set_number_of_colors(3)
    local_search = Search(scheduling_method, alpha, initial_time)
    local_search.search()
