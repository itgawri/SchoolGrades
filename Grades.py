student_name = "Sam"
math_grade = 88
science_grade = 75
english_grade = 90
geology_grade = 69
polish_grade = 91
informatic_grade = 99
total_grade = math_grade + science_grade + english_grade + geology_grade + polish_grade + informatic_grade
max_grade = 600
total_medium = total_grade / 0.6
total_percentage = total_grade / max_grade * 100
print(f"Sam's total percentage is {total_percentage}%")
total_percentage = int(total_percentage)
did_student_pass = total_percentage >= 50
sporting_activities = bool(0)
print(f"Sam participated in sporting activities: {sporting_activities}")
print(f"Sam's total percentage as an integer is {total_percentage}%")
print(f"Sam passed to the next semester: {did_student_pass}")
print(f"Sam's average is.: {total_medium}")

# -------------------------------------------------------------------------------------

imie_studenta = "Sam"
ocena_matematyka = 88
ocena_przyroda = 75
ocena_angielski = 90
ocena_geologia = 69
ocena_polski = 91
ocena_informatyka = 99
suma_ocen = ocena_matematyka + ocena_przyroda + ocena_angielski + ocena_geologia + ocena_polski + ocena_informatyka
maksymalna_ocena = 600
suma_waga = suma_ocen / 0.6
procent_ocen = suma_ocen / maksymalna_ocena * 100
print(f"Procentowa ocena Sama wynosi {procent_ocen}%")
procent_ocen = int(procent_ocen)
czy_student_zdal = procent_ocen >= 50
uczestnictwo_w_aktywnosciach_sportowych = bool(0)
print(f"Sam brał udział w zajęciach sportowych: {uczestnictwo_w_aktywnosciach_sportowych}")
print(f"Procentowa ocena Sama jako liczba całkowita wynosi {procent_ocen}%")
print(f"Sam przeszedł do kolejnego semestru: {czy_student_zdal}")
print(f"Średnia ważona Sama wynosi: {suma_waga}")

print(suma_ocen)
