import tkinter as tk
import sys
from PIL import Image, ImageTk

# pip3 install pillow

class UnitConverter(tk.Frame):
    def __init__(self, root):
        self.colour1 = "#AF9164"
        self.colour2 = "#F7F3E3"
        self.colour3 = "#000000"

        self.conversions_available = ['km --> mi',
                                      'mi --> k',
                                      'kg --> lbs',
                                      'lbs --> kg',
                                      '°C --> °F',
                                      '°F --> °C ']

        super().__init__(
            root,
            bg=self.colour1
        )

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(3, weight=1)
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(
            self.main_frame,
            bg=self.colour1,
            fg=self.colour2,
            font=('Arial', 22, 'bold'),
            text='Unit Converter-Deepak V.R'
        )
        self.title.grid(column=0, row=0, sticky=tk.EW, pady=(10, 20))
        self.conversion = tk.StringVar()
        self.conversion.set(self.conversions_available[0])

        self.select_conversion = tk.OptionMenu(
            self.main_frame,
            self.conversion,
            *self.conversions_available
        )

        self.select_conversion.config(
            bg=self.colour3,
            fg=self.colour2,
            activebackground=self.colour3,
            activeforeground=self.colour1,
            font=('Arial', 14),
            border=0,
            highlightthickness=0,
            indicatoron=0
        )

        self.select_conversion['menu'].config(
            bg=self.colour3,
            fg=self.colour1,
            activebackground=self.colour1,
            activeforeground=self.colour2,
            font=('Arial', 14),
            activeborderwidth=0,
            border=1,
            relief=tk.FLAT
        )
#Deepak V.R
        self.select_conversion.grid(column=0, row=1, sticky=tk.EW, padx=50)

        self.container_values = tk.Frame(self.main_frame, bg=self.colour1)
        self.container_values.columnconfigure(1, weight=1)
        self.container_values.grid(column=0, row=2, sticky=tk.NSEW, padx=50, pady=40)

        value_validation_command = self.container_values.register(self.value_validation)

        self.value_to_convert = tk.Entry(
            self.container_values,
            bg=self.colour3,
            fg=self.colour1,
            selectbackground=self.colour1,
            selectforeground=self.colour2,
            font=('Arial', 14),
            highlightthickness=0,
            border=0,
            justify=tk.CENTER,
            width=11,
            validate='key',
            validatecommand=(value_validation_command, '%P')
        )
        self.value_to_convert.grid(column=0, row=0, sticky=tk.N, ipady=3)

        self.convert_button = tk.Button(
            self.container_values,
            text="CLick Me!",
            bg="black",
            fg="black",
            font=('Arial', 12),
            borderwidth=0,
            relief=tk.RAISED,
            command=self.convert_value,
#Deepak V.R
        )
        self.convert_button.grid(column=1, row=0, sticky=tk.N)

        self.converted_value = tk.StringVar()
        self.entry_converted_value = tk.Entry(
            self.container_values,
            bg=self.colour3,
            fg=self.colour1,
            disabledbackground=self.colour3,
            disabledforeground=self.colour2,
            font=('Arial', 14),
            highlightthickness=0,
            border=0,
            justify=tk.CENTER,
            width=11,
            state='disabled',
            cursor='arrow',
            textvariable=self.converted_value
        )
        self.entry_converted_value.grid(column=2, row=0, sticky=tk.N, ipady=3)

    def value_validation(self, value):
        if not value or value == '-':
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False

    def convert_value(self):
        conversion_type = self.conversion.get()

        if not self.value_to_convert.get() or self.value_to_convert.get() == '-':
            self.converted_value.set('')
            return

        value_to_convert_local = float(self.value_to_convert.get())

        if conversion_type == 'km --> mi':
            self.converted_value.set(f'{value_to_convert_local * 0.62:.2f}')
        elif conversion_type == 'mi --> k':
            self.converted_value.set(f'{value_to_convert_local * 1.61:.2f}')
        elif conversion_type == 'kg --> lbs':
            self.converted_value.set(f'{value_to_convert_local * 2.20462:.2f}')
        elif conversion_type == 'lbs --> kg':
            self.converted_value.set(f'{value_to_convert_local * 0.453592:.2f}')
        elif conversion_type == '°C --> °F':
            self.converted_value.set(f'{value_to_convert_local * 9/5 + 32:.2f}')
        elif conversion_type == '°F --> °C':
            self.converted_value.set(f'{(value_to_convert_local - 32) * 5/9:.2f}')
        else:
            self.converted_value.set('Invalid conversion type')


operating_system = sys.platform
root = tk.Tk()
unit_converter_app = UnitConverter(root)
root.title('Unit Converter')

if 'win' in operating_system:
    root.geometry('450x210')
elif 'linux' in operating_system:
    root.geometry('450x230')
elif 'darwin' in operating_system:
    root.geometry('450x230')

root.resizable(width=False, height=False)

root.mainloop()



#Deepak V.R