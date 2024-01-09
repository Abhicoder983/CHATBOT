echo "BUILD START"
python3.9 -m pip install -r requirement.txt
pyhton3.9 manage.py collectdstatic --noinput --clear
echo "BUILD END"