# perchat
persona-chat collection webtool<br>
<img src="https://raw.githubusercontent.com/kyoshiro-s/perchat/images/logo.png" width="256px">


# requirements
* python (>=3.6)
* redis (>=2.6)

# setup
```sh
git clone https://github.com/kyoshiro-s/perchat.git
cd perchat
pip install -r requirments.txt
python manage.py makemigrations chat
python manage.py migrate
python manage.py createsuperuser
```

# usage
```sh
redis-server >/dev/null &
python manage.py runserver
# (if you want to access from another machine)
python manage.py runserver 0:8000
```
then access to [localhost:8000/chat/](http://localhost:8000/chat/)
