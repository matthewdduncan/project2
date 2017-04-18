#!/bin/bash
rm outfile
rm interfile

for filename in dirtree/*/*/*.tbl; do
 op=`cat $filename | head -3 | tail -1 |cut -f4`
 dn=`echo $filename | cut -d$'/' -f3`

 echo -e "$dn \t $op" >> interfile
done

sort -k2nr -k1 interfile >> outfile
