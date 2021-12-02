import Lab4.HeartFailure.heartfailure
import Lab4.AutoInsurance.prediction_logic

'''
Autorzy: Krystian Dąbrowski s18550, Krzysztof Windorpski s18562

Projekt: Systemy klasyfikacji wartości wypłat ubezpieczalni samochodowej oraz chorób serca

Problem: 
1. Na podstawie danych historycznych przewidujemy jaką wypłatę w tysiącach szwedzkich koron należy wypłacić za daną ilość zgłoszeń
2. Na podstawie danych 918 pacjentów przewidujemy czy u danej osoby na podstawie jej danych zdrowotnych (tetno, glukoza, itp) 
   jest ryzyko wystapienia choroby serca 

Podsumowanie:
AutoInsurance - wykonany metodą SLR simple linear regression - wykorzystujący regresję liniową wyznaczającą średnią przewidywaną 
na podstawie historycznych danych 

HeartFailure - wykonany metodą RBF radial basis function. Ilośc punktów w danym miejscu określa, tzw. "hot spot'y", 
w które jeżeli wpasują się nasze dane to mamy dużą szansę na poprawny przewidywany wynik. 

Patrz: GammaExplanation.png

Sposób użycia:

Uruchom plik main.py

'''