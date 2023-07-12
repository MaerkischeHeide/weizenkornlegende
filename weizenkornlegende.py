def schachbrett(n):
    if n == 0:
        return 0
    else:
        return 2**(n-1) + schachbrett(n-1)

print("Die Weizenkornlegende / Die Schachbrettaufgabe:")
print("Auf jedem Feld liegt die doppelte Anzahl Körner des vorheriegen Feldes")
n = int(input("Geben Sie die Anzahl der Felder des Schachbretts ein: "))
print("Gesamte Anzahl der Weizenkörner auf dem Schachbrett mit", n, "Feldern: ", schachbrett(n))