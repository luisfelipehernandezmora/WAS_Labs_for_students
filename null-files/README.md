Description: ha! you got me last time, now i dare you to try to hack me again hacker ;)

### Deployment

```sh
git clone https://github.com/luisfelipehernandezmora/WAS_Labs_for_students.git
cd null-files
docker build . -t null
docker run -dp 5000:80 null
```

Visit [http://localhost](http://localhost)

