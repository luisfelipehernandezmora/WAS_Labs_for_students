challenge_name:-
Secure Vault

description:-
This is my vault. Try to hack into it. I bett!! you can't!
I think u might wanna look at page source **Frequently**

Try to get the flag, which is the password of one of the users. You will know is the flag, as it says flag, and is the password of the hacker user ;)

navigate to 

cd Securevault/admin 

sudo docker build . -t securev
sudo docker run -dp 5001:9000 securev

Go and visit the localhost!

hint:-
- Do you know about information_schema database???

Try to find the details on the database, you might use SQL commands such as 

provided in this website https://stackoverflow.com/questions/8334493/get-table-names-using-select-statement-in-mysql

SELECT table_name FROM information_schema.tables
WHERE table_schema = database();

to get the name of the tables, and you can get the name of the columns, using PortSwigger. 

Also inspect the SQL function Group_concat(), so it will give you all the values, and not only the first one available in the database 

Remember also to comment your SQL commands with --