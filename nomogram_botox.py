import tkinter as tk
from tkinter import ttk

def compute():
    sexe_value = 1 if sexe_btn.get() == "Femme" else 0
    diabete_value = 1 if diabete_btn.get() == "Diabètique" else 0
    ov_det_value = 1 if ov_det_btn.get() == "Oui" else 0
    symp_value = 1 if symp_btn.get() == "Humide" else 0

    res = -0.2431204539553814 * sexe_value + \
          0.9898193766135761 + \
          -0.12734979639174865 * diabete_value + \
          -0.21940517665289216 * ov_det_value + \
          -0.1953706283498568 * symp_value + \
          0.0006395439167624947 * b1_in.get() + \
          -0.0008242434643266894 * capa_in.get() + \
          -0.010512335092309378 * qmax_in.get() + \
          -0.0016951372255243201 * pdet_max_in.get() + \
          -0.000541836580145543 * rpm_in.get()

    res = max(min(res, 1), 0)
    result_label.config(text="Taux de succès estimé: {:.2f} %".format((1 - res) * 100))

# GUI setup
root = tk.Tk()
root.title("Estimation Tool")
root.geometry("400x400")  # Set initial window size

style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12), foreground="white", background="#3498db")  # Set button color

# Add padding and styling
padding_y = 5
padding_x = 10

sexe_btn = tk.StringVar()
sexe_btn.set("Homme")
sexe_label = ttk.Label(root, text="Sexe")
sexe_label.grid(row=0, column=0, pady=padding_y, padx=padding_x)
sexe_radiobutton1 = ttk.Radiobutton(root, text="Homme", variable=sexe_btn, value="Homme")
sexe_radiobutton2 = ttk.Radiobutton(root, text="Femme", variable=sexe_btn, value="Femme")
sexe_radiobutton1.grid(row=0, column=1, pady=padding_y)
sexe_radiobutton2.grid(row=0, column=2, pady=padding_y)

diabete_btn = tk.StringVar()
diabete_btn.set("Non diabètique")
diabete_label = ttk.Label(root, text="Diabète")
diabete_label.grid(row=1, column=0, pady=padding_y, padx=padding_x)
diabete_radiobutton1 = ttk.Radiobutton(root, text="Non diabètique", variable=diabete_btn, value="Non diabètique")
diabete_radiobutton2 = ttk.Radiobutton(root, text="Diabètique", variable=diabete_btn, value="Diabètique")
diabete_radiobutton1.grid(row=1, column=1, pady=padding_y)
diabete_radiobutton2.grid(row=1, column=2, pady=padding_y)

ov_det_btn = tk.StringVar()
ov_det_btn.set("Non")
ov_det_label = ttk.Label(root, text="Hyperactivité Det.")
ov_det_label.grid(row=2, column=0, pady=padding_y, padx=padding_x)
ov_det_radiobutton1 = ttk.Radiobutton(root, text="Non", variable=ov_det_btn, value="Non")
ov_det_radiobutton2 = ttk.Radiobutton(root, text="Oui", variable=ov_det_btn, value="Oui")
ov_det_radiobutton1.grid(row=2, column=1, pady=padding_y)
ov_det_radiobutton2.grid(row=2, column=2, pady=padding_y)

symp_btn = tk.StringVar()
symp_btn.set("Sec")
symp_label = ttk.Label(root, text="1er Symptome")
symp_label.grid(row=3, column=0, pady=padding_y, padx=padding_x)
symp_radiobutton1 = ttk.Radiobutton(root, text="Sec", variable=symp_btn, value="Sec")
symp_radiobutton2 = ttk.Radiobutton(root, text="Humide", variable=symp_btn, value="Humide")
symp_radiobutton1.grid(row=3, column=1, pady=padding_y)
symp_radiobutton2.grid(row=3, column=2, pady=padding_y)

b1_in = tk.IntVar()
b1_label = ttk.Label(root, text="B1")
b1_label.grid(row=4, column=0, pady=padding_y, padx=padding_x)
b1_entry = ttk.Entry(root, textvariable=b1_in)
b1_entry.grid(row=4, column=1, pady=padding_y)

capa_in = tk.IntVar()
capa_label = ttk.Label(root, text="Capacité vésicale")
capa_label.grid(row=5, column=0, pady=padding_y, padx=padding_x)
capa_entry = ttk.Entry(root, textvariable=capa_in)
capa_entry.grid(row=5, column=1, pady=padding_y)

qmax_in = tk.IntVar()
qmax_label = ttk.Label(root, text="Qmax")
qmax_label.grid(row=6, column=0, pady=padding_y, padx=padding_x)
qmax_entry = ttk.Entry(root, textvariable=qmax_in)
qmax_entry.grid(row=6, column=1, pady=padding_y)

pdet_max_in = tk.IntVar()
pdet_max_label = ttk.Label(root, text="Pression det. max")
pdet_max_label.grid(row=7, column=0, pady=padding_y, padx=padding_x)
pdet_max_entry = ttk.Entry(root, textvariable=pdet_max_in)
pdet_max_entry.grid(row=7, column=1, pady=padding_y)

rpm_in = tk.IntVar()
rpm_label = ttk.Label(root, text="RPM")
rpm_label.grid(row=8, column=0, pady=padding_y, padx=padding_x)
rpm_entry = ttk.Entry(root, textvariable=rpm_in)
rpm_entry.grid(row=8, column=1, pady=padding_y)

compute_button = ttk.Button(root, text="Calculer", command=compute)
compute_button.grid(row=9, column=0, columnspan=3, pady=padding_y)

result_label = ttk.Label(root, text="Taux de succès estimé: ")
result_label.grid(row=10, column=0, columnspan=3, pady=padding_y)

root.mainloop()
