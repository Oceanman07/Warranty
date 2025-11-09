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
