import bpy


#bpy.data.materials[*Material Name*].node_tree.nodes[*Node Name*].location.x
#bpy.data.materials[*Material Name*].node_tree.nodes[*Node Name*].location.y

def arrange(node_tree: list):
    priorDimen = [0,0]
    starter = -1 * (2240 + 140)
    for nodeInd in range(0,len(node_tree),4):
        if nodeInd == 0:
            node_tree[nodeInd + 0].location.x = starter + priorDimen[0]

        priorDimen[0] = node_tree[nodeInd + 0].width
        priorDimen[1] = int(node_tree[nodeInd + 0].height) + 1
        starter+=priorDimen[0]








    pass