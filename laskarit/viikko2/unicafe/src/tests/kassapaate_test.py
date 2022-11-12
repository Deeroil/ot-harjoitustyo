import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
  def setUp(self):
    self.kassapaate = Kassapaate()

  def test_vasta_luodun_kassapaatteen_rahat_oikein(self):
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

  def test_vasta_luodun_kassapaatteen_lounaat_oikein(self):
    self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

# vaihtoraha käteisellä riittävillä rahoilla
  def test_edullisen_kateisosto_riittavilla_rahoilla_antaa_oikean_vaihtorahan(self):
    vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(340)
    self.assertEqual(vaihtoraha, 100)

  def test_maukkaan_kateisosto_riittavilla_rahoilla_antaa_oikean_vaihtorahan(self):
    vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
    self.assertEqual(vaihtoraha, 100)

#tasaraha kasvattaa tasan hinnan verran kassarahaa
  def test_maukkaan_kateisosto_tasarahalla_kasvattaa_rahamaaraa_oikein(self):
    self.kassapaate.syo_edullisesti_kateisella(240)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

  def test_maukkaan_kateisosto_tasarahalla_kasvattaa_rahamaaraa_oikein(self):
    self.kassapaate.syo_maukkaasti_kateisella(400)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

#iso maksuraha nostaa kassarahoja oikein 
  def test_edullisen_kateisosto_isolla_rahamaaralla_kasvattaa_rahamaaraa_oikein(self):
    self.kassapaate.syo_edullisesti_kateisella(5000)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

  def test_maukkaan_kateisosto_isolla_rahamaaralla_kasvattaa_rahamaaraa_oikein(self):
    self.kassapaate.syo_maukkaasti_kateisella(5000)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

# riittävä maksu nostaa lounaiden määrää
  def test_riittava_maksu_nostaa_edullisten_maaraa(self):
    self.kassapaate.syo_edullisesti_kateisella(240)
    self.assertEqual(self.kassapaate.edulliset, 1)

  def test_riittava_maksu_nostaa_maukkaiden_maaraa(self):
    self.kassapaate.syo_maukkaasti_kateisella(400)
    self.assertEqual(self.kassapaate.maukkaat, 1)

# ei-riittävä maksu ei vaikuta
  def test_edullisen_maksu_ei_riittava_niin_rahamaara_ei_muutu(self):
    self.kassapaate.syo_edullisesti_kateisella(200)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

  def test_edullisen_maksu_ei_riittava_niin_rahamaara_ei_muutu(self):
    self.kassapaate.syo_edullisesti_kateisella(200)
    self.assertEqual(self.kassapaate.edulliset, 0)

  def test_maukkaan_maksu_ei_riittava_niin_rahamaara_ei_muutu(self):
    self.kassapaate.syo_maukkaasti_kateisella(200)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

  def test_maukkaan_maksu_ei_riittava_niin_rahamaara_ei_muutu(self):
    self.kassapaate.syo_maukkaasti_kateisella(200)
    self.assertEqual(self.kassapaate.edulliset, 0)

  # myös maksukortilla
  # edullinen tarpeeksi rahaa
  def test_kortilla_tarpeeksi_rahaa_veloitus_toimii_edullinen_palauttaa_true(self):
    maksukortti = Maksukortti(1000)
    bool = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
    self.assertEqual(bool, True)

  def test_kortilla_tarpeeksi_rahaa_veloitus_toimii_edullinen_vahentaa_kortilta(self):
    maksukortti = Maksukortti(1000)
    self.kassapaate.syo_edullisesti_kortilla(maksukortti)
    self.assertEqual(maksukortti.saldo, 760)

  # edullinen ei tarpeeksi rahaa, veloitus ei toimi
  def test_kortilla_ei_tarpeeksi_rahaa_maukas_palauttaa_false(self):
    maksukortti = Maksukortti(10)
    bool = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
    self.assertEqual(bool, False)

  def test_kortilla_ei_tarpeeksi_rahaa_maukas_ei_vahenna_kortilta(self):
    maksukortti = Maksukortti(10)
    self.kassapaate.syo_edullisesti_kortilla(maksukortti)
    self.assertEqual(maksukortti.saldo, 10)

  # maukas tarpeeksi rahaa, veloitus toimii
  def test_kortilla_tarpeeksi_rahaa_veloitus_toimii_maukas_palauttaa_true(self):
    maksukortti = Maksukortti(1000)
    bool = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
    self.assertEqual(bool, True)

  def test_kortilla_tarpeeksi_rahaa_veloitus_toimii_maukas_vahentaa_kortilta(self):
    maksukortti = Maksukortti(1000)
    self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
    self.assertEqual(maksukortti.saldo, 600)

  # maukas ei tarpeeksi rahaa, veloitus ei toimi
  def test_kortilla_ei_tarpeeksi_rahaa_maukas_palauttaa_false(self):
    maksukortti = Maksukortti(10)
    bool = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
    self.assertEqual(bool, False)

  def test_kortilla_ei_tarpeeksi_rahaa_maukas_ei_vahenna_kortilta(self):
    maksukortti = Maksukortti(10)
    self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
    self.assertEqual(maksukortti.saldo, 10)

  # tarpeeksi rahaa, lounaat kasvaa
  def test_kortilla_tarpeeksi_rahaa_edullinen_lkm_kasvaa(self):
    maksukortti = Maksukortti(1000)
    self.kassapaate.syo_edullisesti_kortilla(maksukortti)
    self.assertEqual(self.kassapaate.edulliset, 1)

  def test_kortilla_tarpeeksi_rahaa_maukas_lkm_kasvaa(self):
    maksukortti = Maksukortti(1000)
    self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
    self.assertEqual(self.kassapaate.maukkaat, 1)
  
  # ei tarpeeksi rahaa, lounas lkm ei kasva
  def test_kortilla_tarpeeksi_rahaa_edullinen_lkm_kasvaa(self):
    maksukortti = Maksukortti(10)
    self.kassapaate.syo_edullisesti_kortilla(maksukortti)
    self.assertEqual(self.kassapaate.edulliset, 0)

  def test_kortilla_tarpeeksi_rahaa_maukas_lkm_kasvaa(self):
    maksukortti = Maksukortti(10)
    self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
    self.assertEqual(self.kassapaate.maukkaat, 0)

  # kassan rahamäärä kortilla
  def test_kassan_rahamaara_ei_muutu_kun_ostaa_edullisen_kortilla(self):
    maksukortti = Maksukortti(1000)
    self.kassapaate.syo_edullisesti_kortilla(maksukortti)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
  
  def test_kassan_rahamaara_ei_muutu_kun_ostaa_maukkaan_kortilla(self):
    maksukortti = Maksukortti(1000)
    self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000) 
  
  def test_kassan_rahamaara_ei_muutu_jos_kortilla_ei_rahaa(self):
    maksukortti = Maksukortti(10)
    self.kassapaate.syo_edullisesti_kortilla(maksukortti)
    self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

  # Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla 
  def test_kortille_ladatessa_kortin_saldo_on_oikein(self):
    maksukortti = Maksukortti(0)
    self.kassapaate.lataa_rahaa_kortille(maksukortti, 1337)
    self.assertEqual(maksukortti.saldo, 1337)

  def test_kortille_ladatessa_kassan_rahat_kasvavat_ladatulla_summalla(self):
    maksukortti = Maksukortti(0)
    self.kassapaate.lataa_rahaa_kortille(maksukortti, 1337)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 101337)
  
  def test_kortille_ladatessa_miinus_rahaa_kortin_saldo_ei_muutu(self):
    maksukortti = Maksukortti(10)
    self.kassapaate.lataa_rahaa_kortille(maksukortti, -100)
    self.assertEqual(maksukortti.saldo, 10)

  def test_kortille_ladatessa_negatiivista_kassan_rahat_eivat_muutu(self):
    maksukortti = Maksukortti(0)
    self.kassapaate.lataa_rahaa_kortille(maksukortti, -1337)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
  

