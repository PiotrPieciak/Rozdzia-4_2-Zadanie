#funkcja "palindrome" pobiera słowo i sprawdza czy jest palindromem
def palindrome(word):
  #Poniższe linie to dłuższy zapis "return word == word[::-1]"
  #if word == word[::-1]:
  #  return True
  #else:
  #  return False

  #funkcja sprawdza czy pobrany argument zapisany w odwrotnej kolejności jest taki sam jak zapisany w pierwotnej kolejności. Jeśli tak zwróci True, jeśli nie zwróci False
  return word == word[::-1]

#w wierszu poniżej wywołujemy naszą funkcję z argumentem "kajak"
print(palindrome("kajak"))