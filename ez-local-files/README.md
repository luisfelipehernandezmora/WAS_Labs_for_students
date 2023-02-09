Description: I heard using local files is not secure can you find out why?

Try to get the etc/passwd file!

Try to get the flag! (it will in 'flag{YOUR FLAG GOES HERE}')


### Deployment

```sh
git clone https://github.com/luisfelipehernandezmora/WAS_Labs_for_students.git
cd mwade-challenges/ez-local-files
sudo docker build . -t ez-local-files
sudo docker run -dp 80:80 ez-local-files
```
Visit [http://localhost](http://localhost)

If you have alrady something running in port 80, 

you can change the command : docker run -dp 80:80 ez-local-files

you can try another port like 5000 or 5050 (or anyone!)

to 

docker run -dp 5000:80 ez-local-files
or
docker run -dp 5050:80 ez-local-files
or
docker run -dp (your port here!):80 ez-local-files

and will be 

http://localhost:5000
or
http://localhost:5050
or
http://localhost:(your port here)
