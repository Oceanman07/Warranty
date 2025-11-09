import os
import webbrowser

import customtkinter

from src import database
from src.constants import DATABASE_PATH
from src.frame import AllWarrentiesFrame, AddNewWarrantyFrame, SidebarFrame
from src.popup import DetailWarrantyPopop


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("light")
        self.title("Warranty")
        self.geometry("1330x790")

        self.font = customtkinter.CTkFont(family="JetBrains Mono")

        # ============== MainContentFrame ==========
        self.content_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.content_frame.pack(
            padx=(5, 10), pady=10, side="right", fill="both", expand=True
        )

        self.all_warrenties_frame = AllWarrentiesFrame(self.content_frame)
        self.adding_new_warranty_frame = AddNewWarrantyFrame(self.content_frame)

        for frame in (self.all_warrenties_frame, self.adding_new_warranty_frame):
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.all_warrenties_frame.lift()

        self.adding_new_warranty_button = customtkinter.CTkButton(
            self.adding_new_warranty_frame,
            text="Add",
            font=self.font,
            command=self.add_new_warranty,
        )
        self.adding_new_warranty_button.pack(
            padx=10, pady=(0, 10), side="bottom", anchor="e"
        )

        # ============== SidebarFrame ==============
        self.sidebar_frame = SidebarFrame(self)

        self.move_to_all_warranties_page_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="All",
            font=self.font,
            command=self.move_to_all_warranties_page,
        )
        self.move_to_all_warranties_page_button.pack(padx=10, pady=(15, 10))

        self.move_to_adding_new_warranty_page_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="New",
            font=self.font,
            command=self.move_to_adding_new_warranty_page,
        )
        self.move_to_adding_new_warranty_page_button.pack(padx=10, pady=(0, 10))

        self.open_facebook_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Open facebook",
            font=self.font,
            command=self.open_facebook,
        )
        self.open_facebook_button.pack(padx=10, pady=(0, 10))

        self.delete_warranty_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Delete",
            font=self.font,
            command=self.delete_warranty,
        )
        self.delete_warranty_button.pack(padx=10, pady=(0, 10))

        self.change_appr_mode_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Light",
            font=self.font,
            command=self.change_appearance_mode,
        )
        self.change_appr_mode_button.pack(
            padx=10,
            pady=(0, 10),
            side="bottom",
        )

        # ============== Popup ==============
        self.show_detail_warranty_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="More",
            font=self.font,
            command=self.show_detail_warranty,
        )
        self.show_detail_warranty_button.pack(padx=10, pady=(0, 10))

    def change_appearance_mode(self):
        if customtkinter.get_appearance_mode() == "Light":
            customtkinter.set_appearance_mode("dark")
            self.change_appr_mode_button.configure(text="Dark")
        else:
            customtkinter.set_appearance_mode("light")
            self.change_appr_mode_button.configure(text="Light")

    def move_to_all_warranties_page(self):
        self.all_warrenties_frame.list()
        self.all_warrenties_frame.lift()

    def move_to_adding_new_warranty_page(self):
        self.adding_new_warranty_frame.clear_entries()
        self.adding_new_warranty_frame.lift()

    def add_new_warranty(self):
        name = self.adding_new_warranty_frame.name_entry
        facebook = self.adding_new_warranty_frame.facebook_entry
        phone_number = self.adding_new_warranty_frame.phone_number_entry
        expired_date = self.adding_new_warranty_frame.expired_date_entry
        note = self.adding_new_warranty_frame.note_entry

        if name == "" or facebook == "" or phone_number == "":
            return

        new_warranty = {
            "name": name,
            "facebook": facebook,
            "phone_number": phone_number,
            "expired_date": expired_date,
            "note": note,
        }
        database.add_warranty(new_warranty)

        self.adding_new_warranty_frame.clear_entries()

    def open_facebook(self):
        if not self.all_warrenties_frame.is_selected_button():
            return

        facebook = self.all_warrenties_frame.selected_warranty_facebook
        webbrowser.open(facebook)

    def show_detail_warranty(self):
        if not self.all_warrenties_frame.is_selected_button():
            return

        detail_warranty_popup = DetailWarrantyPopop(self)
        detail_warranty_popup.show_name(
            self.all_warrenties_frame.selected_warranty_name
        )
        detail_warranty_popup.show_phone_number(
            self.all_warrenties_frame.selected_warranty_phone_number
        )
        detail_warranty_popup.show_expired_date(
            self.all_warrenties_frame.selected_warranty_expired_datetime
        )
        detail_warranty_popup.show_warranty_status(
            self.all_warrenties_frame.selected_warranty_status
        )
        detail_warranty_popup.show_note(
            self.all_warrenties_frame.selected_warranty_note
        )

    def delete_warranty(self):
        if not self.all_warrenties_frame.is_selected_button():
            return

        self.all_warrenties_frame.delete_selected_warranty()
        self.all_warrenties_frame.list()
        self.all_warrenties_frame.lift()


def main():
    if not os.path.exists(DATABASE_PATH):
        database.create_database()

    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
