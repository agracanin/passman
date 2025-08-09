import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog

APP_TITLE = "Passman"

class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(APP_TITLE)

        # --- State placeholders (real Vault comes later) ---
        self.vault_open = False  # when True, buttons enable

        # UI
        self._build_menu()
        self._build_table()
        self._build_buttons()
        self._update_controls()

    # ---------- UI builders ----------
    def _build_menu(self):
        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Vault...", command=self._new_vault)
        filemenu.add_command(label="Open Vault...", command=self._open_vault)
        filemenu.add_separator()
        filemenu.add_command(label="Save", command=self._save_vault)
        filemenu.add_command(label="Lock", command=self._lock_vault)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)

        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

    def _build_table(self):
        self.tree = ttk.Treeview(
            self.root,
            columns=("title", "url", "username", "updated"),
            show="headings",
            height=15
        )
        self.tree.heading("title", text="Title")
        self.tree.heading("url", text="URL")
        self.tree.heading("username", text="Username")
        self.tree.heading("updated", text="Updated")

        self.tree.column("title", width=220)
        self.tree.column("url", width=260)
        self.tree.column("username", width=160)
        self.tree.column("updated", width=140)

        self.tree.pack(fill="both", expand=True, padx=8, pady=(8, 4))

    def _build_buttons(self):
        bar = ttk.Frame(self.root)
        bar.pack(fill="x", padx=8, pady=(0, 8))

        self.btn_add = ttk.Button(bar, text="Add", command=self._add_entry)
        self.btn_edit = ttk.Button(bar, text="Edit", command=self._edit_entry)
        self.btn_delete = ttk.Button(bar, text="Delete", command=self._delete_entry)

        self.btn_add.pack(side="left")
        self.btn_edit.pack(side="left", padx=6)
        self.btn_delete.pack(side="left")

    # ---------- Placeholder actions (no real logic yet) ----------
    def _new_vault(self):
        path = filedialog.asksaveasfilename(
            title="Create Vault",
            defaultextension=".ppmx",
            filetypes=[("Passman Vault", "*.ppmx"), ("All Files", "*.*")]
        )
        if not path:
            return
        pw = simpledialog.askstring("Master Password", "Create master password:", show="*")
        if not pw:
            messagebox.showwarning("Cancelled", "No password entered.")
            return
        # Pretend we created it successfully
        self.vault_open = True
        self._update_controls()
        messagebox.showinfo("Vault", f"(placeholder) New vault at:\n{path}")

    def _open_vault(self):
        path = filedialog.askopenfilename(
            title="Open Vault",
            filetypes=[("Passman Vault", "*.ppmx"), ("All Files", "*.*")]
        )
        if not path:
            return
        pw = simpledialog.askstring("Master Password", "Enter master password:", show="*")
        if pw is None:
            return
        # Pretend we opened it successfully
        self.vault_open = True
        self._update_controls()
        messagebox.showinfo("Vault", f"(placeholder) Opened:\n{path}")

    def _save_vault(self):
        if not self.vault_open:
            messagebox.showwarning("Locked", "Open a vault first.")
            return
        messagebox.showinfo("Save", "(placeholder) Saved vault.")

    def _lock_vault(self):
        self.vault_open = False
        self._update_controls()
        messagebox.showinfo("Locked", "Vault locked (placeholder).")

    def _add_entry(self):
        if not self.vault_open:
            messagebox.showwarning("Locked", "Open a vault first.")
            return
        messagebox.showinfo("Add", "(placeholder) Add entry dialog will appear here.")

    def _edit_entry(self):
        if not self.vault_open:
            messagebox.showwarning("Locked", "Open a vault first.")
            return
        messagebox.showinfo("Edit", "(placeholder) Edit selected entry.")

    def _delete_entry(self):
        if not self.vault_open:
            messagebox.showwarning("Locked", "Open a vault first.")
            return
        messagebox.showinfo("Delete", "(placeholder) Delete selected entry.")

    # ---------- Helpers ----------
    def _update_controls(self):
        state = ("normal" if self.vault_open else "disabled")
        for btn in (self.btn_add, self.btn_edit, self.btn_delete):
            btn.config(state=state)

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
