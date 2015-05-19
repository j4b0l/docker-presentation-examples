function j4_example {
	if [ -z "$1" ]; then
		echo "USAGE: $0 <line_number>"
	else
		EXAMPLE=$(cat .meta/j4_examples|grep -A1 "^example $1:$"|grep -v "^example $1:$")
		echo $EXAMPLE
	fi
}

alias j4_ps="watch 'docker ps -a|head -3'"
