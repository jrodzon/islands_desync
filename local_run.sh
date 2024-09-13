islands_count=4
number_of_migrants=5
migration_interval=35
dda=$(date +%y%m%d)
tta=$(date +g%H%M%S)
tmpdir="/tmp/ray"
if [ -z "$1" ]
  then
    sequence_lenght=10
else
    sequence_lenght=$1
fi


export RAY_DEDUP_LOGS=0

export PYTHONPATH="${PYTHONPATH}:$PWD"

python3 -u ./islands_desync/start.py $islands_count \
$tmpdir $number_of_migrants $migration_interval $dda $tta $sequence_lenght
