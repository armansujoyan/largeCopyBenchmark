#!/usr/bin/env bash
amount=${1?Error: no amount given}
bytesize=${2?Error: no bytesize given}
to=${3?Error: no destination specified}

intReg="^[0-9]+$";

cd $to

if ! [[ $amount =~ intReg && $bytesize =~ intReg ]]
    then
        echo "Invalid input"
fi

for ((n=0; n<amount; n++))
do
    dd if=/dev/urandom of=file$( printf %03d "$n" ).bin bs=$bytesize count=$(( RANDOM + 1024 ))
done

echo $amount files written to folder $to. Total size is $(du -sh)