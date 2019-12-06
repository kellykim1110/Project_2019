library("igraph")

# Read in the data:
nodes <-read.csv("C:/Users/cloud/Anaconda_src/No_Japan/keys_values_19_07_Node.csv", header=T, as.is=T)
links <- read.csv("C:/Users/cloud/Anaconda_src/No_Japan/Top100_new_noun1_and_noun2_twitter_data_2019-07-01_to_2019-09-09.csv", header=T, as.is=T)
library(dplyr)
nodes<-nodes%>%head(100)
tail(nodes)
# Examine the data:
head(nodes)
tail(links)

# Converting the data to an igraph object:
# The graph_from_data_frame() function takes two data frames: 'd' and 'vertices'.
# 'd' describes the edges of the network - it should start with two columns 
# containing the source and target node IDs for each network tie.
# 'vertices' should start with a column of node IDs.
# Any additional columns in either data frame are interpreted as attributes.

net <- graph_from_data_frame(d=links, vertices=nodes, directed=T) 

# Examine the resulting object:
class(net)
net 

# We can access the nodes, edges, and their attributes:
E(net)
V(net)

# If you need them, you can extract an edge list 
# or a matrix back from the igraph networks.
as_edgelist(net, names=T)
as_adjacency_matrix(net, attr="weight")

# Or data frames describing nodes and edges:
as_data_frame(net, what="edges")
as_data_frame(net, what="vertices")


# You can also look at the network matrix directly:
net[1,]
net[5,7]

# First attempt to plot the graph:
plot(net) # not pretty!

# Removing loops from the graph:
net <- simplify(net, remove.multiple = F, remove.loops = T) 


plot(net,vertex.label=NA)

plot(net, edge.arrow.size=.2, edge.curved=0,
     vertex.color="orange", vertex.frame.color="#555555",
     vertex.label=V(net)$keys, vertex.label.color="black",
     vertex.label.cex=.7) 
# Let's and reduce the arrow size and remove the labels:
plot(net, edge.arrow.size=.4,vertex.label=NA)


# Compute node degrees (#links) and use that to set node size:
deg <- degree(net, mode="all")
V(net)$size <- deg*3
# Alternatively, we can set node size based on audience size:
V(net)$size <- V(net)$audience.size*0.7

# The labels are currently node IDs.
# Setting them to NA will render no labels:
V(net)$label.color <- "black"
V(net)$label <- NA

# Set edge width based on weight:
E(net)$width <- E(net)$weight/6

#change arrow size and edge color:
E(net)$arrow.size <- .2

E(net)$edge.color <- "gray80"

# We can even set the network layout:
graph_attr(net, "layout") <- layout_with_lgl
plot(net) 

# We can also override the attributes explicitly in the plot:
plot(net, edge.color="orange", vertex.color="gray50") 

