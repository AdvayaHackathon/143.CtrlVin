import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import threading
import time

# ==== SEND SMS FUNCTION ====
def send_sms(phone_number, patient_name, doctor_name, floor, room):
    url = "https://www.fast2sms.com/dev/bulkV2"
    headers = {
        'authorization': 'YOUR_FAST2SMS_API_KEY',  # Replace with your actual API key
        'Content-Type': "application/x-www-form-urlencoded"
    }

    message = f"Hello {patient_name}, your payment is successful. Please visit {doctor_name}, Floor: {floor}, Room: {room}. - CTRL+V IN Hospital"

    payload = {
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'v3',
        'numbers': phone_number
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        print("SMS Sent:", response.text)
    except Exception as e:
        print("SMS sending failed:", e)

# ==== PAYMENT SCREEN FUNCTION ====
def payment_screen(patient_name, phone_number, doctor_name, floor_number, room_number):
    root = tk.Tk()
    root.title("Payment Portal")
    root.geometry("400x500")
    root.configure(bg="#f0fff0")

    tk.Label(root, text="Scan to Pay", font=("Arial", 18, "bold"), bg="#f0fff0").pack(pady=10)

    # Load QR Code Image
    try:
        qr_img = Image.open("upi_qr.png")
        qr_img = qr_img.resize((200, 200))
        qr_photo = ImageTk.PhotoImage(qr_img)
        qr_label = tk.Label(root, image=qr_photo, bg="#f0fff0")
        qr_label.image = qr_photo  # Prevent garbage collection
        qr_label.pack(pady=10)
    except:
        tk.Label(root, text="[QR Image Missing]", font=("Arial", 12), fg="red", bg="#f0fff0").pack()

    tk.Label(root, text="UPI ID: 7795428138@ybl", font=("Arial", 14), bg="#f0fff0").pack(pady=5)

    status_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", bg="#f0fff0")
    status_label.pack(pady=10)

    def background_process():
        status_label.config(text="⏳ Analyzing payment...")
        time.sleep(3)  # Simulate delay
        send_sms(phone_number, patient_name, doctor_name, floor_number, room_number)
        status_label.config(text="✅ Payment Successful!", fg="green")
        messagebox.showinfo("Payment", "Payment confirmed. SMS sent!")
        root.destroy()

    def confirm_payment():
        threading.Thread(target=background_process).start()

    tk.Button(root, text="Payment Done", font=("Arial", 14), bg="green", fg="white", command=confirm_payment).pack(pady=30)

    root.mainloop()

# ==== TEST CALL ====
if __name__ == "__main__":
    payment_screen(
        patient_name="John Doe",
        phone_number="9876543210",
        doctor_name="Dr. Arjun Rao",
        floor_number="3",
        room_number="305"
    )
