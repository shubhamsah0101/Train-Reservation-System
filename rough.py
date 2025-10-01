# # import tkinter as tk
# # from tkinter import ttk

# # root = tk.Tk()

# # root.geometry("300x300")

# # f = tk.Frame(root)
# # f.pack(fill="both", expand=True)

# # c = tk.Canvas(f)
# # c.pack(side="left", fill="both", expand=True)

# # sb = tk.Scrollbar(c, orient="vertical", command=c.yview)
# # sb.pack(side="right", fill="y")

# # sf = tk.Scrollbar(c)
# # sf.pack()

# # sel = tk.StringVar()
# # sel.set("Select")

# # def com():
# #     value = sel.get()
# #     print(value)

# # tk.Button(root, text="Print", command=com).pack(padx=50, pady=50)



# # cb = ttk.Combobox(root, textvariable=sel, values=("A", "B", "C"))
# # cb.pack(padx=20, pady=20)

# # root.mainloop()

# import tkinter as tk
# from tkinter import ttk

# class AutocompleteCombobox(ttk.Combobox):
#     def set_completion_list(self, completion_list):
#         """Set the list of possible strings."""
#         self._completion_list = sorted(completion_list, key=str.lower)
#         self['values'] = self._completion_list
#         self.bind('<KeyRelease>', self._check_input)

#     def _check_input(self, event):
#         typed = self.get()
#         if typed == '':
#             self['values'] = self._completion_list
#         else:
#             filtered = [item for item in self._completion_list if item.lower().startswith(typed.lower())]
#             self['values'] = filtered
#         # Open dropdown automatically if typing matches
#         if self['values']:
#             self.event_generate('<Down>')

# # Example usage
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("City Autocomplete Combobox")

#     cities = ["Delhi", "Deoghar", "Mumbai", "Kolkata", "Chennai", "Bengaluru",
#               "Hyderabad", "Jaipur", "Lucknow", "Patna", "Pune", "Bhubaneswar"]

#     label = ttk.Label(root, text="Select City:")
#     label.pack(pady=5)

#     combo = AutocompleteCombobox(root)
#     combo.set_completion_list(cities)
#     combo.pack(pady=10)

#     def show_selection():
#         print("Selected:", combo.get())

#     btn = ttk.Button(root, text="Confirm", command=show_selection)
#     btn.pack(pady=5)

#     root.mainloop()


import tkinter as tk
from tkcalendar import DateEntry
from datetime import date, timedelta

root = tk.Tk()
root.title("Reservation Date Picker")

# Today as minimum date
today = date.today()

# Next 60 days as maximum
max_day = today + timedelta(days=40)

label = tk.Label(root, text="Select Journey Date (Next 60 Days):")
label.pack(pady=5)

# Drop-down calendar restricted to next 60 days
cal = DateEntry(root,
                width=15,
                background='darkblue',
                foreground='white',
                borderwidth=2,
                mindate=today,
                maxdate=max_day,
                year=today.year,
                month=today.month,
                day=today.day)
cal.pack(pady=10)

def show_date():
    print("Selected Journey Date:", cal.get_date())

btn = tk.Button(root, text="Confirm", command=show_date)
btn.pack(pady=5)

root.mainloop()
