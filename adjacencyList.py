# Defining our vertex class
class Vertex:

    # Constructor for the Vertex class
    def __init__(self, nameParam):

        # The name of the current vertex
        self.name = nameParam
        
        # The list of neighbors of the current vertex
        self.neighbors = list()
        
        # The "time" that the current vertex was first encountered
        self.timeOfDiscovery = 0
        
        # The "time" when the current vertex finishes its recursion
        self.timeOfExploration = 0
        
        # Vertices are initialized to be colored black
        self.color = 'black'

    # Function to add a specified vertex to be the neighborhood list of the calling vertex
    def add_neighbor(self, vertexParam):

        # Converts the list of neighbors to a set
        setOfNeighbors = set(self.neighbors)

        # Checks if the specified vertex is not in the neighborhood list
        if vertexParam not in setOfNeighbors:

            # Adds the vertex to the neighbor list
            self.neighbors.append(vertexParam)

            # Re-sorts the neighborhood list
            self.neighbors.sort()

# Defining our adjacency list class to represent a graph
class AdjacencyList:

    # Dictionary of vertices (string/object pairs) (name/vertex pairs)
    vertices = {}

    # List of edges in our graph
    listOfEdges = []
        
    # Function to add a vertex to the graph
    def add_vertex(self, vertexParam):

        # Checks:
        # if the given parameter is an instance of the vertex class &
        # if the vertex is not already in the vertex list
        if isinstance(vertexParam, Vertex) and vertexParam.name not in self.vertices:

            # Adds the name/vertex pair to associative map ("Dictionary")
            self.vertices[vertexParam.name] = vertexParam

            # Indicates that the vertex was successfully added to the graph
            return True

        # If either of the conditions failed
        else:

            # Returns false to indicate that the vertex can't be added to the graph
            return False

    # Function to add an edge between two(2) vertices of the graph
    def add_edge(self, u, v):

        # Checks if vertices 'u' and 'v' exist in the vertex list
        if u in self.vertices and v in self.vertices:
        
            # Uses tuples and a for each loop to iterate through each key/value pair of the vertex dictionary
            # "key" refers to vertex names
            # "value" is a reference to the vertex properties
            for key, value in self.vertices.items():

                # If the current vertex is 'u'
                if key == u:
                
                    # Adds 'v' to the neighborhood list
                    value.add_neighbor(v)
        
                # If the current vertex is 'v'
                if key == v:

                    # Adds 'u' to the neighborhood list
                    value.add_neighbor(u)

            # Returns true to indicate that an edge was successfully added
            return True

        # If either of the vertices are not already in the list
        else:

            # Returns false to indicate that the edge was not added
            return False

    # Function to display the adjacency list
    def printAdjacencyList(self):

        # Shows the start of the adjacency list
        print("\nAdjacency list:")
        print("Format:")
        print("vertexID: neighborhood_list  time_of_discovery/time_of_exploration")

        # Iterates through each vertex ID in the vertex list
        for key in self.vertices.keys():

            # Prints the current vertex's ID
            print(key + ": ", end = '')
            
            # Iterates through each vertex ID in the neighborhood of the current vertex
            for vertexID in self.vertices[key].neighbors:
                
                # Prints the current neighbors ID
                print(self.vertices[vertexID].name, end = ' ')

            # Displays the "time of discovery" as well as the "time of exploration"
            print(" " + str(self.vertices[key].timeOfDiscovery) + "/" + str(self.vertices[key].timeOfExploration))

    # Wrapper function for the depth first search(DFS)
    # Used to account for separate graph components
    def runDFS(self, vertexParam):

        # Sets the variable that keeps track of time to be global
        global currTime

        # Initializes the current time to be 1
        currTime = 1
        
        # Calls the recursive helper function
        self.helpDFS(vertexParam)

    # Recursive helper function to implement the DFS
    def helpDFS(self, vertexParam):

        # Sets the variable that keeps track of time to be global
        global currTime

        # Discovers the current vertex and sets its color to be blue
        vertexParam.color = "blue"

        # Stores the time that the current vertex was discovered
        vertexParam.timeOfDiscovery = currTime

        # Increments the time variable
        currTime += 1

        # Evaluates each vertex in the neighborhood list of the current vertex
        for v in vertexParam.neighbors:

            # Checks if the current neighbor is still black
            # This indicates that the vertex is undiscovered
            if self.vertices[v].color == "black":

                # Calls the recursive function on the undiscovered vertex
                self.helpDFS(self.vertices[v])

        # Explores/Finalizes the current vertex and sets its color to red
        vertexParam.color = "red"

        # Stores the time that the current vertex was explored
        vertexParam.timeOfExploration = currTime

        # Increments the time variable
        currTime += 1 

# Instantiates our graph
# Implemented as an adjacency list
g = AdjacencyList()

# Defines a vertex, 'A', used to start the DFS
a = Vertex('A')

# Adds vertex A to the graph
g.add_vertex(a)

# For each loop to iterate from A to J
# ord() is used to convert from char to int
for i in range(ord('A'), ord('K')):

    # Creates a vertex
    # It's name is a letter
    # chr() is used to convert from int to char
    v = Vertex(chr(i))
    
    # Adds the vertex to the graph
    g.add_vertex(v)

# Defines the list of edges in our graph
g.listOfEdges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

# Iterates through each edge in the list of edges of the graph
for edge in g.listOfEdges:

    # Adds the edge to the graph
    # Uses "string slices" to access substrings
    # myStr[0:1] refers to the first letter
    g.add_edge(edge[0:1], edge[1:2])

# Runs a DFS starting from vertex 'A'
g.runDFS(a)

# Outputs the adjacency list
g.printAdjacencyList()