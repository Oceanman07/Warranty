import customtkinter

from .frame import AllWarrentiesFrame


class DetailWarrantyPopop(customtkinter.CTkToplevel):
    def __init__(self, master, all_warrenties_frame: AllWarrentiesFrame, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Detail")
        self.geometry("800x600")

        self.__all_warrenties_frame = all_warrenties_frame
        self.__font = customtkinter.CTkFont(family="JetBrains Mono", size=19)

        self.__frame = customtkinter.CTkFrame(self)
        self.__frame.pack(padx=5, pady=5, fill="both", expand=True)

        customtkinter.CTkLabel(
            self.__frame,
            font=self.__font,
            text="Full name:",
            anchor="w",
        ).pack(padx=10, pady=(10, 2), fill="x")
        customtkinter.CTkButton(
            self.__frame,
            font=self.__font,
            text=self.__all_warrenties_frame.selected_warranty_name,
            anchor="w",
        ).pack(padx=10, pady=(0, 10), fill="x")

        customtkinter.CTkLabel(
            self.__frame,
            font=self.__font,
            text="Phone number:",
            anchor="w",
        ).pack(padx=10, pady=(10, 2), fill="x")
        customtkinter.CTkButton(
            self.__frame,
            font=self.__font,
            text=self.__all_warrenties_frame.selected_warranty_phone_number,
            anchor="w",
        ).pack(padx=10, pady=(0, 10), fill="x")

        customtkinter.CTkLabel(
            self.__frame,
            font=self.__font,
            text="Expired date:",
            anchor="w",
        ).pack(padx=10, pady=(10, 2), fill="x")
        customtkinter.CTkButton(
            self.__frame,
            font=self.__font,
            text=self.__all_warrenties_frame.selected_warranty_expired_datetime,
            anchor="w",
        ).pack(padx=10, pady=(0, 10), fill="x")

        customtkinter.CTkLabel(
            self.__frame,
            font=self.__font,
            text="Warranty status:",
            anchor="w",
        ).pack(padx=10, pady=(10, 2), fill="x")
        customtkinter.CTkButton(
            self.__frame,
            font=self.__font,
            text=self.__all_warrenties_frame.selected_warranty_status,
            anchor="w",
        ).pack(padx=10, pady=(0, 10), fill="x")

        customtkinter.CTkLabel(
            self.__frame,
            font=self.__font,
            text="Note:",
            anchor="w",
        ).pack(padx=10, pady=(10, 2), fill="x")
        note_box = customtkinter.CTkTextbox(
            self.__frame, font=self.__font, fg_color="#3B8ED0"
        )
        note_box.insert("0.0", self.__all_warrenties_frame.selected_warranty_note)
        note_box.pack(padx=10, pady=(0, 10), fill="both", expand=True)
        note_box.configure(state="disable")
