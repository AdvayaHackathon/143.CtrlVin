import tkinter as tk
from tkinter import ttk
import subprocess

# Simulated patient data from previous screen
patient_data = {
    "name": "Ravi Kumar",
    "phone": "9876543210",
    "location": "Bangalore",
    "age": "30",
    "language": "English"
}

def disease_selection_screen():
    root = tk.Tk()
    root.title("Disease Selection")
    root.geometry("600x600")
    root.configure(bg="lightgreen")

    selected_language = patient_data["language"]

    tk.Label(root, text="Select Your Disease", font=("Arial", 16, "bold"), bg="lightgreen").pack(pady=15)

    disease_data = {
        "Headache": {
            "English": {"Doctor": "Dr. A. Kumar", "Room": "101", "Floor": "1st"},
            "Hindi": {"Doctor": "डॉ. ए. कुमार", "Room": "१०१", "Floor": "पहली मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಎ. ಕುಮಾರ್", "Room": "೧೦೧", "Floor": "ಮೊದಲ ಮಹಡಿ"},
        },
        # (Other diseases remain unchanged...)
        "Gynecologist (Women’s Health)": {
            "English": {"Doctor": "Dr. Swathi Desai", "Room": "410", "Floor": "4th"},
            "Hindi": {"Doctor": "डॉ. स्वाति देसाई", "Room": "४१०", "Floor": "चौथी मंज़िल"},
            "Kannada": {"Doctor": "ಡಾ. ಸ್ವಾತಿ ದೇಸಾಯಿ", "Room": "೪೧೦", "Floor": "ನಾಲ್ಕನೇ ಮಹಡಿ"},
        }
    }

    selected_disease = tk.StringVar()
    selected_disease.set("Select Disease")

    def on_disease_selected(*args):
        disease = selected_disease.get()
        if disease in disease_data:
            info = disease_data[disease][selected_language]
            doctor_label.config(text=f"Doctor: {info['Doctor']}")
            floor_label.config(text=f"Floor: {info['Floor']}")
            room_label.config(text=f"Room No: {info['Room']}")
            next_button.config(state="normal")
        else:
            doctor_label.config(text="")
            floor_label.config(text="")
            room_label.config(text="")
            next_button.config(state="disabled")

    disease_options = list(disease_data.keys())
    drop = ttk.Combobox(root, textvariable=selected_disease, values=disease_options, font=("Arial", 12), state="readonly", width=50)
    drop.pack(pady=10)
    drop.bind("<<ComboboxSelected>>", on_disease_selected)

    doctor_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="lightgreen")
    doctor_label.pack(pady=5)

    floor_label = tk.Label(root, text="", font=("Arial", 12), bg="lightgreen")
    floor_label.pack(pady=5)

    room_label = tk.Label(root, text="", font=("Arial", 12), bg="lightgreen")
    room_label.pack(pady=5)

    def go_to_payment():
        disease = selected_disease.get()
        info = disease_data[disease][selected_language]
        args = [
            "python", "payment_screen.py",
            patient_data["name"],
            patient_data["phone"],
            patient_data["location"],
            patient_data["age"],
            disease,
            info["Doctor"],
            info["Room"],
            info["Floor"],
            "₹300",
            selected_language
        ]
        root.destroy()
        subprocess.Popen(args)

    next_button = tk.Button(root, text="Next", font=("Arial", 12, "bold"), bg="orange", fg="white", command=go_to_payment, state="disabled")
    next_button.pack(pady=20)

    # Back Button
    back_button = tk.Button(root, text="Back", font=("Arial", 12, "bold"), bg="gray", fg="white", command=root.destroy)
    back_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    disease_selection_screen()
