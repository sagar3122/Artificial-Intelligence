#Name: Sagar Sharma
#UTA ID: 1001626958

import sys
from Node import Node

# function for reading the input file
def read_file(input_file):
    data = list() # creating a list to store the contents of the input file
    try:
        fhandle = open(input_file) # creating a handle to access the content of the input file
    except:
        print 'File not found in the same directory.'
    #else:
    for line in fhandle:  # loop for adding the content to the data list
        data.append(line)
    #print data
    fhandle.close() # close the handle for the input file
    return data # return the list 'data' with the contents of the input file

# function for reading the hueristics file
def read_hueristics(h_file):
    data2 = list() # creating a list to store the contents of the hueristics file
    try:
        fhandle = open(h_file) # creating a handle to access the content of the hueristics file
    except:
        print 'File not found in the same directory.'
    for line in fhandle: # loop for adding the content to the data2 list
        data2.append(line)
    fhandle.close() #close the handle of the hueristics file
    return data2 # return the lsit 'data2' with the contents of the hueristics file

# function to expand node for ucs
def expand_node(fringe, paths, visited_node):
    node_city = fringe[0] #assign the first node in the fringe as the node_city we are going to expand
    city_name = node_city.city_name # pull the city name from the node
    present_cost = node_city.cumm_cost # pull the current cost of the node

    visited_node.append(city_name) # add to the visisted cities list

    del fringe[0] #delete the first node, we are going to expand
    for path in paths:
        if city_name in path:
            ## when node in fringe is the first city in the path
            if path[0] == city_name and not(path[1] in visited_node): #when the adjacent city is not in visited list then add adjacent city to fringe as a node
                adj_city = Node(path[1], node_city, None, int(present_cost)+int(path[2]), int(path[2])) #assign the values for the node
                fringe.append(adj_city)
            ## when node in fringe is the second city in the path
            elif path[1] == city_name and not(path[0] in visited_node): #when the adjacent city is not in visited list then add adjacent city to fringe as a node
                adj_city = Node(path[0], node_city, None, int(present_cost)+int(path[2]), int(path[2])) # assign the values for the node
                fringe.append(adj_city)

# function to expand node for A*
def a_expand_node(fringe, paths, hueristics, visited_node):
    node_city = fringe[0] #assign the first node in the fringe as the node_city we are going to expand
    city_name = node_city.city_name # pull the city name from the node
    present_cost = node_city.cumm_cost # pull the current cost of the node

    visited_node.append(city_name) # add to the visisted cities list

    del fringe[0] #delete the first node, we are going to expand
    for path in paths:
        if city_name in path:
            ## when node in fringe is the first city in the path
            if path[0] == city_name and not(path[1] in visited_node):  #when the adjacent city is not in visited list then add adjacent city to fringe as a note
                for hvalue in hueristics: # add the fvalue to the node by adding associated hueristic value it to the cummulative path cost
                    if city_name in hvalue:
                        if hvalue[0] == city_name:
                            # assign the values for the node
                            adj_city = Node(path[1], node_city, int(present_cost)+int(path[2])+int(hvalue[1]), int(present_cost)+int(path[2]), int(path[2]))
                            fringe.append(adj_city)
            ## when node in fringe is the second city in the path
            elif path[1] == city_name and not(path[0] in visited_node):
                for hvalue in hueristics: # add the fvalue to the node by adding associated hueristic value it to the cummulative path cost
                    if city_name in hvalue:
                        # assign the values for the node
                        if hvalue[0] == city_name:
                            adj_city = Node(path[0], node_city, int(present_cost)+int(path[2])+int(hvalue[1]), int(present_cost)+int(path[2]), int(path[2]))
                            fringe.append(adj_city)

# function to manage the fringe for ucs graph search
def create_fringe(paths, source, dest_city):
    fringe = list()
    visited_node = list()

    fringe.append(source) # add the start node to the fringe
    #print fringe
    # implement graph search
    #visited_node.append(source.city_name) #add the visited city names associated with nodes in a list

    while True: #indefinite loop

        if not fringe: #if fringe is empty return none
            return None

        if fringe[0].city_name == dest_city: #if first element in fringe is the destination city then return it
            return fringe[0]

        expand_node(fringe, paths, visited_node) #call this function to expand the first node in fringe

        fringe = sorted(fringe, key=lambda node: node.cumm_cost) #sort the fringe on the basis of increasing cummulative path cost of thee nodes

# function to manage the fringe for A* graph search
def a_create_fringe(paths, hueristics, source, dest_city):
    fringe = list()
    visited_node = list()

    fringe.append(source) # add the start node to the fringe
    #print fringe
    # implement graph search
    #visited_node.append(source.city_name)  #add the visited city names associated with nodes in a list

    while True: #indefinite loop

        if not fringe: #if fringe is empty return none
            return None

        if fringe[0].city_name == dest_city: #if first element in fringe is the destination city then return it
            return fringe[0]

        a_expand_node(fringe, paths, hueristics, visited_node) #call this function to expand the first node in fringe

        fringe = sorted(fringe, key=lambda node: node.fvalue) #sort the fringe on the basis of increasing fvalue of the nodes


def track_path(des_node):
    # cost to the goal city is the cummulatice cost to that city calculated either by ucs or A* search
    print 'Distance: %d Km' % des_node.cumm_cost

    # for tracing the cities on the path to the goal city from start city
    trace_city = list()
    # for tracing the step cost between the cities on the path to the goal city from start city
    trace_cost = list()
    while des_node: #loops exists when None
        trace_city.append(des_node.city_name)
        trace_cost.append(des_node.step_cost)
        des_node = des_node.parent_node
    # to track from the start city use reverse
    trace_city.reverse()
    trace_cost.reverse()

    del trace_cost[0] ## delete the step cost for start node as it is 0

    print 'Route:'
    # print the whole route with step routes and step costs
    for i in range(0, len(trace_city)-1):
        print '%s to %s, %d Km' % (trace_city[i], trace_city[i+1], trace_cost[i])

# function for uniform cost search
def ucs(paths, source, des):
    result = create_fringe(paths, source, des) #get either the goal state city or either the empty fringe
    if result is None:
        print 'Distance = Infinity'
        print 'route:'
        print 'None'
    else:
        track_path(result) #track the path from the start city to the goal city with the step route and cost

#function for A* search
def a_search(paths, hueristics, source, des):
    result = a_create_fringe(paths, hueristics, source, des) #get either the goal state city or either the empty fringe
    if result is None:
        print 'Distance = Infinity'
        print 'route:'
        print 'None'
    else:
        track_path(result) #track the path from the start city to the goal city with the step route and cost


def main():
    #when the cmd line arguments are less then 5 or more than 6 print the following
    if len(sys.argv) < 5 or len(sys.argv) > 6:
        print 'Use Either of the formats:'
        print '[Format 1] python find_route.py uninf <input_file> <source> <des>'
        print '[Format 2] python find_route.py inf <input_file> <source> <des> <h_file>'

#assign values to the variables acc to command line arguments
    if len(sys.argv) == 5:
        input_file = sys.argv[2]
        source = sys.argv[3].lower()
        des = sys.argv[4].lower()

#assign values to the variables acc to command line arguments
    elif len(sys.argv) == 6:
        input_file = sys.argv[2]
        source = sys.argv[3].lower()
        des = sys.argv[4].lower()
        h_file = sys.argv[5].lower()

# put route data in the list for future operations
    data = read_file(input_file)
    paths = list()
    for path in data:
        paths.append(path.lower().split())
    #print paths
    del paths[len(paths)-1] # to delete the last line of the input file i.e end of file
    #print paths

# when the cmd srguments are 5 and flag used is uninf ; perform uniform cost search
    if len(sys.argv) == 5 and sys.argv[1].lower() == 'uninf':
        start = Node(source, None, None, 0, 0)
        try:
            ucs(paths, start, des)
        except:
            print 'Use Either of the formats:'
            print '[Format 1] python find_route.py uninf <input_file> <source> <des>'
            print '[Format 2] python find_route.py inf <input_file> <source> <des> <h_file>'

# when the cmd srguments are 5 and flag used is not uninf ,print the warning
    if len(sys.argv) == 5 and sys.argv[1].lower() != 'uninf':
        print 'Use Either of the formats:'
        print '[Format 1] python find_route.py uninf <input_file> <source> <des>'
        print '[Format 2] python find_route.py inf <input_file> <source> <des> <h_file>'

# when the cmd srguments are 6 and flag used is inf, perform A* search
    if len(sys.argv) == 6 and sys.argv[1].lower() == 'inf':
        # put the hueristics values in a list with associated cities for future operations
        data2 = read_hueristics(h_file)
        hueristics = list()
        for hvalue in data2:
            hueristics.append(hvalue.lower().split())

        del hueristics[len(hueristics)-1]# to delete the last line of the h_file i.e end of file
        #print hueristics

        # for assigning the hueristic value to the start node
        for hvalue in hueristics:
            if source in hvalue:
                if hvalue[0] == source:
                    start = Node(source, None, int(hvalue[1]), 0, 0)
        #print start
        try:
            a_search(paths, hueristics, start, des)
        except:
            print 'Check the spellings of the cities'
            print 'OR'
            print 'Use Either of the formats:'
            print '[Format 1] python find_route.py uninf <input_file> <source> <des>'
            print '[Format 2] python find_route.py inf <input_file> <source> <des> <h_file>'

# when the cmd srguments are 6 and flag used is not inf, print the warning
    if len(sys.argv) == 6 and sys.argv[1].lower() != 'inf':
        print 'Use Either of the formats:'
        print '[Format 1] python find_route.py uninf <input_file> <source> <des>'
        print '[Format 2] python find_route.py inf <input_file> <source> <des> <h_file>'

if __name__ == "__main__":
    main()
