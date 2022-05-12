v=[aeiouAEIOU]
echo "Enter the string "
read string
i=0
vowelno=0
len=${#string}
n=$((len-1))
while [ $i -le $n ]
do
	curr="${string:$i:1}"
	if [[ $curr =~ $v ]]
	then
		vowelno=$((vowelno+1))	
	fi
	i=$((i+1))
done
echo "The number of vowel in $string is $vowelno "
