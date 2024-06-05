
class Loop:   
    slots = ["widget", "interval", "callback", "args", "running"]

    def __init__(self, widget, interval, callback, args=()):
        self.widget = widget
        self.interval = interval
        self.callback = callback
        self.args = args
        self.running = False

    def start(self):
        """Start the loop
        """        
        self.widget.after(self.interval, self.loop)
        self.running = True
    
    def loop(self):
        """Looping
        """        
        if self.running:
            self.callback(*(self.args))
            self.widget.after(self.interval, self.loop)

    def stop(self):
        """Stop the loop
        """        
        self.running = False
