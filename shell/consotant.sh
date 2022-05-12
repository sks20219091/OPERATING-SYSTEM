vowel=[aeiouAEIOU]
echo "Enter the string"
read string
i=0
len=${#string}
vowelcount=0
n=$((len-1))
while [ $i -le $n ]
do
	curr="${string:$i:1}"
	if [[ $curr =~ $vowel ]]
	then
		vowelcount=$((vowelcount+1))
	fi
	i=$((i+1))
done 
echo "The no. of vowel is $vowelcount"
cosnonantcount=$((len-vowelcount))
echo "The number of consonant in $string is $cosnonantcount"
		

