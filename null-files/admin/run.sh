cd admin

#bash example of connecting to service
curl $(echo $CI_REGISTRY_IMAGE | sed "s/\//-/g")

python3 solve.py
