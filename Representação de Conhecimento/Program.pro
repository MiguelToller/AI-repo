%fatos ou verdades
nasceuEm("Miguel","Guajara Mirim").
nasceuEm("Gabriel","Porto Velho").
nasceuEm("Cassio","Sao Pedro").
nasceuEm("Luciana","Sao Pedro").
nasceuEm("Glades","Sao Pedro").
nasceuEm("Flori","Sao Pedro").
nasceuEm("Iracema","Sao Pedro").

%regra recursiva de sobrecarga
nasceuEm(Pessoa, Lugar):- 
    nasceuEm(Pessoa, I),
    estaEm(I, Lugar).

localizadoEm("Guajara Mirim","RO").
localizadoEm("Porto Velho","RO").
localizadoEm("Sao Pedro","RS").
localizadoEm("RS","Brasil").
localizadoEm("RO","Brasil").

%regra recursiva
estaEm(Lugar, OutroLugar) :-
    localizadoEm(Lugar, OutroLugar).
estaEm(Lugar, OutroLugar) :-
    localizadoEm(Lugar, I),
    estaEm(I, OutroLugar).

progenitor("Iracema","Flori").
progenitor("Iracema","Glades").
progenitor("Iracema","Luciana").
progenitor("Luciana","Miguel").
progenitor("Luciana","Gabriel").
progenitor("Glades","Cassio").

avo(Avo, Neta) :-
    progenitor(Avo, Pai),
    progenitor(Pai, Neta).

irmao(I1, I2) :-
    progenitor(Pai,I1),
    progenitor(Pai,I2),
    I1 \= I2.

tio(Tio,Sobrinho) :-
    irmao(Tio,Pai),
    progenitor(Pai,Sobrinho).
