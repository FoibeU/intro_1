echo "Enter any sentence"
read text
word=$(echo -n"$text" | wc -w)
echo "The numbers of words is "$word
spaces=$(expr length "$text" - length `echo "$text" | sed "s/ //g"`)
echo "the numbers of spaces is "$spaces
