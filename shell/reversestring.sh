echo "Enter the string "
read string
rev=""
len=${#string}
n=$((len-1))
while [ $n -ge 0 ]
do
	rev="$rev${string:$n:1}"
	n=$((n-1))
done
echo "The length of string is $len & reverse string is $rev "
