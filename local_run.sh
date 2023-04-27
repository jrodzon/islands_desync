number_of_migrants=5
migration_interval=5
dda=$(date +%y%m%d)
tta=$(date +g%H%M%S)
tmpdir=" "

#cd islands_desync

export PYTHONPATH="${PYTHONPATH}:$PWD"

python3 -u ./islands_desync/start.py 10 $tmpdir $number_of_migrants $migration_interval $dda $tta