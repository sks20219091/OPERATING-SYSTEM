echo "Enter the string "
read string
n=${#string}
rev=""
while [ $n -ge 0 ]
do
	rev="$rev${string:$n:1}"
	n=$((n-1))
done
echo $rev
if [ $string == $rev ]
then
	echo "The string is palindrome " 
else 
	echo "The strig is not a palindrome"
fi
