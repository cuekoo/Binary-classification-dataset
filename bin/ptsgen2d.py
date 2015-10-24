import numpy as np

class PtsGen2d:

    def __init__(self, figure, axrange = [0, 10, 0, 10]):

        self.figure = figure
        if len(figure.axes) < 1:
            self.figure.add_subplot(111)
        self.ax = figure.axes[0]
        self.axrange = axrange
        self.ax.cla()
        self.ax.axis(self.axrange)
        
        self.figure.canvas.mpl_connect('button_press_event', self.append_data)
        self.figure.canvas.mpl_connect('key_press_event', self.on_press)

        self.data = np.empty((0,3), float) #[label, x, y]

        # default mode is positive
        self.mkstyle = 'r+'
        self.isPos = True
        self.annoPos = (axrange[0], axrange[3])
        self.mode = self.ax.annotate('positive', xy=self.annoPos, color='r',
                va='top')

        self.train_outfile = '2d_data_train.csv'

    def on_press(self, event):
        if event.key == 'n': self.change_mode()
        elif event.key == 'c': self.clear_data()
        elif event.key == 'd': self.save_data_csv()

    def append_data(self, event):
        contains, attrd = self.ax.contains(event)
        if not contains: return 

        self.ax.plot(event.xdata, event.ydata, self.mkstyle, markeredgewidth=2)
        self.figure.canvas.draw()

        label = 1
        if not self.isPos: label = -1
        self.data = np.append(self.data, np.array([[label, event.xdata,
            event.ydata]]), axis=0)

    def change_mode(self):
        self.ax.texts.remove(self.mode)
        if self.isPos:
            self.mode = self.ax.annotate('negtive', xy=self.annoPos, color='b',
                    va = 'top')
            self.isPos = False
            self.mkstyle = 'b+'
        else:
            self.mode = self.ax.annotate('positive', xy=self.annoPos, color='r',
                    va = 'top')
            self.isPos = True
            self.mkstyle = 'r+'
        self.figure.canvas.draw()

    def clear_data(self):
        self.ax.cla()
        self.ax.axis(self.axrange)
        self.data = np.empty((0, 3), int)
        self.mode = self.ax.annotate('positive', xy=self.annoPos, color='r',
                va = 'top')
        self.datastyle = 'r+'
        self.isPos = True
        self.figure.canvas.draw()

    def save_data_csv(self):
        np.savetxt(self.train_outfile, self.data, fmt='%.4f', delimiter=',')
        print "Data written to " + self.train_outfile 

