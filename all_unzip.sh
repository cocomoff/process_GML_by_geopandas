# 北海道 1 から沖縄 47 まで解凍する

cd download;

for n in `seq 1 9`;
do
    unzip N03-20210101_0${n}_GML.zip
done

for n in `seq 10 47`;
do
    unzip N03-20210101_${n}_GML.zip
done

cd ../
