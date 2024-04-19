#curl --head -s $1 | grep Location | cut -d ' ' -f2

#curl -ILs $1 | grep -i "Location" | cut -d ' ' -f2


curl -s $1 | grep "href" | cut -d'"' -f2