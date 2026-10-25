# Variabler, tall og matematikk i Python

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne lage og bruke variabler i Python
* Kunne regne med tall i Python
* Kunne bruke resultatene i enkle programmer
:::::



:::::::::::::::{summary} Variabler
En variabel er et navn som peker på en verdi.

:::{code-block} python
x = 5
navn = "Ada"
:::

`=` i Python betyr **tilordning**: verdien på høyre side lagres i variabelen på venstre side.
:::::::::::::::

:::::::::::::::{example} Eksempel 1: Lage variabler
:::{code-block} python
---
linenos:
---
a = 3
b = 4
sum = a + b

navn = "Juan"

print(sum)

print(navn)
:::

Utskrift:
```text
7
Juan
```
:::::::::::::::

:::{margin}
"#" tegnet brukes til å skrive kommentarer i koden og programmet vil se bort ifra teksten bak et hashtag når programmet kjører.
:::

:::::::::::::::{exercise} Underveisoppgave 1
Skriv kode som laget to variabler `a`{l=python} og `b`{l=python} og beregner summen av tallene `8`{l=python} og `12`{l=python}, og skriv ut svaret.

:::{interactive-code}
# Skriv programmet ditt her
a = 
b = 



:::

:::::{solution}
:::{code-block} python
---
linenos:
---
sum = 8 + 12
print(sum)
:::
:::::
:::::::::::::::



## Regneoperatorer

:::::::::::::::{summary} Vanlige operatorer
| Operator | Betydning | Eksempel | Vanlig notasjon |
|----------|-----------|----------|-------|
| `+`{l=python} | addisjon | `3 + 2` | $3 + 2$ |
| `-`{l=python} | subtraksjon | `7 - 4` | $7 - 4$ |
| `*`{l=python} | multiplikasjon | `3 * 5` | $3 \cdot 5$ |
| `/`{l=python} | divisjon | `7 / 2` | $\frac{7}{2}$ |
| `**`{l=python} | potens | `2 ** 3` | $2^3$ |
:::::::::::::::

:::::::::::::::{example} Eksempel 2: Regneuttrykk
:::{code-block} python
---
linenos:
---
x = 2
y = 5
print(x + y)
print(y - x)
print(x * y)
print(y ** x)
:::

Utskrift:
```text
7
3
10
25
```
:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 2
Skriv kode som regner ut arealet av et rektangel med `lengde = 7`{l=python} og `bredde = 4`{l=python}.

:::{interactive-code}
# Skriv programmet ditt her



:::

:::::{solution}
:::{code-block} python
---
linenos:
---
lengde = 7
bredde = 4
areal = lengde * bredde
print(areal)
:::
:::::
:::::::::::::::

:::{margin}
Tips: Bruk tydelige variabelnavn. Det gjør koden lettere å lese senere.
:::

## Variabeltyper

De vanligste variablertypene i Python er:

- `int`{l=python}: heltall, for eksempel `5`{l=python}, `-2`{l=python}
- `float`{l=python}: desimaltall, for eksempel `3.5`{l=python}, `-0.25`{l=python}
- `string`{l=python}: tekst, for eksempel `"Ada"`{l=python}, `"-0.25"`{l=python}


:::::::::::::::{example} Eksempel 3: Forskjellige typer variabler lagt sammen
:::{code-block} python
---
linenos:
---
x = 5
y = 2.5
z = 2
navn = "Hei"

print(x + y)
print(x - z)
print(x * z)
print(x / z)

print(navn + " er mitt navn.")
:::

Utskrift:
```text
7.5
3
10
2.4
Jens er mitt navn.

```

Nå viser vi flere operasjoner med samme variabler. Resultatet av `/` gir en `float`{l=python} variabel, mens `+`, `-` og `*` gir  en `int`{l=python} variabel. Vi kan ikke addere `+` en variabel med type `string`{l=python} og `ìnt`{l=python}.
:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 3
La `a = 10`{l=python}, `b = 3`{l=python}, `fornavn = "Ali"`{l=python} og `etternavn = "Hussein"`{l=python}

Skriv ut:
- `a + b`
- `a - b`
- `a * b`
- `a / b`
- `etternavn + fornavn`

:::{interactive-code}
# Skriv programmet ditt her



:::

:::::{solution}
:::{code-block} python
---
linenos:
---
a = 10
b = 3
fornavn = "Ali "
etternavn = "Hussein"
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(fornavn + etternavn)

:::
:::::
:::::::::::::::
