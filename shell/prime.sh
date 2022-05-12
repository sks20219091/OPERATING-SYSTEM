echo "Enter the number N "
read n
k=2
l=$((n-1))
flag=0
while [ $k -le $l ]
do
	if [ $((n%k)) == 0 ]
	then
		flag=1
		break
	fi
	k=$((k+1))
done
if [ $flag == 0 ]
then
	echo "Number $n is prime no."
else
	echo "Number $n is not prime no."
fi

		 
