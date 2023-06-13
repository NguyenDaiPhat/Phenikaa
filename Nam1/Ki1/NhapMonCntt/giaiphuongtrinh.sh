#!/bin/bash
echo "'''"
delta=$(( $2 * $2 - 4 * $1 * $3 ))
if [ $1 -eq 0 ] && [ $2 -ne 0 ]; then	
	echo "  Phuong trinh co mot nghiem:"
	echo "  > x=$(echo " scale=2 ; -1*$3/$2 " | bc )"
elif [ $1 -eq 0 ] && [ $2 -eq 0 ] && [ $3 -ne 0 ]; then  
	echo "  Phuong trinh vo nghiem"
elif [ $1 -eq 0 ] && [ $2 -eq 0 ] && [ $3 -eq 0 ]; then  
	echo "  Phuong trinh vo so nghiem"    
elif [ $1 -ne 0 ] && [ $delta -gt 0 ]; then
	echo "  Phuong trinh co hai nghiem:"
	echo "  > x1=$(echo " scale=2 ; (-1*$2-sqrt($delta))/(2*$1) " | bc )"
	echo "  > x2=$(echo " scale=2 ; (-1*$2+sqrt($delta))/(2*$1) " | bc )"
elif [ $1 -ne 0 ] && [ $delta -eq 0 ]; then
       	echo "  Phuong trinh co mot nghiem:"
	echo "  > x=$(echo " scale=2 ; -1*$2/(2*$1) " | bc )"
elif [ $1 -ne 0 ] && [ $delta -le 0 ]; then
	echo "  Phuong trinh vo nghiem"
fi
echo "'''"

