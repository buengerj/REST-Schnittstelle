<h3>Aufagenstellung</h3>
Es soll eine Server-Anwendung erstellt werden, mit deren Hilfe Todo-Listen mit entsprechenden Einträgen erstellt und bearbeitet werden können. Jede Liste besteht aus
einer beliebigen Anzahl an Einträgen und ist einem Benutzer zugewiesen.
Jeder Eintrag einer Todo-Liste besteht aus einer ID, einem Namen, einer optionalen
Beschreibung und der Zuordnung zu einer Todo-Liste und einem Benutzer. Jede Todo-Liste und jeder Benutzer besitzt neben der ID einen Namen.
Die Schnittstelle muss es ermöglichen, Listen neu anzulegen und bestehende Listen zu
löschen. Über einen Endpunkt können alle Einträge der Liste geladen werden. Außerdem müssen Einträge in Listen hinzugefügt und gelöscht werden können. Für die
Festlegung der Listenbesitzer müssen neue Benutzer hinzugefügt und gelöscht und es
muss eine Liste aller vorhandenen Benutzer abgefragt werden können.
Eine Authentifizierung ist zunächst nicht zu planen bzw. implementieren. Aus Sicherheitsgründen sollen jedoch für alle verwendeten IDs keine fortlaufenden Nummern
verwendet werden. Statt dessen werden zufällige GUID genutzt.
