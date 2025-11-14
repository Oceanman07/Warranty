import os
import tkinter
import webbrowser

import customtkinter

from src import database
from src.constants import DATABASE_PATH
from src.frame import AllWarrentiesFrame, NewWarrantyFrame, SidebarFrame
from src.popup import DetailWarrantyPopop


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("light")
        self.title("Warranty")
        self.geometry("1330x790")

        self.font = customtkinter.CTkFont(family="JetBrains Mono")

        # ============== MenuFunctionsForWarranty =================
        self.warranty_functions_menu = tkinter.Menu(self, tearoff=0)
        self.warranty_functions_menu.add_command(
            label="More", command=self.show_detail_warranty
        )
        self.warranty_functions_menu.add_command(
            label="Edit", command=self.move_to_update_warranty_page
        )
        self.warranty_functions_menu.add_command(
            label="Open facebook", command=self.open_warranty_facebook
        )
        self.warranty_functions_menu.add_command(
            label="Delete",
            command=self.delete_warranty,
        )

        # ============== MainContentFrame ==========
        self.content_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.content_frame.pack(
            padx=(5, 10), pady=10, side="right", fill="both", expand=True
        )

        self.all_warrenties_frame = AllWarrentiesFrame(self.content_frame)
        self.new_warranty_frame = NewWarrantyFrame(self.content_frame)

        for frame in (self.all_warrenties_frame, self.new_warranty_frame):
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # show all_warrenties_frame first
        self.all_warrenties_frame.list(self.warranty_functions_menu)
        self.all_warrenties_frame.lift()

        self.add_warranty_button = customtkinter.CTkButton(
            self.new_warranty_frame,
            text="Add",
            font=self.font,
            command=self.add_warranty,
        )
        self.add_warranty_button.pack(padx=10, pady=(0, 10), side="bottom", anchor="e")

        self.apply_update_warranty_button = customtkinter.CTkButton(
            self.new_warranty_frame,
            text="Apply",
            font=self.font,
            command=self.apply_update_warranty,
        )
        self.apply_update_warranty_button.pack(
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

        self.move_to_add_warranty_page_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="New",
            font=self.font,
            command=self.move_to_add_warranty_page,
        )
        self.move_to_add_warranty_page_button.pack(padx=10, pady=(0, 10))

        self.change_appearance_mode_button = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Light",
            font=self.font,
            command=self.change_appearance_mode,
        )
        self.change_appearance_mode_button.pack(
            padx=10,
            pady=(0, 10),
            side="bottom",
        )

    def change_appearance_mode(self):
        if customtkinter.get_appearance_mode() == "Light":
            customtkinter.set_appearance_mode("dark")
            self.change_appearance_mode_button.configure(text="Dark")
            self.all_warrenties_frame.configure(label_fg_color="#C4C4C4")
        else:
            customtkinter.set_appearance_mode("light")
            self.change_appearance_mode_button.configure(text="Light")
            self.all_warrenties_frame.configure(label_fg_color="#F2F2F2")

    def move_to_all_warranties_page(self):
        self.all_warrenties_frame.list(self.warranty_functions_menu)
        self.all_warrenties_frame.lift()

    def move_to_add_warranty_page(self):
        self.apply_update_warranty_button.pack_forget()
        self.add_warranty_button.pack(padx=10, pady=(0, 10), side="bottom", anchor="e")

        self.new_warranty_frame.clear_entries()
        self.new_warranty_frame.lift()

    def move_to_update_warranty_page(self):
        if not self.all_warrenties_frame.is_selected_warranty_button():
            return

        self.add_warranty_button.pack_forget()
        self.apply_update_warranty_button.pack(
            padx=10, pady=(0, 10), side="bottom", anchor="e"
        )
        self.new_warranty_frame.clear_entries()

        self.new_warranty_frame.insert_name_entry(
            self.all_warrenties_frame.selected_warranty_name
        )
        self.new_warranty_frame.insert_facebook_entry(
            self.all_warrenties_frame.selected_warranty_facebook
        )
        self.new_warranty_frame.insert_phone_number_entry(
            self.all_warrenties_frame.selected_warranty_phone_number
        )
        self.new_warranty_frame.insert_expired_date(
            self.all_warrenties_frame.selected_warranty_expired_datetime
        )
        self.new_warranty_frame.insert_note_entry(
            self.all_warrenties_frame.selected_warranty_note
        )

        self.new_warranty_frame.lift()

    def add_warranty(self):
        new_warranty = {
            "name": self.new_warranty_frame.name_entry,
            "facebook": self.new_warranty_frame.facebook_entry,
            "phone_number": self.new_warranty_frame.phone_number_entry,
            "expired_date": self.new_warranty_frame.expired_date_entry,
            "note": self.new_warranty_frame.note_entry,
        }
        database.add_warranty(new_warranty)

        self.new_warranty_frame.clear_entries()

    def apply_update_warranty(self):
        new_warranty = {
            "id": self.all_warrenties_frame.selected_warranty_id,
            "name": self.new_warranty_frame.name_entry,
            "facebook": self.new_warranty_frame.facebook_entry,
            "phone_number": self.new_warranty_frame.phone_number_entry,
            "expired_date": self.new_warranty_frame.expired_date_entry,
            "note": self.new_warranty_frame.note_entry,
        }
        database.update_warranty(new_warranty)

        self.new_warranty_frame.clear_entries()
        self.all_warrenties_frame.list(self.warranty_functions_menu)
        self.all_warrenties_frame.lift()

    def open_warranty_facebook(self):
        if not self.all_warrenties_frame.is_selected_warranty_button():
            return

        webbrowser.open(self.all_warrenties_frame.selected_warranty_facebook)

    def show_detail_warranty(self):
        if not self.all_warrenties_frame.is_selected_warranty_button():
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
        if not self.all_warrenties_frame.is_selected_warranty_button():
            return

        warranty_id = self.all_warrenties_frame.selected_warranty_id
        database.delete_warranty(warranty_id)

        self.all_warrenties_frame.reset_selected_warranty_button()
        self.all_warrenties_frame.list(self.warranty_functions_menu)
        self.all_warrenties_frame.lift()


def main():
    if not os.path.exists(DATABASE_PATH):
        database.create_database()

    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
