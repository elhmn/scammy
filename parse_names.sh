# cat names.txt | tr -s "\t" ";" | sed 's/[0-9]//g; s/^;//g; s/;/ /g' > names_test.txt
