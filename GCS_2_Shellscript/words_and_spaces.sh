echo "Enter any sentence"
read text
word=$(echo -n"$text" | wc -w)
echo "The number of words is "$word
spaces=$(expr length "$text" - length `echo "$text" | sed "s/ //g"`)
echo "The number of white spaces is "$spaces
