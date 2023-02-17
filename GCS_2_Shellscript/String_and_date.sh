current="$(date +'%d-%m-%Y'-file.txt)"
echo "Today's date "$current
number="file.txt"
while read -r line; do
	echo "$line"
done <$number

