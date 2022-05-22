rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py migrate --run-syncdb
echo ''
echo ''
echo ''
echo ''
echo ''
echo ''
echo 'so you fucked up, eh?'
