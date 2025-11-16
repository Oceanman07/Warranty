import threading
import time

import customtkinter


class DetailWarrantyPopop(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Detail")
        self.geometry("800x600")

        self.__font = customtkinter.CTkFont(family="JetBrains Mono", size=19)

        self.__frame = customtkinter.CTkFrame(self)
        self.__frame.pack(padx=5, pady=5, fill="both", expand=True)

    def show_name(self, selected_warranty_name):
        customtkinter.CTkLabel(
            self.__frame,
            font=self.__font,
            text="Full name:",
            anchor="w",
        ).pack(padx=10, pady=(10, 2), fill="x")
        customtkinter.CTkButton(
            self.__frame,
            font=self.__font,
            text=selected_warranty_name,
            anchor="w",
        ).pack(padx=10, pady=(0, 10), fill="x")

    def show_phone_number(self, selected_warranty_phone_number):
        customtkinter.CTkLabel(
            self.__frame,
            font=self.__font,
            text="Phone number:",
            anchor="w",
        ).pack(padx=10, pady=(10, 2), fill="x")
        customtkinter.CTkButton(
            self.__frame,
            font=self.__font,
            text=selected_warranty_phone_number,
            anchor="w",
        ).pack(padx=10, pady=(0, 10), fill="x")

    def show_expired_date(self, selected_warranty_expired_datetime):
        customtkinter.CTkLabel(
            self.__frame,
            font=self.__font,
            text="Expired date:",
            anchor="w",
        ).pack(padx=10, pady=(10, 2), fill="x")
        customtkinter.CTkButton(
            self.__frame,
            font=self.__font,
            text=selected_warranty_expired_datetime,
            anchor="w",
        ).pack(padx=10, pady=(0, 10), fill="x")

    def show_warranty_status(self, selected_warranty_status):
        customtkinter.CTkLabel(
            self.__frame,
            font=self.__font,
            text="Warranty status:",
            anchor="w",
        ).pack(padx=10, pady=(10, 2), fill="x")
        customtkinter.CTkButton(
            self.__frame,
            font=self.__font,
            text=selected_warranty_status,
            anchor="w",
        ).pack(padx=10, pady=(0, 10), fill="x")

    def show_note(self, selected_warranty_note):
        customtkinter.CTkLabel(
            self.__frame,
            font=self.__font,
            text="Note:",
            anchor="w",
        ).pack(padx=10, pady=(10, 2), fill="x")
        note_box = customtkinter.CTkTextbox(
            self.__frame, font=self.__font, fg_color="#3B8ED0"
        )
        note_box.insert("0.0", selected_warranty_note)
        note_box.pack(padx=10, pady=(0, 10), fill="both", expand=True)
        note_box.configure(state="disable")


class DeletionConfirmPopup(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("")
        self.geometry("390x140")

        customtkinter.CTkLabel(
            self,
            text="Do you reall want to delete this warranty?",
            font=("JetBrains Mono", 16),
            wraplength=400,
        ).pack(padx=10, pady=10)

        self.__confirm_button = customtkinter.CTkButton(
            self, text="confirm", command=self.__confirm
        )
        self.__confirm_button.pack(
            padx=(5, 10), pady=10, fill="x", expand=True, side="right", anchor="s"
        )

        self.__cancel_button = customtkinter.CTkButton(
            self, text="cannel", command=self.__cancel
        )
        self.__cancel_button.pack(
            padx=(10, 5), pady=10, fill="x", expand=True, side="left", anchor="s"
        )

        self.__is_confirmed = False

    def is_confirmed(self):
        return self.__is_confirmed

    def __confirm(self):
        self.__is_confirmed = True
        self.destroy()

    def __cancel(self):
        self.destroy()
