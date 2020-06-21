import matplotlib.pyplot as pyp
import matplotlib.animation as animation

#Creating a new figure
figure = pyp.figure()

#Creating a subplot with 1 row, 1 column and index 1 - this means a single subplot in our figure
subplot = figure.add_subplot(1, 1, 1)

#Creating the function that reads the data from cpu.txt and feeds it to our subplot
def animation_function(i):
    #Opening the file and reading each row of CPU utilization data in the file; creating a list of values
    cpu_data = open("D:\\App3\\cpu.txt").readlines()
    
    #Creating an empty list in which to append each value in the file converted from string to float;
    x = []
    
    #Iterating over the list of CPU values and appending each value (converted to float) to the previously created list - x; adding an if statement to exclude any blank lines in the file
    for each_value in cpu_data:
        if len(each_value) > 1:
            x.append(float(each_value))
    
    #Clearing/refreshing the figure to avoid unnecessary overwriting for each new poll (every 10 seconds)
    subplot.clear()
    
    #Plotting the values in the list
    subplot.plot(x)

#Using the figure, the function and a polling interval of 10000 ms (10 seconds) to build the graph    
graph_animation = animation.FuncAnimation(figure, animation_function, interval = 10000)

#Displaying the graph to the screen
pyp.show()