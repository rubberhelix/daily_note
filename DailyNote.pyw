import csv
import customtkinter as ctk
import datetime
from datetime import date

class DailyNote(ctk.CTk):
    """daily note UI class that display a note from a list of daily notes"""

    def __init__(self):
        super().__init__()

        # configure the window
        self.title("Daily Note")
        self.resizable(False, False)
        self.minsize(200, 125)
        ctk.set_appearance_mode("System")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # the daily note
        self.note = ctk.CTkLabel(self, text="", wraplength=350)
        self.note.grid(row=0, padx=25, pady=(20,0), sticky='ew')
        
        # 'close' button
        self.login_button = ctk.CTkButton(self, height=30, text="Close", command=self.destroy)
        self.login_button.grid(row=1, padx=30, pady=20, sticky='sew')

        # display the note
        self.display_note()

    def display_note(self):
        """opens/ reads notes file, displays note of the day on the UI"""

        with open('notes.csv', 'r') as file:
            reader = csv.reader(file)
            self.data = []
            for row in reader:
                self.data.extend(row)
        fmt = '%Y-%m-%d'
        today = str(date.today())
        sdtdate = datetime.datetime.strptime(today, fmt)
        sdtdate = sdtdate.timetuple()
        jdate = sdtdate.tm_yday
        note = self.data[jdate%len(self.data)]
        self.note.configure(text=note)

if __name__=="__main__":
    app = DailyNote()
    app.mainloop()
