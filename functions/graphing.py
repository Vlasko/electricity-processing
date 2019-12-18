import matplotlib.pyplot as plt

def simple_graphing(dataframe):
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 15
    fig_size[1] = 8
    fig = plt.figure()
    fig, ax1 = plt.subplots()
    ax1.plot(dataframe.index, dataframe.iloc[:,0], 'b')
    ax1.set_ylabel(dataframe.columns[0])
    ax1.set_xlabel('Datetime')
    plt.show()

def total_graphing(dictionary):

    for key, item in dictionary.items():
        if key == 'price demand':
            y_max = round((max(item.loc[:,'Electricity Price(p/kWh)'])/5)*5)
            h_line = 0
            line_colour = 'r'
        elif key == 'temperature demand':
            y_max = round((max(item.loc[:,'Temperature (*C)'])/5)*5)
            h_line = 11.5
            line_colour = 'g'
        fig_size = plt.rcParams["figure.figsize"]
        fig_size[0] = 15
        fig_size[1] = 8
        fig = plt.figure()
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.plot(item.index, item.iloc[:,0], 'b')
        ax2.plot(item.index, item.iloc[:,1], line_colour)
        rounded_max = round((max(item.loc[:,'Demand (W)'])/5)*5)
        ax1.set_ylim(0,rounded_max) #add functionality to take max/min of real data
        ax2.set_ylim(0,y_max) #add functionality to take max/min of real data
        ax2.hlines(h_line,item.index[0], item.index[-1] )
        ax1.set_ylabel(item.columns[0])
        ax2.set_ylabel(item.columns[1])
        # ask matplotlib for the plotted objects and their labels
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='best')
        ax1.set_xlabel('Datetime')
        plt.show()

def cropped_graphing(dictionary, start_date, end_date):

    for key, item in dictionary.items():
        crop = item.loc[start_date:end_date]

        if key == 'price demand':
            y_max = round((max(item.loc[:,'Electricity Price(p/kWh)'])/5)*5) + 1
            h_line = 0
            line_colour = 'r'
        elif key == 'temperature demand':
            y_max = 20 # round((max(item.loc[:,'Temperature (*C)'])/5)*5) + 1
            h_line = 11.5
            line_colour = 'g'
        fig_size = plt.rcParams["figure.figsize"]
        fig_size[0] = 15
        fig_size[1] = 8
        fig = plt.figure()
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.plot(crop.index, crop.iloc[:,0], 'b')
        ax2.plot(crop.index, crop.iloc[:,1], line_colour)
        rounded_max = round((max(crop.loc[:,'Demand (W)'])/5)*5) + 1
        ax1.set_ylim(0,rounded_max) #add functionality to take max/min of real data
        ax2.set_ylim(0,y_max) #add functionality to take max/min of real data
        ax2.hlines(h_line,crop.index[0], crop.index[-1] )
        ax1.set_ylabel(crop.columns[0])
        ax2.set_ylabel(crop.columns[1])
        # ask matplotlib for the plotted objects and their labels
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='best')
        ax1.set_xlabel('Datetime')
        plt.show()
