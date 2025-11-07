import os

import customtkinter


class ContentFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class FunctionsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add_new_button = customtkinter.CTkButton(self, text="New")
        self.add_new_button.pack(padx=10, pady=(15, 10))

        self.change_appr_mode_button = customtkinter.CTkButton(
            master, text="Light", command=self.change_appearance_mode
        )
        self.change_appr_mode_button.pack(
            padx=10, pady=(0, 10), side="bottom", fill="x"
        )

    def change_appearance_mode(self):
        if customtkinter.get_appearance_mode() == "Light":
            customtkinter.set_appearance_mode("dark")
            self.change_appr_mode_button.configure(text="Dark")
        else:
            customtkinter.set_appearance_mode("light")
            self.change_appr_mode_button.configure(text="Light")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("light")
        self.title("Warranty")
        self.geometry("1300x700")

        self.content_frame = ContentFrame(self)
        self.content_frame.pack(
            padx=(5, 10), pady=10, side="right", fill="both", expand=True
        )

        self.functions_frame = FunctionsFrame(self, width=220)
        self.functions_frame.pack(padx=10, pady=10, side="left", fill="y")


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
