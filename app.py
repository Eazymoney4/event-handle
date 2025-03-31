import tkinter as tk

class InchesToCentimetersConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Inches to Centimeters Converter")

        self.inches_label = tk.Label(self.window, text="Enter length in inches:")
        self.inches_label.pack()

        self.inches_entry = tk.Entry(self.window)
        self.inches_entry.pack()

        self.convert_button = tk.Button(self.window, text="Convert to Centimeters", command=self.convert_inches_to_centimeters)
        self.convert_button.pack()

        self.centimeters_label = tk.Label(self.window, text="")
        self.centimeters_label.pack()

    def convert_inches_to_centimeters(self):
        try:
            inches = float(self.inches_entry.get())
            centimeters = inches * 2.54
            self.centimeters_label.config(text=f"{inches} inches is equal to {centimeters:.2f} centimeters")
        except ValueError:
            self.centimeters_label.config(text="Invalid input. Please enter a valid number.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    converter = InchesToCentimetersConverter()
    converter.run()
