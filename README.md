Accident-Reporting-System
=========================
Group Members:
Arjun Sunel 

Abhimanyu Niroola 

Abhishek Kumar 

Manjeet Singh 

Santosh Reddy 
 
Project Goal: To develop an android application for reporting a vehicular accident to the concerned authorities/family members of the victims while keeping the anonymity of the informer.
 
Inspiration: Many road accidents either go unreported or are reported when it is too late because of the inherent fear of the law enforcing officers to avoid to scrutiny. Thus, there is a need for an application that reports such incidents and the identity of the informer remains unrevealed.
 
Approach:
 
The functioning of the application is such that the user is to click an image of the number-plate of the accident-inflicted vehicle and send it across the database server ( back-end ). As the image is sent, the G.P.S information of the location of the accident site is also sent along.
 
The back-end maintains a database of the registration numbers of all the vehicles. On receiving the image, an image-recognition algorithm determines the registration number from the image.
 
This registration number is now run as the key of a DBMS query on the server and the corresponding information is obtained.
 
Using the queried information, the contact information family-members of the vehicle-owner
is obtained.
 
The concerned authorities ie. the Police, the nearest Medical Hospitals and the family-members of the vehicle-owner are intimated about the accident and using the GPS information, they can pinpoint the exact location.
 
During the entire process, neither the local authorities nor the family-members of the vehicle-owner can obtain any information of the informer and this good deed is done anonymously.
 
 Any suggestions will be appreciated.
