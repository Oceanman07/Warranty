import datetime

import customtkinter
import tkcalendar

from . import database
from . import utils


class SidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(padx=10, pady=10, side="left", fill="y")


class AllWarrentiesFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.list()

    def clear_items(self):
        for item in self.winfo_children():
            item.destroy()

    def list(self):
        self.clear_items()

        all_warrenties = database.get_all_warranties()
        for warranty in all_warrenties:
            customtkinter.CTkLabel(
                self,
                text=f"{warranty['name']}  :  {warranty['phone_number']}  :  {warranty['expired_date']}",
            ).pack()


class AddNewWarrantyFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.__font = customtkinter.CTkFont(size=19)

        customtkinter.CTkLabel(self, text="Full name:", font=self.__font).pack(
            padx=20, pady=(10, 0), anchor="w"
        )
        self.__name_entry = customtkinter.CTkEntry(self, font=self.__font)
        self.__name_entry.pack(padx=20, pady=(2, 20), fill="x")

        customtkinter.CTkLabel(self, text="Facebook:", font=self.__font).pack(
            padx=20, anchor="w"
        )
        self.__facebook_entry = customtkinter.CTkEntry(self, font=self.__font)
        self.__facebook_entry.pack(padx=20, pady=(2, 20), fill="x")

        customtkinter.CTkLabel(self, text="Phone number:", font=self.__font).pack(
            padx=20, anchor="w"
        )
        self.__phone_number_entry = customtkinter.CTkEntry(self, font=self.__font)
        self.__phone_number_entry.pack(padx=20, pady=(2, 20), fill="x")

        customtkinter.CTkLabel(self, text="Expired date:", font=self.__font).pack(
            padx=20, anchor="w"
        )
        self.__expired_date_entry = tkcalendar.DateEntry(
            self,
            font=self.__font,
            width=20,
            background="lightblue",
            foreground="black",
            borderwidth=2,
            date_pattern="dd/MM/yyyy",
        )
        self.__expired_date_entry.pack(padx=20, pady=(2, 20), fill="x")

    def clear_entries(self):
        for entry in (
            self.__name_entry,
            self.__facebook_entry,
            self.__phone_number_entry,
        ):
            entry.delete(0, "end")

        self.__expired_date_entry.set_date(datetime.date.today())

    @property
    def name_entry(self):
        return self.__name_entry.get().strip()

    @property
    def facebook_entry(self):
        return self.__facebook_entry.get().strip()

    @property
    def phone_number_entry(self):
        return self.__phone_number_entry.get().strip()

    @property
    def expired_date_entry(self):
        return utils.convert_unix_time(self.__expired_date_entry.get_date())
