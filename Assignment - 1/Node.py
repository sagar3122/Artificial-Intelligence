#Name: Sagar Sharma
#UTA ID: 1001626958

class Node:
    def __init__(self, city_name, parent_node, fvalue, cumm_cost, step_cost):
        self.city_name = city_name; # name of the city associated with node
        self.parent_node = parent_node; # name of the parent node
        self.fvalue = fvalue; # f(n) = g(n) + h(n) ; where g is the cummulative path cost and h is hueristic value
        self.cumm_cost = cumm_cost; #cummulative path cost
        self.step_cost = step_cost; #step cost for the node from the parent node
