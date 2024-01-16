# Use the depth-first approach to traverse the Tree and find the desired node. Like the browser's getElementById method, your method should take a string as an argument and return the node with that value. If a matching node is not found, your method should return None.

# Initialize a root and set it to none
# Initialize an list of nodes to visit and add the root node to it
# While there are nodes in the list of nodes to visit
# Remove the first node from the list of nodes to visit
# Check this node against the condition (if the node key == id). Return the node if meets the condition.
# Still in the loop, add its children (if any) to the BEGINNING of the list of nodes to visit
# Return None in the end of the loop.

class Tree:
  def __init__(self, root = None):
    self.root = root
    
  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]
    
    while nodes_to_visit:
      node = nodes_to_visit.pop(0)  
      if node['id'] == id:
        return node
      nodes_to_visit = node['children'] + nodes_to_visit 
    return None
      

      



