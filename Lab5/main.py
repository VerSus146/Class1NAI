'''
Autorzy: Krystian Dąbrowski s18550, Krzysztof Windorpski s18562

Projekt: Sieci neuronowe dla klasyfikacji

Problem:
1. Na podstawie danych pacjentów tworzymy model sieci neuronowej mający pomóc przewidzieć chorobę serca - porównanie z SVC
2. Wykrywanie różnic między różnymi zwierzętami, a środkami transportu
3. Wkrywanie różnych części garderoby + Confussion Matrix

Podsumowanie:
HeartFailure - Sieć Neuronowa w około 80% jest w stanie poprawnie wykryć chorobę serca przy loss=0.43 .
  Jest wynik o 35% lepszy niż w przypadku klasyfikacji za pomocą SVC.
Animals - Sieć Neuronowa w około 70% jest w stanie poprawnie rozróżnić zwierzę od środka transportu oraz poprawnie je
  sklasyfikować. Loss = 0.5
Dresses - Sieć Neuronowa w około 85% jest w stanie poprawnie rozróżnić części garderoby. Loss = 0.3. Dodatkowo dodaliśmy
  Conffusion Matrix

Do Animals oraz Dresses Wygenerowaliśmy model który możemy sobie w dowolnej chwili wczytać i wykonać nowe predykcje

Sposób użycia:

Dla Dresses:
  - uruchamiamy dresses.py - jeżeli model jeszcze nie istnieje to się nam wygeneruje. Jeżeli istnieje wykona predykcje.
    * Pokaże on nam Conffusion Matrix
Dla Animals:
  - Jeżeli model nie istnieje:
    * Uruchamiamy cifar10ModelGenerator.py - wygeneruje nam on nowy model lub zastąpi istniejący
  - Jeżeli model istnieje:
    * Uruchamiamy animalRecognition.py - wykona on nam predykcje
Dla Heart Failure:
  - Uruchamiamy heartfailure.py - wygeneruje on i wykona predykcje
    * Pokaże nam on PLT accuracy i val_accuracy oraz loss i val_loss

'''