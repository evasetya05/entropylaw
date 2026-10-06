from django.test import TestCase

from django.urls import reverse

from .models import PerkaraYudisial


class PerkaraViewsTests(TestCase):
    def test_daftar_perkara_renders(self):
        response = self.client.get(reverse('daftar_perkara'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'entropycalc/index.html')

    def test_create_and_view_perkara(self):
        response = self.client.post(
            reverse('kalkulasi_baru'),
            {
                'nomor_perkara': 'TEST-001',
                'judul_kasus': 'Uji perkara',
                'jenis_perkara': 'PIDANA',
                'l1_fakta_dasar': 5,
                'l5_keraguan_pengujian': 1,
                'l6_konsistensi_logika': 1,
                'l7_validasi_metode': 2,
                'l11_konklusi_putusan': 4,
                'l12_keadilan_sosial': 3,
                'catatan_analisis': '',
            },
        )

        perkara = PerkaraYudisial.objects.get(nomor_perkara='TEST-001')
        self.assertRedirects(
            response,
            reverse('detail_perkara', kwargs={'pk': perkara.pk}),
        )

        detail = self.client.get(
            reverse('detail_perkara', kwargs={'pk': perkara.pk})
        )
        self.assertEqual(detail.status_code, 200)
        self.assertTemplateUsed(detail, 'entropycalc/entropycalc.html')
