Description: Admin has everything you want

### Deployment

```sh
git clone https://github.com/luisfelipehernandezmora/WAS_Labs_for_students.git
cd admin_or_admin/src
docker build . -t admin
docker run -dp 5000:5000 admin
```

Visit [http://localhost:5000](http://localhost:5000)