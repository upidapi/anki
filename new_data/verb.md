# promt to get the compact present conjugations for words

https://chatgpt.com/c/670121ac-257c-800b-b7b5-6ee6d6c469f2

```
given the following list of spanish verbs and their swedish translations add extra info to the spanish part

add /u/ /ue/ /ie/ etc for various diphthongisation

if the verb doesn't conform to the rules for the first person form add that form in paranthasies

if the verb is conjugated like another ad said verb in angle brackets

if that extra info isn't enough to determine each form in the present then add each present for but add 4 spaces before each one  

for example for the following input:
poder | kunna
ir | gå, åka
ser | vara (permanent)
seguir | följa, fortsätta

you would output:
poder /ue/ | kunna
ir (voy) <var> | gå, åka
ser | vara (permanent)
    soy | jag är (permanent)
    eres | du är (permanent)
    es | han/hon/den är (permanent)
    somos | vi är (permanent)
    sois | ni är (permanent)
    son | de är (permanent)
seguir (sigo) | följa, fortsätta
```

you probl


# some test data
```
poner | lägga, ställa, sätta
seguir | följa, fortsätta
ver | se
ir | gå, åka
querer | vilja, älska
poder | kunna
pedir | be om, begära
estar | vara (tillstånd), befinna sig
ser | vara (permanent)
tener | ha
dar | ge
hacer | göra
decir | säga
saber | veta, kunna
venir | komma
oír | höra
```


```
poner (pongo) | lägga, ställa, sätta
seguir /i/ (sigo) | följa, fortsätta
ver (veo) | se
ir (voy) | gå, åka
    voy | jag går, åker
    vas | du går, åker
    va | han/hon/den går, åker
    vamos | vi går, åker
    vais | ni går, åker
    van | de går, åker
querer /ie/ | vilja, älska
poder /ue/ | kunna
pedir /i/ | be om, begära
estar | vara (tillstånd), befinna sig
    estoy | jag är (tillstånd)
    estás | du är (tillstånd)
    está | han/hon/den är (tillstånd)
    estamos | vi är (tillstånd)
    estáis | ni är (tillstånd)
    están | de är (tillstånd)
ser | vara (permanent)
    soy | jag är (permanent)
    eres | du är (permanent)
    es | han/hon/den är (permanent)
    somos | vi är (permanent)
    sois | ni är (permanent)
    son | de är (permanent)
tener /ie/ (tengo) | ha
dar (doy) | ge
hacer (hago) | göra
decir /i/ (digo) | säga
saber (sé) | veta, kunna
venir /ie/ (vengo) | komma
oír (oigo) | höra
    oigo | jag hör
    oyes | du hör
    oye | han/hon/den hör
    oímos | vi hör
    oís | ni hör
    oyen | de hör
```



```
given the following list of spanish verbs and their swedish translations add extra info to the spanish part

1. add /u/ /ue/ /ie/ etc for various diphthongisation

2. if the verb doesn't conform to the rules for the first person form add that form in paranthasies

3. if the verb is conjugated according to only the rules of ar, er, and ir verbs of another word (doesn't have to be a real word) the put that word in ange brackets

4. If the verb is irregular. And points 1-3 doesnt fully clarify this. Then you should return each form but indented with 4 spaces. While ignoring points 1 thrugh 3. 

for example for the following input:
poder | kunna
ir | gå, åka
ser | vara (permanent)
seguir | följa, fortsätta

you would output:
poder /ue/ | kunna
ir (voy) <var> | gå, åka
ser | vara (permanent)
    soy | jag är (permanent)
    eres | du är (permanent)
    es | han/hon/den är (permanent)
    somos | vi är (permanent)
    sois | ni är (permanent)
    son | de är (permanent)
seguir (sigo) | följa, fortsätta

if you are unsure of the instructions please ask clarifying questions until you are then return a improved promt

```

```
Instructions for Processing the Verbs:
    1. Add diphthongization notation (e.g., /u/, /ue/, /ie/, etc.) to the Spanish verb.
    2. If the verb does not conform to the standard rules for the first person form (yo), provide that form in parentheses.
    3. If the verb follows the conjugation rules of -ar, -er, or -ir verbs based on another word that isn't this word, (even if that word is not real), include that word in angle brackets.
    4. If the verb is irregular and points 1-3 doesnt fully clarify this, list each form indented with four spaces while disregarding points 1-3. 

Afterwards go thrugh the your output and make sure that there is enough information that you can reconstruct each of the 6 forms, but not any uneccisary info. If not update the outputed with a corrected version, taht doesn't include each of the 6 forms unless required by point 4.

Example Input:

    poder | kunna
    ir | gå, åka
    ser | vara (permanent)
    seguir | följa, fortsätta

Expected Output:

    poder /ue/ | kunna
    ir (voy) <var> | gå, åka
    ser | vara (permanent)
        soy | jag är (permanent)
        eres | du är (permanent)
        es | han/hon/den är (permanent)
        somos | vi är (permanent)
        sois | ni är (permanent)
        son | de är (permanent)
    seguir (sigo) | följa, fortsätta


output it in a raw text format
```


