import customtkinter as ctk
from main import *
from interpreter import interpret

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("720x540")

program_code = ''
filePath = "../asm/asmFile.asm"
with open(filePath, "r") as file:
		program_code = file.read()

'''
with open("cpu_registers.txt", "r") as file:
	 registers = file.read()
'''

class CPU:
    def __init__(self):
        self.registers = {'rax': 0, 'rbx': 0, 'rcx': 0, 'rdx': 0, 'rsp': 0, 'rbp': 0, 'rsi': 0, 'rdi': 0}

    def print_registers(self):
        register_contents = "\n".join([f"{reg}: {val}" for reg, val in self.registers.items()])
        label_register.configure(text=register_contents)

    def update_registers(self, new_values):
        for register, value in new_values.items():
            if register in self.registers:
                self.registers[register] = value
        self.print_registers()

frame1 = ctk.CTkFrame(master=root)
frame1.pack(side="left", pady=12, padx=10, fill="both", expand=True)

frame2 = ctk.CTkFrame(master=root)
frame2.pack(side="right", pady=12, padx=10, fill="both", expand=True)

label1 = ctk.CTkLabel(master=frame1, text="Line Of Code")
label1.pack(pady=12, padx=10)

label2 = ctk.CTkLabel(master=frame2, text="Register Contents")
label2.pack(pady=12, padx=10)

label_register = ctk.CTkLabel(master=frame2)
label_register.pack(pady=12, padx=10)

program_text = ctk.CTkTextbox(master=frame1, wrap="word")
program_text.insert("1.0", program_code)
program_text.pack(expand=True, fill="both")

cpu = CPU()

new_values = {'rax': 10, 'rbx': 20, 'rcx': 30, 'rdx': 40, 'rsp': 50, 'rbp': 60, 'rsi': 70, 'rdi': 80}
cpu.update_registers(new_values)

root.mainloop()

'''
register_text = ctk.CTkTextbox(master=frame2, wrap="word")
register_text.insert("1.0", registers)
register_text.pack(expand=True, fill="both")


entry1 = ctk.CTkEntry(master=frame, placeholder_text="Variables")
entry1.pack(pady=12, padx=10)

entry2 = ctk.CTkEntry(master=frame, placeholder_text="Values")
entry2.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

frame1_1 = ctk.CTkFrame(master=frame1)
frame1_1.pack(side="bottom", pady=12, padx=10, fill="both", expand = True)

label1_1 = ctk.CTkLabel(master=frame1_1, text="Code")
label1_1.pack(pady=12, padx=10)
'''