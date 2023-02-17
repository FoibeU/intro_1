Num=$(($RANDOM))
echo "The first random number generated is :"$Num
square_Root=$(echo "$Num" |awk '{print sqrt($1)}')
echo "The square root is: $square_Root"
Number2=$(($RANDOM))
echo "The second random number generated "$Number2
Square_root2=$(echo "$Number2" | awk '{print sqrt($1)}')
echo "The square root  is : $Square_root2"
add=$(echo "$square_Root + $Square_root2" | bc)
echo "The sum of their square roots is" $add
