# Programmering av tallfølger

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne lage programmer som lager tallene i en tallfølge.
* Kunne lage programmer som finner summen av tall i en tallfølge.
:::::

Tallfølger er nært knyttet til de naturlige tallene og egenskaper ved tall. Du har kanskje møtt på figurtall før som trekanttall eller kvadrattall. Dette er eksempler på tallfølger som er representert med figurer. Her skal vi se på hvordan vi kan bruke programmering til å svare på spørsmål knyttet til tallfølger og figurtall. 

## Formler

Når vi skriver et program, så ønsker vi ofte å regne med formler. 


:::::::::::::::{example} Eksempel 1

:::{figure} ./figurer/eksempler/eksempel_2.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::

Over ser vi figurtallene til de tre første i formelen $F_n = 3\cdot n + 1$.
Vi skriver ut de fire første figurtrallene:


:::{code-block} python
---
linenos:
---
for n in range(1,5):
    print(3 * n + 1)
:::

Dette programmet skriver ut:
```text
4
7
11
14
```
::::

Vi kan også skrive ut tekst for hvert figurtall:
:::{code-block} python
---
linenos:
---
for n in range(1,5):
    print("Figur nummer", n , ":", 3 * n + 1)
:::

Dette programmet skriver ut:
```text
Figur nummer 1 : 4
Figur nummer 2 : 7
Figur nummer 3 : 10
Figur nummer 4 : 13
```

::::

:::::::::::::::


:::::::::::::::{explore} Utforsk 1
Nedenfor vises et program som bruker en formel for å regne ut og skrive ut noen tall i en tallfølge.

Les programmet og forutsi hvilke tall programmet skriver ut.

:::::::::::::

::::::::::::::

:::{interactive-code}
---
predict:
---
for n in range(1, 5):
    a = 2 * n**2 + 3
    
    print(a)
:::
:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 1

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet nedenfor slik at det skriver ut verdiene til tallfølgen gitt ved 

$$
a_n = 2n + 3 \qfor n \in \set{1, 2, 3, 4, 5}
$$

:::{interactive-code}
for n in range(????): # FYLL INN
    a = # FYLL INN
    
    print(a)

:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(1, 6):
    a = 2 * n**2 + 1
    
    print(a)
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Fyll ut programmet nedenfor slik at det skriver ut verdiene til tallfølgen gitt ved 

$$
b_n = n^2 + 2n + 1 \qfor n \in \set{1, 3, 5, 7, 9}
$$

:::{interactive-code}
for n in range(????): # FYLL INN
    b = # FYLL INN
    
    print(b)

:::

::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(1, 10, 2):
    b = n**2 + 2 * n + 1
    
    print(b)
:::
::::

:::::::::::::


:::::::::::::{tab-item} c
Fyll ut programmet nedenfor slik at det skriver ut verdiene til tallfølgen gitt ved 

$$
c_n = 2^n \qfor n \in \set{-2, -1, 0, 1, 2}
$$

:::{interactive-code}
for n in range(????): # FYLL INN
    c = # FYLL INN
    
    print(c)

:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(-2, 3):
    c = 2 ** n
    
    print(c)
:::
::::
:::::::::::::
::::::::::::::



:::::::::::::::


## Summere tall i en tallfølge

I mange tilfeller er vi interessert i å summere tallene i en tallfølge. 


:::{margin} `s = s + n`{l=python}
Når vi skriver `s = s + n`{l=python}, så betyr det at vi legger til verdien til `n`{l=python} til verdien til `s`{l=python} og lagrer resultatet i `s`{l=python}. 
:::

:::::::::::::::{explore} Utforsk 2
Nedenfor vises et program som summerer noen tall. 



Les programmet nedenfor og forutsi hva som skrives ut. 

Skriv inn svaret ditt nedenfor og sjekk.
:::::::::::::


:::::::::::::

::::::::::::::

:::{interactive-code}
---
predict:
---
s = 0
for n in range(1, 6):
    s = s + n

print(s)
:::

:::::::::::::::


:::::::::::::::{example} Eksempel 2

:::{figure} ./figurer/eksempler/n*n.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::

Over ser vi figurtallene til de tre første kvadrattallene $k_n = n^2$.
Vi ønsker å summere de tre første kvadrattallene. Vi lager derfor en variabel `sum = 0`{l=python} og adderer figurtallet for hvert steg i `for`{l=python}-løkken.


:::{code-block} python
---
linenos:
---
sum = 0
for n in range(1,4):
    sum = sum + n**2
    print(sum)
:::

Dette programmet skriver ut:
```text
1
5
14
```
::::

Det programmet skriver ut er:<br>
$k_1 = 1$<br>
$k_1 + k2 = 5$ <br>
$k_1 + k_2 + k_3 = 14$


:::::::::::::::

:::::::::::::::{example} Eksempel 3

:::{figure} ./figurer/eksempler/n*n.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::

Vi ser igjen på kvadrattallene med formelen $k_n = n^2$.
Hvis vi har 100 ruter tlgjengelig til å tegne kvadrattall, hvor mange kvadrattall kan vi tegne?

Vi ønsker dermed å stoppe løkken som summerer figurtallene når summen er større enn 100.
Dette kan vi gjøre med en `while`{l=python}-løkke som kjører `while sum < 100`{l=python}. Vi lager variabelen `n`{l=python} for å holde styr på hvor mange figurtall vi har summert. <br>

I tillegg bruker vi en `if`{l=python}-setning etter `while`{l=python}-løkken siden vi hvis vi må summere fordi 100 for at `while`{l=python}-løkken skal stoppe. Vi må derfor trekke fra forrige `sum`{l=python} og forrige `n`{l=python}: <br> `sum = sum - n**2`{l=python} <br> `n = n - 1`{l=python}.
:::{code-block} python
---
linenos:
---
sum = 0
n = 0  # Antall figurer vi har laget

while sum < 100:
    n = n + 1
    sum = sum + n**2

if sum > 100:
    sum = sum - n**2
    n = n - 1

print("Man kan lage", n, "kvadrattall med 100 ruter, og da har man brukt", sum, "ruter.")
:::

Dette programmet skriver ut:
```text
Man kan lage 6 kvadrattall med 100 ruter, og da har man brukt 91 ruter.

```
::::




:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 2

:::{figure} ./figurer/eksempler/n*(n+1).svg
---
width: 70%
class: no-click, adaptive-figure
---
:::

Over ser vi figurtallene til de tre første Rektangeltallene $R_n = n\cdot(n+1)$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

Endre programmet nedenfor slik at det skriver hvor mange ruter det er i de fem første rektangeltallene.


:::{interactive-code}
for n in range(????): # FYLL INN
    R = # FYLL INN
    print(# FYLL INN)

:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(1,6):
    R = n*(n+1)
    print(R)
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Endre på programmet slik at det skriver ut summen av det første, det andre og opp til det femte rektangeltallet:
```text
2
8
20
40
70
```



:::{interactive-code}
sum = # FYLL INN
for n in range(????): # FYLL INN
    R = # FYLL INN
    sum = # FYLL INN
    print (sum)

:::

::::{answer}
:::{code-block} python
---
linenos:
---
sum = 0
for n in range(1,6):
    R = n*(n+1)
    sum = sum + R
    print (sum)
:::
::::

:::::::::::::


:::::::::::::{tab-item} c
Endre på programmet slik at det bare skriver ut summen av de fem første rektangeltallene.
```text
70
```

:::{interactive-code}
sum = # FYLL INN
for n in range(????): # FYLL INN
    R = # FYLL INN
    sum = # FYLL INN
    print (sum)

:::


::::{answer}
:::{code-block} python
---
linenos:
---
sum = 0
for n in range(1,6):
    R = n*(n+1)
    sum = sum + R
print (sum)
:::
::::
:::::::::::::

:::::::::::::{tab-item} d
Endre på programmet slik at det skriver ut
```text
Man kan lage 6 rektageltall med 100 ruter, og da har man brukt 91 ruter.
```

:::{interactive-code}
sum = # FYLL INN
n = # FYLL INN  # Antall figurer vi har laget

while sum < # FYLL INN:
    n = # FYLL INN
    sum = # FYLL INN

if sum > # FYLL INN:
    sum = # FYLL INN
    n = # FYLL INN

print("Man kan lage", n, "rektangeltall med 100 ruter, og da har man brukt", sum, "ruter.")

:::


::::{answer}
:::{code-block} python
---
linenos:
---
sum = 0
n = 0  # Antall figurer vi har laget

while sum < 100:
    n = n + 1
    sum = sum + n*(n+1)

if sum > 100:
    sum = sum - n*(n+1)
    n = n - 1

print("Man kan lage", n, "rektangeltall med 100 ruter, og da har man brukt", sum, "ruter.")
:::
::::
:::::::::::::
::::::::::::::



:::::::::::::::






:::::::::::::::

