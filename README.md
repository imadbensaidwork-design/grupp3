# Grupparbete - Grupp 3

### Utvecklingsmiljö
    - Python: 3.11.7
    - Virtuell mijlön: .venv

## Installation 
1. Öppna projektmappen 
```git
cd grupp3
```
2. Skapa en virtuell miljö
   
   - Se till att versionen av Python är 3.11
```git
python -m venv .venv
```
3. Aktivera vistuell miljön
   
   - Med den aktiverar vi den virtuella miljön , vi borde se (.venv) i terminalen
```git
source .venv/Scripts/activate
```
4. Installera rätt versionen 
```git
python -m pip install -r requirements.txt
```
   - Med den här git kommandot  installerar vi de exakta versionen av Pandas och alla andra bibliotek som behövs för projekten. Detta gör att alla i gruppen använder samma versioner och då slipper installera dem globalt i vår egern systmet. 