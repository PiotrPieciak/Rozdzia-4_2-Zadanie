#funkcja "palindrome" pobiera słowo i sprawdza czy jest palindromem
def palindrome(word):
  #finkcja sprawdza czy pobrany argument zapisany w odwrotnej kolejności jest taki sam jak zapisany w pierwotnej kolejności. Jeśli tak zwróci True, jeśli nie zwróci False
  if word == word[::-1]:
    return True
  else:
    return False

#w wierszu poniżej wywołujemy naszą funkcję z argumentem "kajak"
print(palindrome("kajak"))