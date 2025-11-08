import os

import customtkinter

from src import database
from src.frame import AllWarrentiesFrame, AddNewWarrantyFrame, SidebarFrame


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
        self.sidebar_frame = SidebarFrame(self, width=220)

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
        self.move_to_adding_new_warranty_page_button.pack(padx=10, pady=(5, 10))

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

        if name == "" or facebook == "" or phone_number == "":
            return

        new_warranty = {
            "name": name,
            "facebook": facebook,
            "phone_number": phone_number,
            "expired_date": expired_date,
        }
        database.add_warranty(new_warranty)

        self.adding_new_warranty_frame.clear_entries()


def main():
    if not os.path.exists(database.DATABASE_PATH):
        database.create_database()

    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
