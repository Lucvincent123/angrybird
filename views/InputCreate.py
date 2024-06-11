import tkinter as tk

class InputCreate(tk.Toplevel):
    slots = ["status", "planet"]

    def __init__(self, app):
        super().__init__(app)
        self.planet = None
        # Input frame
        self.input_frame = tk.Frame(self)
        self.input_frame.pack()
        ## Name label + input
        self.name_label = tk.Label(self.input_frame, text="name")
        self.name = tk.StringVar(self)
        self.name_input = tk.Entry(self.input_frame, textvariable=self.name, width=50, borderwidth=3)
        self.name_label.grid(row=0, column=0, sticky="w", padx=(20, 10), pady=5)
        self.name_input.grid(row=0, column=1, padx=(10, 20), pady=5)
        ## Mass label + input
        self.mass_label = tk.Label(self.input_frame, text="mass(kg)")
        self.mass = tk.StringVar(self)
        self.mass_input = tk.Entry(self.input_frame, textvariable=self.mass, width=50)
        self.mass_label.grid(row=1, column=0, sticky="w", padx=(20, 10), pady=5)
        self.mass_input.grid(row=1, column=1, padx=(10, 20), pady=5)
        ## Radius label + input
        self.radius_label = tk.Label(self.input_frame, text="radius(m)")
        self.radius = tk.StringVar(self)
        self.radius_input = tk.Entry(self.input_frame, textvariable=self.radius, width=50)
        self.radius_label.grid(row=2, column=0, sticky="w", padx=(20, 10), pady=5)
        self.radius_input.grid(row=2, column=1, padx=(10, 20), pady=5)
        ## Color label + input
        self.color_label = tk.Label(self.input_frame, text="color")
        self.color = tk.StringVar(self)
        self.color_input = tk.Entry(self.input_frame, textvariable=self.color, width=50)
        self.color_label.grid(row=3, column=0, sticky="w", padx=(20, 10), pady=5)
        self.color_input.grid(row=3, column=1, padx=(10, 20), pady=5)
        ## Velocity label + input
        self.velocity_label = tk.Label(self.input_frame, text="velocity(m/s)")
        self.velocity = tk.StringVar(self)
        self.velocity_input = tk.Entry(self.input_frame, textvariable=self.velocity, width=50)
        self.velocity_label.grid(row=4, column=0, sticky="w", padx=(20, 10), pady=5)
        self.velocity_input.grid(row=4, column=1, padx=(10, 20), pady=5)
        ################################################################
        # Control frame
        self.control_frame = tk.Frame(self)
        self.control_frame.pack(side="bottom")
        ## Ok button
        self.ok_button = tk.Button(self.control_frame, text="Ok", width=10, command=self.click_ok)
        self.ok_button.grid(row=5, column=0, padx=10, pady=5)
        ## Cancel button
        self.cancel_button = tk.Button(self.control_frame, text="Cancel", width=10, command=self.close)
        self.cancel_button.grid(row=5, column=1, padx=10, pady=5)
        ## error msg 
        self.error_msg = tk.StringVar(value="Please fill all the blanks")
        self.error_label = tk.Label(self.control_frame, textvariable=self.error_msg)
        self.error_label.grid(row=6, column=0, columnspan=2, sticky="nsew", pady=(5, 10))
        ################################################################
        self.mainloop()
    
    def close(self):
        """Close the create window
        """        
        self.destroy()
        self.quit()
        
    def click_ok(self):
        """Submit the form
        """        
        self.check_form()
        if self.planet:
            self.close()
        else:
            self.reset_form()

    def check_form(self):
        """Check the form
        """        
        ## check name if it is filled
        if self.name_input.get() == "":
            self.error_msg.set("You must fill the name of your planet")
        ## check if data is valid
        try:
            self.planet = {"name" : self.name_input.get(),
                "mass" : float(self.mass_input.get()), 
                "radius" : float(self.radius_input.get()),
                "color" : self.color_input.get(),
            "velocity" : float(self.velocity_input.get()),
                }
        except ValueError:
            self.planet = None
            self.error_msg.set("Invalid data")
        ## check if color is valid
        try:
            self.test_color = tk.Label(background=self.color_input.get())
        except:
            self.planet = None
            self.error_msg.set("Your color is not valid")

    def reset_form(self):
        """Reset the form
        """        
        self.name.set("")
        self.mass.set("")
        self.radius.set("")
        self.color.set("")
        self.velocity.set("")
        
