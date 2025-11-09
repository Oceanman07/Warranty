import datetime
import functools

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
        self.__font = customtkinter.CTkFont(family="JetBrains Mono", size=16)
        self.__text_color = "#242424"
        self.__fg_color = "#C4C4C4"
        self.__title = f"Full name{' ' * (40 - 9)}Phone number{' ' * (31 - 12)}Expired date{' ' * (26 - 12)}Status"

        super().__init__(
            master,
            label_text=self.__title,
            label_font=self.__font,
            label_anchor="w",
            label_fg_color="#F2F2F2",
        )

        self.__current_unix_time = int(datetime.datetime.now().timestamp())
        self.__warranties_info = {}
        self.__selected_button = None

        self.list()

    def is_selected_button(self):
        return self.__selected_button

    @property
    def selected_warranty_name(self):
        return self.__warranties_info[self.__selected_button]["name"]

    @property
    def selected_warranty_facebook(self):
        return self.__warranties_info[self.__selected_button]["facebook"]

    @property
    def selected_warranty_phone_number(self):
        return self.__warranties_info[self.__selected_button]["phone_number"]

    @property
    def selected_warranty_expired_datetime(self):
        return self.__warranties_info[self.__selected_button]["expired_datetime"]

    @property
    def selected_warranty_status(self):
        return self.__warranties_info[self.__selected_button]["warranty_status"]

    @property
    def selected_warranty_note(self):
        return self.__warranties_info[self.__selected_button]["note"]

    def delete_selected_warranty(self):
        if self.__selected_button:
            warranty_id = self.__warranties_info[self.__selected_button]["id"]
            database.delete_warranty(warranty_id)
            self.__selected_button.destroy()
            self.__selected_button = None

    def __do_selected(self, self_button: customtkinter.CTkButton):
        if self.__selected_button:
            self.__selected_button.configure(fg_color=self.__fg_color)

        self.__selected_button = self_button
        self.__selected_button.configure(fg_color="#3B8ED0")

    def __add_warranty_info(self, info):
        text = f"{info['name']}{' ' * (41 - len(info['name']))}{info['phone_number']}{' ' * (31 - len(str(info['phone_number'])))}{info['expired_datetime']}{' ' * (25 - len(info['expired_datetime']))}{info['warranty_status']}"
        info_button = customtkinter.CTkButton(
            self,
            font=self.__font,
            text=text,
            anchor="w",
            text_color=self.__text_color,
            fg_color=self.__fg_color,
            corner_radius=0,
        )
        info_button.configure(
            command=functools.partial(self.__do_selected, info_button),
        )
        info_button.pack(fill="x", pady=(0, 5))

        self.__warranties_info[info_button] = info

    def __get_warranty_status(self, expired_unix_time):
        if expired_unix_time - self.__current_unix_time <= 0:
            return "Expired"
        return "Active"

    def list(self):
        self.clear_items()
        self.__warranties_info.clear()
        self.__selected_button = None

        all_warrenties = database.get_all_warranties()
        for warranty in all_warrenties:
            info = {
                "id": warranty["id"],
                "name": warranty["name"],
                "facebook": warranty["facebook"],
                "phone_number": warranty["phone_number"],
                "expired_datetime": utils.convert_datetime(warranty["expired_date"]),
                "note": warranty["note"],
                "warranty_status": self.__get_warranty_status(warranty["expired_date"]),
            }
            self.__add_warranty_info(info)

    def clear_items(self):
        for item in self.winfo_children():
            item.destroy()


class AddNewWarrantyFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.__font = customtkinter.CTkFont(family="JetBrains Mono", size=19)

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

        customtkinter.CTkLabel(self, text="Note:", font=self.__font).pack(
            padx=20, anchor="w"
        )
        self.__note_entry = customtkinter.CTkTextbox(self, font=self.__font)
        self.__note_entry.pack(padx=20, pady=(2, 20), fill="both", expand=True)

    def clear_entries(self):
        for entry in (
            self.__name_entry,
            self.__facebook_entry,
            self.__phone_number_entry,
        ):
            entry.delete(0, "end")

        self.__expired_date_entry.set_date(datetime.date.today())
        self.__note_entry.delete("0.0", "end")

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

    @property
    def note_entry(self):
        return self.__note_entry.get("0.0", "end").strip()
