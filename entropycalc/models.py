from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class PerkaraYudisial(models.Model):
    JENIS_PILIHAN = [
        ('PIDANA', 'Pidana'),
        ('PERDATA', 'Perdata'),
        ('NARKOTIKA', 'Narkotika / FILM-Rehabilitasi'),
    ]

    nomor_perkara = models.CharField(max_length=100, unique=True)
    judul_kasus = models.CharField(max_length=255)
    jenis_perkara = models.CharField(max_length=20, choices=JENIS_PILIHAN, default='PIDANA')
    
    # 12 Level Parameter (Skala 1 - 10)
    l1_fakta_dasar = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    l5_keraguan_pengujian = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    l6_konsistensi_logika = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    l7_validasi_metode = models.FloatField(default=1, validators=[MinValueValidator(0.1), MaxValueValidator(10)])
    l11_konklusi_putusan = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    l12_keadilan_sosial = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    nilai_e = models.FloatField(blank=True, null=True)
    zona = models.CharField(max_length=50, blank=True)
    catatan_analisis = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def hitung_entropi(self):
        # Postulat Khusus: Fakta dasar cacat/nol -> perkara gugur
        if self.l1_fakta_dasar <= 0:
            self.nilai_e = -999.0
            self.zona = "Zona Kolaps (Fakta Dasar Cacat / L1=0)"
            return

        # Formula Entropi Yudisial Utama
        pembilang = (self.l11_konklusi_putusan + self.l12_keadilan_sosial - 
                     self.l1_fakta_dasar - self.l5_keraguan_pengujian - self.l6_konsistensi_logika)
        penyebut = self.l7_validasi_metode if self.l7_validasi_metode > 0 else 1.0

        self.nilai_e = round(pembilang / penyebut, 2)

        if self.nilai_e >= 1.0:
            self.zona = "Zona Kokoh (Pembuktian Solid)"
        elif 0 <= self.nilai_e < 1.0:
            self.zona = "Zona Ambang (Perlu Verifikasi Bukti Tambahan)"
        else:
            self.zona = "Zona Kolaps (Tuntutan/Putusan Gugur)"

    def save(self, *args, **kwargs):
        self.hitung_entropi()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nomor_perkara} - {self.judul_kasus} ({self.zona})"