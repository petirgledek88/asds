import requests
import time

def send_message():
    # Token API bot Telegram Anda
    TOKEN = "7157559937:AAHhhKES6Z8Je0HaZ-bknQtUKW1S93N6U0w"
    # ID chat tujuan (numerik)
    CHAT_ID = "6433568846"  # Ganti dengan ID chat numerik yang benar
    # Pesan yang ingin Anda kirim
    message = "Ini adalah pesan otomatis dari bot."

    # URL endpoint untuk mengirim pesan
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    # Parameter yang akan dikirimkan
    params = {"chat_id": CHAT_ID, "text": message}
    # Menggantikan while True dengan kondisi terbatas untuk menghindari infinite loop
    while True:  # Diubah menjadi sebuah loop finit, misalnya mengirim 10 kali
        
        try:
            # Mengirimkan permintaan POST untuk mengirim pesan
            response = requests.post(url, params=params)
            response.raise_for_status()
            print("Pesan telah berhasil dikirim!")
            time.sleep(60)  # Increase sleep time to lower the likelihood of hitting rate limits or getting a KeyboardInterrupt
        except Exception as e:
            print("Gagal mengirim pesan:", e)

if __name__ == "__main__":
    send_message()
