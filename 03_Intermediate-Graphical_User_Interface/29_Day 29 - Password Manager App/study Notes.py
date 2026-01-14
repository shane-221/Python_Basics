from tkinter import messagebox

messagebox.showinfo(title=" Tile of the box", message="Message you want")

is_ok = messagebox.askokcancel(title=website_value,
                               message=f"""
                       These are the details entered:
                        Email:{email_value}
                        Password : {password_value}
                        Is it okay to save?     
                            """)
