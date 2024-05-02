import tkinter as tk
import tkinter.messagebox as tkmessagebox
import base64
import os
import zipfile
import time

help_domain = "https://unblockabl.github.io/Project-Rebearth-Asset-Manager/"

def main():

    print("Project Rebearth Asset Manager")
    print(f"Check '{help_domain}' for more information and help\n")
    print("Not affiliated with Project Rebearth")

    print("This program is a work in progress.\n")

    if not os.path.exists("assets"):
        print(f"\nAssets folder not found. Make sure you are running the executable from the same location as ProjectRebearthgame.exe  -  {help_domain} for instructions.")
        input("Press enter to exit.")
        exit()

    print("Please continue in the pop-up window.")

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Project Rebearth Asset Manager")
    root.geometry("400x200")

    
    def reset_pack():

        if not tkmessagebox.askyesno("Reset Pack", "Are you sure you want to reset the pack?"):
            return
        
        for file in os.listdir("assets"):
            if os.path.isdir(f"assets/{file}"):
                for subfile in os.listdir(f"assets/{file}"):
                    os.remove(f"assets/{file}/{subfile}")
            os.remove(f"assets/{file}")
        
        time.sleep(1)

        try:
            import requests
            code = requests.get(f"{help_domain}/default_pack.txt").text
        except:
            print("Failed to fetch default pack. Please check your internet connection.")
            return

        try:
            decoded_data = base64.b64decode(code)
        except base64.b64decodeError:
            tkmessagebox.showerror("Error", "Invalid base64-encoded data. Please provide a valid ZIP code.")
            raise ValueError("Invalid base64-encoded data. Please provide a valid ZIP code.")
        

        assets_folder = "assets"
        os.makedirs(assets_folder, exist_ok=True)

        try:
            zip_filename = os.path.join(assets_folder, "pack.zip")
            with open(zip_filename, "wb") as f:
                f.write(decoded_data)

            with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
                zip_ref.extractall(assets_folder)

            os.remove(zip_filename)

            print("zip saved and extracted successfully!")
            tkmessagebox.showinfo("Success", "Successfully applied pack!")
        except (IOError, Exception) as e:
            tkmessagebox.showerror("Error", f"Error saving or extracting the ZIP file: {e}")
            raise IOError(f"Error saving or extracting the ZIP file: {e}")
        
    def on_submit():

        code = entry.get("1.0", "end-1c")

        try:
            decoded_data = base64.b64decode(code)
        except base64.b64decodeError:
            tkmessagebox.showerror("Error", "Invalid base64-encoded data. Please provide a valid ZIP code.")
            raise ValueError("Invalid base64-encoded data. Please provide a valid ZIP code.")
        

        assets_folder = "assets"
        os.makedirs(assets_folder, exist_ok=True)

        try:
            zip_filename = os.path.join(assets_folder, "pack.zip")
            with open(zip_filename, "wb") as f:
                f.write(decoded_data)

            with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
                zip_ref.extractall(assets_folder)

            os.remove(zip_filename)

            print("zip saved and extracted successfully!")
            tkmessagebox.showinfo("Success", "Successfully applied pack!")
        except (IOError, Exception) as e:
            tkmessagebox.showerror("Error", f"Error saving or extracting the ZIP file: {e}")
            raise IOError(f"Error saving or extracting the ZIP file: {e}")
        

    label = tk.Label(root, text="Enter the resource pack code below: ")
    label.pack()

    entry = tk.Text(root, height=1, width=20)
    entry.pack()
    submit = tk.Button(root, text="Apply", command=on_submit)
    submit.pack()
    reset = tk.Button(root, text="Reset Pack", command=reset_pack)
    reset.pack()

    padding = tk.Label(root, text="")
    padding.pack()

    help_label = tk.Label(root, text=f"Need help? Check {help_domain}")
    help_label.pack()



    root.mainloop()

if __name__ == "__main__":
    main()



# to build use ``` python -m nuitka file.py ```
# use Note, when using 'tkinter', consider using '--disable-console' option. Otherwise a terminal window will open. However for
# Nuitka-Plugins:options-nanny: debugging, terminal output is the easiest way to see informative traceback and error information, so delay this until your program 
# Nuitka-Plugins:options-nanny: 



# FINAL BUILD:
# python -m nuitka .\main.py --standalone --enable-plugin=tk-inter