 # -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:10:07 2021

Ficha Interativa (beta)

@author: Nascimento
"""
    
pontos = 100

FOR = 7
CON = 8
DES = 17
AGI = 10
INT = 17
VON = 17
CAR = 14
SAB = 10

buffRaca   = 0
buffClasse = 0

pontosUsados = (FOR + CON + DES + AGI + INT + VON + CAR + SAB)

if pontos == pontosUsados:
    
    #Bases globais
    base = 10
    AtributosNaturais = 5
    periciasFOR = 4
    periciasDES = 6
    periciasAGI = 6
    periciasINT = 9
    periciasVON = 3
    periciasTotal = (periciasFOR + periciasDES + periciasAGI + periciasINT + periciasVON)
    periciasMedia = periciasTotal/AtributosNaturais
    
    #Atributos Naturais
    forca        = base + FOR
    constituição = base + CON
    destreza     = base + DES
    agilidade    = base + AGI
    inteligencia = base + INT
    vontade      = base + VON
    
    #Atributos Secundários
    carisma   = base + CAR
    sabedoria = base + SAB
    
    #Habilidades
    Fortitude = round((forca + constituição)/2)
    Reflexo   = round((agilidade + vontade)/2)
    Percepção = round((destreza + inteligencia)/2)
    Defesa    = round((constituição + destreza)/2)
    
    BonusFortitude = Fortitude - 2*base
    BonusReflexo   = Reflexo   - 2*base
    BonusPercepção = Percepção - 2*base
    BonusDefesa    = Defesa    - 2*base
    
    #Propriedades
    Vida     = 2*constituição + forca + buffRaca
    Mana     = vontade + round(sabedoria/2) + buffClasse
    Ações    = round((constituição + agilidade)/10) + 2
    Sanidade = 2*vontade - int(inteligencia/10)
    
    #Pontos Perícias
    pontosFOR = round(FOR*(periciasFOR/periciasMedia))
    pontosDES = round(DES*(periciasDES/periciasMedia))
    pontosAGI = round(AGI*(periciasAGI/periciasMedia))
    pontosINT = round(INT*(periciasINT/periciasMedia))
    pontosVON = round(VON*(periciasVON/periciasMedia))
    
    #Pontos Faculdades
    
    
    #Pontos Relações
    
    
    
    
    print('######################################################''\n'
          'ATRIBUTOS:' '\n')
    print('Força        =', forca,'(Perícias: ',pontosFOR,'pontos)')
    print('Constituição =', constituição)
    print('Destreza     =', destreza,'(Perícias: ',pontosDES,'pontos)')
    print('Agilidade    =', agilidade,'(Perícias: ',pontosAGI,'pontos)')
    print('Inteligência =', inteligencia,'(Perícias: ',pontosINT,'pontos)')
    print('Vontade      =', vontade,'(Perícias: ',pontosVON,'pontos)')
    print('\n')
    print('Carisma      =', carisma,'(Relações:   ',CAR,'pontos)')
    print('Sabedoria    =', sabedoria,'(Faculdades: ',SAB,'pontos)')
    print('\n\n')
    
    print('######################################################''\n'
          'HABILIDADES:' '\n'
          )
    print('Fortitude = ',Fortitude,'(Bonus: ',BonusFortitude,'  )')
    print('Reflexo   = ',Reflexo,'(Bonus: ', BonusReflexo,'  )')
    print('Percepção = ',Percepção,'(Bonus: ',BonusPercepção,'  )')
    print('Defesa    = ',Defesa,'(Bonus: ',BonusDefesa,'  )')
    
    print('\n\n')
    
    print('######################################################''\n'
          'PROPRIEDADES:' '\n'
          )
    print('Vida     =', Vida)
    print('Mana     =', Mana)
    print('Ações    =', Ações)
    print('Sanidade =', Sanidade)
        
    
elif pontos > pontosUsados:
    print('ERRO: AINDA FALTAM ', (pontos - pontosUsados), 'PONTOS!')
    
else:
    print('ERRO: O NUMERO DE PONTOS EM USO ESTÁ EXTRAPOLADO:', 
          (pontosUsados - pontos), 'pontos precisam ser retirados')
    
