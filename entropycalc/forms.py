from django import forms
from .models import PerkaraYudisial

class PerkaraForm(forms.ModelForm):
    class Meta:
        model = PerkaraYudisial
        fields = [
            'nomor_perkara', 'judul_kasus', 'jenis_perkara',
            'l1_fakta_dasar', 'l5_keraguan_pengujian', 'l6_konsistensi_logika',
            'l7_validasi_metode', 'l11_konklusi_putusan', 'l12_keadilan_sosial',
            'catatan_analisis'
        ]
        widgets = {
            'catatan_analisis': forms.Textarea(attrs={'rows': 3}),
        }