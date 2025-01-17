colors=['red','blue','green','yellow','black']
states=['andhra','karnataka','tamilnadu','kerala']
neighbors={}
neighbors['andhra']=['karnataka','tamilnadu']
neighbors['karnataka']=['andhra','tamilnadu','kerala']
neighbors['tamilnadu']=['andhra','tamilnadu','kerala']
neighbors['kerala']=['karnataka','tamilnadu']
colors_of_states={}
def promising(state,color):
    for neighbor in neighbors.get(state):
        color_of_neighbor=colors_of_states.get(neighbor)
        if color_of_neighbor==color:
            return False
    return True
def get_color_for_states(state):
    for color in colors:
        if promising(state,color):
            return color
def main():
    for state in states:
        colors_of_states[state]=get_color_for_states(state)
    print(colors_of_states)
main()
