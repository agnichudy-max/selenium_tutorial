import unittest

class TestCzlowiek(unittest.TestCase):
    def setUp(self):
        self.czlowiek = Czlowiek("Stasio")
        #print("Przygotowanie testu")
        pass
    #Metody testowe
    # zaczynaja sie od slowa test...
    # testy wykonuja sie w dowolnej kolejnosci
    def test_przedstaw_sie(self):
        przedstwieniesie_str = self.czlowiek.przedstawsie_str()
        #print("Test pierwszy")
        self.assertEqual("Czesc jestem Stasio", przedstwieniesie_str)
        pass
    def test002Drugi(self):
        #print("Test drugi")
        pass
    def tearDown(self):
        del self.czlowiek

        #print("Koniec testu")
        pass
if __name__ == "__main__":
    unittest.main(verbosity=1) # gadatliwosc 0,1,2


