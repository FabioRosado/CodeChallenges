'''
Description:
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

'''

def sortByHeight(a):
    ''' Sorts the height of every person, keeping the 
    location of the trees in a separate list.
    Finally, add the location of the tree to the sorted
    list and returns it. '''
    sorted_height = []
    tree_position = []
    for i in range(len(a)):
        if a[i] == -1:
            tree_position.append(i)
        else:
            sorted_height.append(a[i])
            
    sorted_height.sort()        
    for tree in tree_position:
        sorted_height.insert(tree, -1)
    
    return sorted_height
