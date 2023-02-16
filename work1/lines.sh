now="$(date +'%d/%m/%Y')"
echo "Today's date" $now
number="file.txt"
while read -r line; do
        echo "$line"
done <$number
