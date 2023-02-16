import tkinter as tk
import statistics
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

class BoxPlotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Box Plot ")

      
        self.data_label = tk.Label(master, text="Enter data separated by commas:")
        self.data_label.pack()
        self.data_entry = tk.Entry(master)
        self.data_entry.pack()

        # generate button
        self.plot_button = tk.Button(master, text="Generate Box Plot", command=self.generate_box_plot)
        self.plot_button.pack()

    
        self.fig = plt.figure(figsize=(5, 4), dpi=100)

        # create a canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().pack()

    def generate_box_plot(self):
        # convert list of floats
        data_str = self.data_entry.get()
        try:
            data_list = [float(x.strip()) for x in data_str.split(",")]
        except ValueError as e:
            # display an error message if the input is not valid
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
            return

        # calculate the quartiles and IQR
        try:
            q1 = statistics.median(sorted(data_list)[:len(data_list)//2])
            q3 = statistics.median(sorted(data_list)[-(len(data_list)//2):])
            iqr = q3 - q1
        except statistics.StatisticsError as e:
            # display an error message the input is not valid
            messagebox.showerror("Error", f"Insufficient data: {str(e)}")
            return

        # upper and lower bounds
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        # filter the data
        filtered_data = [x for x in data_list if lower_bound <= x <= upper_bound]

        # box plot
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.boxplot(filtered_data)

        # update
        self.canvas.draw()

root = tk.Tk()
app = BoxPlotApp(root)
root.mainloop()

