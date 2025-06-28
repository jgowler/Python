import customtkinter as ctk
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import threading
import time
import subprocess
import platform


class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        # Build window:
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        # Build top frame:
        self.Frame1()
        # Build button frame:
        self.ButtonFrame()
        # Build output frame:
        self.OutputFrame()
        # Build Status Bar:
        self.StatusBar()
        
        

    def Frame1(self):
        frame1 = ctk.CTkFrame(self)
        frame1.pack(fill = "x", padx = 10, pady = 10)
        # Source IP address details:
        self.SrcIP_entry = ctk.CTkEntry(frame1, placeholder_text="Source IP Address")
        self.SrcIP_entry.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.SrcLocalhost = ctk.CTkCheckBox(frame1, text = "Use Localhost", command=self.SrcLocahostToggle)
        self.SrcLocalhost.grid(row = 0, column = 1, padx = 5, pady = 5)      
        # Destination IP adress details:
        self.DestIP_entry = ctk.CTkEntry(frame1, placeholder_text="Destination IP Address")
        self.DestIP_entry.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.DestLocalhost = ctk.CTkCheckBox(frame1, text = "Use Localhost", command=self.DestLocalhostToggle)
        self.DestLocalhost.grid(row = 1, column = 1, padx = 5, pady = 5)


        return frame1
    
    def ButtonFrame(self):
        # Create the button frame:
        buttonframe = ctk.CTkFrame(self)
        buttonframe.pack(fill = "x", padx = 10, pady = 5)
        # Create the Ping button:
        self.ping_button = ctk.CTkButton(buttonframe, text = "Ping", command=self.Ping)
        self.ping_button.pack(side = "left", padx = 5, pady = 5)
        # Create the Traceroute button:
        self.tracert_button = ctk.CTkButton(buttonframe, text = "Traceroute")
        self.tracert_button.pack(side = "left", padx = 5, pady = 5)
        # Create Portscan button:
        self.portscan_button = ctk.CTkButton(buttonframe, text = "Portscan")
        self.portscan_button.pack(side = "left", padx = 5, pady = 5)
        # Create Clear button:
        self.clear_button = ctk.CTkButton(buttonframe, text = "Clear")
        self.clear_button.pack(side = "left", padx = 5, pady = 5)

        return buttonframe
    
    def OutputFrame(self):
        output_frame = ctk.CTkFrame(self)
        output_frame.pack(fill = "both", expand = True, padx = 10, pady = 10)
        self.output_text = ctk.CTkTextbox(output_frame)
        self.output_text.pack(fill = "both", expand = True)

        return output_frame
    
    def StatusBar(self, message="Ready"):
        status_bar = ctk.CTkLabel(self, text = message)
        status_bar.pack(side = "bottom", fill = "x", padx = 10, pady = 5)

        return status_bar

    def SrcLocahostToggle(self):
        if self.SrcLocalhost.get():
            self.SrcIP_entry.delete(0, "end")
            self.SrcIP_entry.insert(0, "127.0.0.1")
            self.SrcIP_entry.configure(state = "disabled")
        else:
            self.SrcIP_entry.configure(state = "normal")
            self.SrcIP_entry.delete(0, "end")

    def DestLocalhostToggle(self):
        if self.DestLocalhost.get():
            self.DestIP_entry.delete(0, "end")
            self.DestIP_entry.insert(0, "127.0.0.1")
            self.DestIP_entry.configure(state = "disabled")
        else:
            self.DestIP_entry.configure(state = "normal")
            self.DestIP_entry.delete(0, "end")

    def Ping(self):
        threading.Thread(target=self, daemon=True).start()
        self.after(0, lambda: self.StatusBar("Running Ping..."))
        src = self.SrcIP_entry.get()
        dst = self.DestIP_entry.get()
        
        if not self.SrcIP_entry:
            src = "127.0.0.1"

        if not dst:
            self.after(0, lambda: self.StatusBar("Please enter a destination IP address"))
            return

        count = "-n" if platform.system().lower() == "windows" else "-c"
        command = [
            "ping", count, "4", dst
        ]
        
        if src == "127.0.0.1" or src.lower() == "localhost":
            try:
                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                output = result.stdout or result.stderr or "No output"
            except subprocess.TimeoutExpired:
                output = "Ping timed out"
            except Exception as e:
                output = f"Error: {e}"

        else:
            ps_command = f'''
            Invoke-Command -ComputerName {src} -ScriptBlock {{
                Test-Connection -ComputerName {dst} -Count 4 | Out-String
            }}
            '''
            try:
                result = subprocess.run(
                    ["powershell",
                     "-Command",
                     ps_command],
                     capture_output=True,
                     text=True,
                     timeout=20
                )
                output = result.stdout or result.stderr or "No output"
            except subprocess.TimeoutExpired:
                output = "Remote ping timed out"
            except Exception as e:
                output = f"Error running remote ping: {e}"
        
        # Update output and status bar:
        self.after(0, lambda: self.output_text.delete("1.0", "end"))
        self.after(0, lambda: self.output_text.insert("end", output))
        self.after(0, lambda: self.StatusBar("Ping complete."))


''' To work on next:

Ping test will run but the status bar is not updating correctly. this needs to clear during each step as it is currently stacking instead.

'''
if __name__ == "__main__":
    App('Sample title', (600, 500)).mainloop()


