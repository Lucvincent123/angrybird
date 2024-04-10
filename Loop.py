# from threading import Thread

# class Loop(Thread):
#     def __init__(self, widget, interval, callback, args=()):
#         self.widget = widget
#         self.interval = interval
#         self.callback = callback
#         self.args = args
#         super().__init__(target=self.loop)
#         self.start()

#     def loop(self):
#         self.callback(*(self.args))
#         self.widget.after(self.interval, self.loop)

class Loop:
    def __init__(self, widget, interval, callback, args=()):
        self.widget = widget
        self.interval = interval
        self.callback = callback
        self.args = args
        self.callback()
        self.widget.after(self.interval, self.loop)

    def loop(self):
        self.callback(*(self.args))
        self.widget.after(self.interval, self.loop)
