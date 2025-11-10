import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

	#self.assertEqual(str(self.varasto.__str__()), lmao) / f-string
    #Testaa printin
    def test_printtaus(self):
        self.varasto.lisaa_varastoon(8)
        lmao = "saldo = 8, vielä tilaa 2"
        self.assertEqual(str(self.varasto), lmao)

	#Liian pieni varasto
    def test_uudella_varastolla_liian_pieni(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

	#Alkusaldo oikea
    def test_alkusaldo_oikea(self):
        self.varasto = Varasto(10, 8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

	#Alkusaldo <0
    def test_alkusaldo_alle_nolla(self):
        self.varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

	#Alkusaldo > Tilavuus
    def test_alkusaldo_yli_tilavuuden(self):
        self.varasto = Varasto(10, 11)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

	#yritetään ottaa liikaa
    def test_yritetaan_ottaa_liikaa(self):
        self.varasto.lisaa_varastoon(8)

        # Yritetään ottaa 1 liikaa
        self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

	#yritetään ottaa negatiivinen
    def test_yritetaan_ottaa_negatiivinen(self):
        self.varasto.lisaa_varastoon(8)

        # Yritetään ottaa nega
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, 8)

	# yritetään laittaa liikaa
    def test_laitetaan_liikaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(3)
        self.assertAlmostEqual(self.varasto.saldo, 10)

	# yritetään laittaa alle 0
    def test_laitetaan_negatiivinen(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

	#Lisääminen vie tilaa
    def test_lisaaminen_vie_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.lisaa_varastoon(1)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 1)
