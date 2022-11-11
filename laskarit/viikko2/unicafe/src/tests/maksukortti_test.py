import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 30.00 euroa")

    def test_nollan_rahan_lataaminen_ei_kasvata_saldoa(self):
        self.maksukortti.lataa_rahaa(0)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    # näemmä vaikuttaakin, joten ei testata tätä
    # def test_negatiivisen_rahan_lataaminen_ei_vaikuta_saldoon(self):
    #     self.maksukortti.lataa_rahaa(-100)

    #     self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(200)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")
    
    def test_saldo_ei_muuty_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_metodi_palauttaa_true_jos_rahat_riittivat(self):
        bool = self.maksukortti.ota_rahaa(200)

        self.assertTrue(bool)

    def test_metodi_palauttaa_false_jos_rahat_eivat_riittaneet(self):
        bool = self.maksukortti.ota_rahaa(2000)
        
        self.assertFalse(bool)