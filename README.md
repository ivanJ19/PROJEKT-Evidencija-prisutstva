# PROJEKT-Evidencija-prisutstva

Aplikacija služi za prikazivanje stavljanje prisutstva studenata na predavanjima, te da profesori mogu imate lakši uvid u prisutstvo studenata na njihovim predavanjima.

# Funkcije same aplikacije
Studentima se prilikom prijave na aplikaciju pruža izbor između predmeta koje pohađaju. Nakon odabira predmeta, studenti su automatski stavili prisutsvo koje se prikazuje profesoru. Studentima je tada omogućen uvid u ocjenu koju imaju iz tog predmeta, te opis samog predmeta. Što se tiče profesora, oni kada se ulogiraju, njima se ispisuje popis svih studenata koji su stavili prisutstvo na njegovom satu. Osim imena, profesor vidi email adresu studenta i datum i vrijeme u koje se student prijavio na predavanje.

# Instaliranje aplikacije
Da bi se instlirala aplikacija, potrebna je aplikacija Docker Desktop, uz to je potrebno preuzeti sve datoke koje se nalaze na Github-u. Nakon što se preuzmu sve datoke, potrebno je uz pomoć terminala na računalu doći do dva containera. Da bi se ta dva containera pokrenula unutar dockera potrebno je upisati komandu: docker-compose up -d --build. Uz pomoć ove komande kreiraju se Docker image i Docker container unutar Docker aplikacije. Nakon što smo to kreirali možemo pokrenuti samu aplikaciju koja se nalazi na localhost:8081. Svaki korisnik može ubacivati svoje podatke i uređivati aplikaciju po njegovoj volji unutar koda. nakon što se izmijeni kod unutar jednog od containera, potrebno je ponovo upisati docker-compose up -d --build komandu kako bi se ažurirali podatci.



