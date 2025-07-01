lass Asystent:
    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja

class AnalizaJezykowa:
    def analizuj_zapytanie(self, zapytanie):
        # Prosta symulacja analizy zapytania
        if "pogoda" in zapytanie.lower():
            return "intencja_pogoda"
        elif "czas" in zapytanie.lower():
            return "intencja_czas"
        else:
            return "intencja_nieznana"

class GeneratorOdpowiedzi:
    def generuj_odpowiedz(self, analiza):
        # Generowanie odpowiedzi na podstawie analizy
        if analiza == "intencja_pogoda":
            return "Dziś jest słonecznie i 25 stopni."
        elif analiza == "intencja_czas":
            return "Jest godzina 15:00."
        else:
            return "Przepraszam, nie rozumiem pytania."

class InteligentnyAsystent:
    def __init__(self, nazwa, wersja):
        self.asystent = Asystent(nazwa, wersja)
        self.analizator = AnalizaJezykowa()
        self.generator = GeneratorOdpowiedzi()

    def odpowiedz_na_zapytanie(self, zapytanie):
        analiza = self.analizator.analizuj_zapytanie(zapytanie)
        return self.generator.generuj_odpowiedz(analiza)

# Przykład użycia:
# bot = InteligentnyAsystent("AI-Bot", "1.0")
# print(bot.odpowiedz_na_zapytanie("Jaka jest dziś pogoda?"))
