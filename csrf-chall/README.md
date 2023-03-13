# Simple Forgery

## Description



## Short Writeup

* XSS on post
* CSRF using XSS to make admin give access to his post

You can see other users by changing the username in the URL as;
http://localhost:5000/home/{user_name} (I used port 5000 but you can use any)

So if you create several users: Mike and Mary. And logged in as Mike make a post, you can share access to Mary. When logged in as Mary, you can go to http://localhost:5000/home/Mike  and see his post (the one that you got permission).

In this case the admin, is a normal user, that needs to receive permission from you to see your post. Take this into account.

You can get the admin's post id by navigating to http://localhost:5000/home/admin

## Flag



## Launch Challenge

```
sudo docker build . -t csrf-chall
sudo docker run -p 5000:5000 csrf-chall
```

## Challenge Author

**[sk4d00.sh](https://twitter.com/RahulSundar8)**

