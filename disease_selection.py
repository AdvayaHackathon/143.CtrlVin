import tkinter as tk
from tkinter import messagebox, Canvas, Frame
import subprocess
import sys

diseases = {
    "English": [
        ("Cardiologist (Heart Disease)", "Dr. Heart", "1", "101"),
        ("Neurologist (Brain Disorders)", "Dr. Brain", "2", "102"),
        ("Pulmonologist (Asthma)", "Dr. Lungs", "2", "103"),
        ("Hematologist (Blood Cancer)", "Dr. Blood", "3", "104"),
        ("Endocrinologist (Diabetes)", "Dr. Sugar", "3", "105"),
        ("Dermatologist (Skin)", "Dr. Skin", "1", "106"),
        ("Rheumatologist (Arthritis)", "Dr. Joints", "2", "107"),
        ("Ophthalmologist (Eyes)", "Dr. Eyes", "1", "108"),
        ("Psychiatrist (Mental Health)", "Dr. Mind", "3", "109"),
        ("Gynecologist (Women Health)", "Dr. Women", "2", "110"),
    ],
    "Hindi": [
        ("हृदय रोग विशेषज्ञ", "डॉ. दिल", "1", "101"),
        ("न्यूरोलॉजिस्ट (मस्तिष्क विकार)", "डॉ. ब्रेन", "2", "102"),
        ("फेफड़ों के रोग विशेषज्ञ (दमा)", "डॉ. लंग्स", "2", "103"),
        ("हीमाटोलॉजिस्ट (ब्लड कैंसर)", "डॉ. ब्लड", "3", "104"),
        ("एंडोक्राइनोलॉजिस्ट (मधुमेह)", "डॉ. शुगर", "3", "105"),
        ("त्वचा रोग विशेषज्ञ", "डॉ. स्किन", "1", "106"),
        ("रूमेटोलॉजिस्ट (गठिया)", "डॉ. जॉइंट्स", "2", "107"),
        ("नेत्र रोग विशेषज्ञ", "डॉ. आंखें", "1", "108"),
        ("मनोचिकित्सक", "डॉ. माइंड", "3", "109"),
        ("स्त्री रोग विशेषज्ञ", "डॉ. वुमन", "2", "110"),
    ],
    "Kannada": [
        ("ಹೃದಯರೋಗ ತಜ್ಞ", "ಡಾ. ಹಾರ್ಟ್", "1", "101"),
        ("ನರವೈದ್ಯ (ಮೆದುಳಿನ ರೋಗ)", "ಡಾ. ಬ್ರೈನ್", "2", "102"),
        ("ಶ್ವಾಸಕೋಶ ತಜ್ಞ (ಆಸ್ತಮಾ)", "ಡಾ. ಲಂಗ್ಸ್", "2", "103"),
        ("ರಕ್ತದ ಕ್ಯಾನ್ಸರ್ ತಜ್ಞ", "ಡಾ. ಬ್ಲಡ್", "3", "104"),
        ("ಅಂತರಸ್ರಾವಿ ತಜ್ಞ (ಮಧುಮೇಹ)", "ಡಾ. ಶುಗರ್", "3", "105"),
        ("ಚರ್ಮ ತಜ್ಞ", "ಡಾ. ಸ್ಕಿನ್", "1", "106"),
        ("ಜೋಡಣಾ ತಜ್ಞ (ಆರ್ಥರೈಟಿಸ್)", "ಡಾ. ಜಾಯಿಂಟ್ಸ್", "2", "107"),
        ("ಕಣ್ಣು ತಜ್ಞ", "ಡಾ. ಐಸ್", "1", "108"),
        ("ಮಾನಸಿಕ ತಜ್ಞ", "ಡಾ. ಮೈಂಡ್", "3", "109"),
        ("ಸ್ತ್ರೀಯರ ತಜ್ಞ", "ಡಾ. ವುಮನ್", "2", "110"),
    ]
}

class DiseaseSelectionApp:
    def __init__(self, root, language, patient_name, phone_number):
        self.root = root
        self.root.title("Disease Selection")
        self.root.geometry("450x500")
        self.root.configure(bg="#fff8e1")

        self.language = language
        self.patient_name = patient_name
        self.phone_number = phone_number

        title_text = {
            "English": "Select Your Disease",
            "Hindi": "अपनी बीमारी चुनें",
            "Kannada": "ನಿಮ್ಮ ರೋಗವನ್ನು ಆಯ್ಕೆಮಾಡಿ"
        }

        tk.Label(root, text=title_text[language], font=("Arial", 16, "bold"), bg="#fff8e1", fg="#bf360c").pack(pady=10)

        # === Scrollable Frame ===
        canvas = Canvas(root, bg="#fff8e1", borderwidth=0, highlightthickness=0, height=400)
        frame = Frame(canvas, bg="#fff8e1")
        scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        for disease, doctor, floor, room in diseases[language]:
            btn = tk.Button(frame, text=disease, font=("Arial", 12), width=40, bg="#aed581", fg="black",
                            command=lambda d=disease, doc=doctor, f=floor, r=room: self.proceed_to_payment(d, doc, f, r))
            btn.pack(pady=6)

    def proceed_to_payment(self, disease, doctor_name, floor, room):
        self.root.destroy()
        subprocess.run([
            "python", "payment_screen.py",
            self.patient_name,
            self.phone_number,
            doctor_name,
            floor,
            room
        ])

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python disease_selection.py <Language> <PatientName> <PhoneNumber>")
        sys.exit(1)

    lang = sys.argv[1]
    patient_name = sys.argv[2]
    phone_number = sys.argv[3]

    root = tk.Tk()
    app = DiseaseSelectionApp(root, lang, patient_name, phone_number)
    root.mainloop()
