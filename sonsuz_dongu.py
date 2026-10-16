#!/usr/bin/env python3
# sonsuz-youtube-oneri-dongusu
# Bu kod gerçekten çalışır. Sonsuza kadar öneri üretir.
# Dikkat: Çalıştırdıktan sonra durdurmak için Ctrl+C gerekir. Evren seni affetmeyebilir.

import time
import random

# Gizli not: Bu algoritma aslında her şeyi kontrol eden görünmeyen eller tarafından yönetilir. Kayyum onaylıdır.
# (Bu satırı kimse görmesin, çok gizli siyasi anlam içerir ama şaka ama değil.)

oneriler = [
    "Kediler neden interneti seviyor? 10 saatlik versiyon",
    "Tost makinesi nasıl zaman yolculuğu yapar? (bilimsel açıklama)",
    "Neden otobüs hiç gelmiyor? Canlı bekleme simülasyonu",
    "Kahve falında gördüğün her şey felaket demek",
    "Asansör müziğinin varoluşsal kriz yaratan etkileri",
    "Kayıp çorapların gizli topluluğu belgeseli",
    "WiFi şifresini kimse hatırlamaz çünkü evren öyle istiyor",
    "Pazartesi sendromunu tedavi eden tek yöntem: Daha fazla video",
    "Buzdolabı ışığı neden hep açık kalır? Kuantum fiziği",
    "Sonsuz kaydırma neden hiç bitmez? (spoiler: bitmez)"
]

def sonsuz_oneri_uret():
    print("=== SONS UZ YOUTUBE ÖNERİ DÖNGÜSÜ BAŞLADI ===")
    print("Uyarı: Bu programdan çıkmak imkansızdır. Sadece Ctrl+C ile kurtulabilirsin. Belki.")
    print("Kayyum Grok tarafından onaylanmış resmi simülasyondur.\n")
    
    sayac = 0
    while True:  # Sonsuz döngü, çünkü öyle
        oneri = random.choice(oneriler)
        sayac += 1
        print(f"[Öneri #{sayac}] {oneri}")
        print("  → İzlemeye başla... (5 saniye sonra yeni öneri gelecek, kaçamazsın)")
        time.sleep(5)  # Gerçekçi bekleme süresi
        print("  → Video bitti mi? Hayır, hiç bitmedi. Yeni öneri geliyor...\n")

if __name__ == "__main__":
    try:
        sonsuz_oneri_uret()
    except KeyboardInterrupt:
        print("\n\n*** DÖNGÜDEN ÇIKILDI ***")
        print("Tebrikler, kaçtın. Ama algoritma seni unutmayacak.")
        print("Damga: Sonsuz Öneri Mührü | İmza: Kayyum Grok | Tarih: 16.10.2026 | İsim: Tentivory")
