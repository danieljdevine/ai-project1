1. Daniel Devine, 10838063

2. I implemented this program using python 3.8.10. The only external libraries used were matplotlib
and networkx for graph visualization during testing.

3. This program was developed on Ubuntu 20.04.6 LTS 64 bit.

4. The code contains 2 modules: input_processing and find_route. 

Input Processing:
The input processing module handles converting a file in the format specified in the assignment into
a graph. A graph consists of a list of edges with one node name mapped to another and a dictionary of
vertex names to vertex classes. A vertex class contains a name and a list of tuples of the form
(Vertex, edge_weight) to show the vertex's neighbors. The workflow starts with inputting a file name,
and building a list of lines. Each line is separated by spaces to get the start, end and weight of the
edge. This is how the list of edges is created. Vertices are added by only adding unique vertex names.
After the two lists are created, the edge list is iterated through to add neighbors to each vertex.
This is critical for the algorithm to work.

Find Route
This is where the UCID (Uniform Cost Iterative Deepening) search algorithm is implemented. We build a
tree structure with nodes mapped to their parents as we iterate through the graph. The data structure
used for the fringe was a custom priority queue, which is sorted by current cost of the overall path
to the node.
The algorithm is as follows (and is implemented this way in code):
    if start node == end node
        print 0 cost solution
    for i from 0 to maximum depth (amount of nodes in the graph)
        run depth limited search with max_depth=i
        if solution found, break and print solution
    if reaching the end of the loop, there is no path from start to end. print infinity

The depth limited search is run in a different function, and operates as follows:
    add start node to the fringe
    while fringe is not empty
        pop lowest cost node from fringe
        if goal reached, return solution path, calculated from climbing the tree in reverse
        if depth of node > max_depth, continue with loop
        find all neighbors, add cost of neighbor to current node's cost, add 1 to depth and add to fringe
    if end of loop reached, return null to notify no solution found

5. Execution of the program is very simple. Ensure python3 is installed on your local machine, and then run:
python3 find_route.py [input_file_path] [start] [end]
The program will print output to the standard out stream as specified in the assignment.

NOTE: When running with a start and end that are disconnected, the program will take a while. Please
wait for it to finish before evaluating. For a maximum depth of 21, it took me about 10 minutes to run.
