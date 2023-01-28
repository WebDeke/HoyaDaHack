def main():
    st.set_page_config(page_title="Study Buddy Finder", page_icon=":guardsman:", layout="wide")
    st.title("Study Buddy Finder")

    classes = st.multiselect(
    'What classes are you taking',
    ['COSC 225 - Computer Networks', 'MATH 150 , Linear Algebra', 'CHEM 228 - Synthetic Methods', 'PHYS 101 - Physics', 'HIST 007- Introduction to Early History', 'CULP 346 - Crit Geography: Theory and Practice', 'CLSS 141 - Roman History', 'CLSL 002 - Latin II'],
    )
    space = st.select_slider(
    'Select your favorite space',
    options=['Place A', 'Place B', 'Place C', 'Place D', 'Place E']
    )
    st.write('I am taking', classes, 'and my favorite study space is', space)
    source = classes 
    index_tracker = 0
    i = 0 
    tracker = 1
    #The logic: create an empty dictionary to store potential match and viability (number of courses in common)
    #Iterate through the 2D array (the code here is for 1D array because I wanted to tackle courses first) and compare it to the values within the dictionary 
    #Create function for this
    length_tracker = 0
    empty_dict = {}
        #for class in source:
            #for x in thisdict.values():
                #while index_tracker < len(x):
                    #if x[index_tracker] == class: 
                        #empty_dict[key????] = tracker
                        #tracker +=1
                    #index_tracker+= 1