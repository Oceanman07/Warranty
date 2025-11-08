import os
import datetime

import customtkinter
import tkcalendar

from src.database import (
    DATABASE_PATH,
    create_database,
    add_warranty,
    get_all_warranties,
)


class SidebarFunctionsFrame(customtkinter.CTkFrame):
    def __init__(
        self, master, all_warrenties_frame, adding_new_warrenty_frame, **kwargs
    ):
        super().__init__(master, **kwargs)
        self.all_warrenties_frame = all_warrenties_frame
        self.adding_new_warrenty_frame = adding_new_warrenty_frame

        self.move_to_all_warranties_page_button = customtkinter.CTkButton(
            self, text="All", command=self.move_to_all_warranties_page
        )
        self.move_to_all_warranties_page_button.pack(padx=10, pady=(15, 10))

        self.move_to_adding_new_warranty_page_button = customtkinter.CTkButton(
            self, text="New", command=self.move_to_adding_new_warranty_page
        )
        self.move_to_adding_new_warranty_page_button.pack(padx=10, pady=(5, 10))

        self.change_appr_mode_button = customtkinter.CTkButton(
            master, text="Light", command=self.change_appearance_mode
        )
        self.change_appr_mode_button.pack(
            padx=10, pady=(0, 10), side="bottom", fill="x"
        )

    def move_to_all_warranties_page(self):
        self.all_warrenties_frame.lift()
        self.all_warrenties_frame.list()

    def move_to_adding_new_warranty_page(self):
        self.adding_new_warrenty_frame.lift()

    def change_appearance_mode(self):
        if customtkinter.get_appearance_mode() == "Light":
            customtkinter.set_appearance_mode("dark")
            self.change_appr_mode_button.configure(text="Dark")
        else:
            customtkinter.set_appearance_mode("light")
            self.change_appr_mode_button.configure(text="Light")


class AllWarrentiesFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.list()

    def clear_items(self):
        for item in self.winfo_children():
            item.destroy()

    def list(self):
        self.clear_items()

        all_warrenties = get_all_warranties()
        for warranty in all_warrenties:
            customtkinter.CTkLabel(
                self,
                text=f"{warranty['name']}  :  {warranty['phone_number']}  :  {warranty['expired_date']}",
            ).pack()


class AddNewWarrantyFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.font = customtkinter.CTkFont(size=19)

        self.name_entry = customtkinter.CTkEntry(
            self, font=self.font, placeholder_text="Name"
        )
        self.name_entry.pack(padx=20, pady=20, fill="x")

        self.facebook_entry = customtkinter.CTkEntry(
            self, font=self.font, placeholder_text="Facebook"
        )
        self.facebook_entry.pack(padx=20, pady=20, fill="x")

        self.phone_number_entry = customtkinter.CTkEntry(
            self, font=self.font, placeholder_text="Phone"
        )
        self.phone_number_entry.pack(padx=20, pady=20, fill="x")

        self.expired_date_entry = tkcalendar.DateEntry(
            self,
            font=self.font,
            width=20,
            background="lightblue",
            foreground="black",
            borderwidth=2,
            date_pattern="dd/MM/yyyy",
        )
        self.expired_date_entry.pack(padx=20, pady=20, fill="x")

        self.adding_new_warranty_button = customtkinter.CTkButton(
            self, text="Add", font=self.font, command=self.add_new_warranty
        )
        self.adding_new_warranty_button.pack(
            padx=10, pady=(0, 10), side="bottom", anchor="e"
        )

    def clear_entries(self):
        for entry in (
            self.name_entry,
            self.facebook_entry,
            self.phone_number_entry,
        ):
            entry.delete(0, "end")

        self.expired_date_entry.set_date(datetime.date.today())

    def convert_unix_time(self, date):
        datetime_obj = datetime.datetime.combine(date, datetime.datetime.min.time())
        return int(datetime_obj.timestamp())

    def add_new_warranty(self):
        new_warranty = {
            "name": self.name_entry.get().strip(),
            "facebook": self.facebook_entry.get().strip(),
            "phone_number": self.phone_number_entry.get().strip(),
            "expired_date": self.convert_unix_time(self.expired_date_entry.get_date()),
        }
        add_warranty(new_warranty)

        self.clear_entries()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("light")
        self.title("Warranty")
        self.geometry("1300x700")

        # display warranty, adding new, updating, ... frames
        self.content_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.content_frame.pack(
            padx=(5, 10), pady=10, side="right", fill="both", expand=True
        )

        self.all_warrenties_frame = AllWarrentiesFrame(self.content_frame)
        self.adding_new_warranty_frame = AddNewWarrantyFrame(self.content_frame)

        for frame in (self.all_warrenties_frame, self.adding_new_warranty_frame):
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.all_warrenties_frame.lift()

        # side bar functions for adding new, updating, ...
        self.functions_frame = SidebarFunctionsFrame(
            self, self.all_warrenties_frame, self.adding_new_warranty_frame, width=220
        )
        self.functions_frame.pack(padx=10, pady=10, side="left", fill="y")


def main():
    if not os.path.exists(DATABASE_PATH):
        create_database()

    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
