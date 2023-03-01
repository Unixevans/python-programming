import pywhatkit
import time

def send_whatsapp_message(message, phone_number, hour, minute):
    # Menghitung waktu untuk pengiriman pesan
    now = time.localtime()
    year, month, day = now.tm_year, now.tm_mon, now.tm_mday
    send_time = (year, month, day, hour, minute, 0, 0, 0, -1)

    # Mengirim pesan WhatsApp ke nomor telepon
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)

    # Menunggu pengiriman pesan selesai
    while True:
        if time.localtime() >= send_time:
            break
        time.sleep(1)

# Silahkan ganti nomor wa, pesan, dan waktu sesuai kebutuhan di bawah ini!
send_whatsapp_message("Tes", "+6285646042925", 11, 28)

