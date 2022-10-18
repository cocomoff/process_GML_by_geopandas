# 北海道 1 から沖縄 47 までダウンロードする

for n in `seq 1 9`;
do
  wget -P download https://nlftp.mlit.go.jp/ksj/gml/data/N03/N03-2021/N03-20210101_0${n}_GML.zip
done

for n in `seq 10 47`;
do
  wget -P download https://nlftp.mlit.go.jp/ksj/gml/data/N03/N03-2021/N03-20210101_${n}_GML.zip
done
