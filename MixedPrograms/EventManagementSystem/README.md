# Event Management System

Projekt Event Management System został stworzony przez Marcela Seremaka w Django.

## Opis

Event Management System jest aplikacją webową, która umożliwia użytkownikom organizowanie i zarządzanie wydarzeniami. Projekt skupia się na prostocie użytkowania oraz funkcjonalnościach dostosowanych do potrzeb organizatorów i uczestników wydarzeń.

### Funkcje projektu:

- **Rejestracja i logowanie użytkowników**: Użytkownicy mogą tworzyć konta, logować się i zarządzać nimi, co zapewnia spersonalizowane doświadczenie.
  
- **Dodawanie własnych wydarzeń**: Użytkownicy mogą dodawać wydarzenia, podając tytuł, opis, czas i miejsce za pomocą interaktywnej mapy do wyboru punktu na mapie.

- **Zakup biletów**: Możliwość zakupu biletów na wydarzenia, z możliwością dodawania do koszyka, edycji ilości i finalizacji zakupu.

- **Koszyk zakupowy**: Funkcjonalność koszyka, gdzie użytkownicy mogą dodawać i usuwać bilety przed dokonaniem płatności.

- **Zarządzanie bazą danych**: Wykorzystanie Django ORM do operacji na bazie danych, przechowującej informacje o użytkownikach, wydarzeniach i zakupionych biletach.

- **Zakładka kontaktowa**: Przyszli użytkownicy mogą podać swój adres e-mail w formularzu kontaktowym, który umożliwia wysyłanie maili z informacjami o wydarzeniach.

## Instalacja i uruchomienie

Aby uruchomić projekt lokalnie, wykonaj następujące kroki:

1. **Pobranie projektu**:
   ```bash
   git clone https://github.com/twoje-repozytorium.git
   cd EventManagementSystem
   
2. **Instalacja wymaganych bibliotek**

   ```bash
   pip install -r requirements.txt

3. **Wykonanie migracji**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

4. **Uruchomienie serwera deweloperskiego**
   ```bash
   python manage.py runserver
Aplikacja będzie dostępna pod adresem http://localhost:8000.

## Użyte technologie
- Django
- HTML, CSS (Bootstrap)
- JavaScript
- SQLite

### Autor
Marcel Seremak


#### © 2024 Marcel Seremak. Wszelkie prawa zastrzeżone.