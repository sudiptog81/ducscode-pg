function display() {
  echo "This is a display function. Called with argument? $1";
  ls -al $1;

}

display $1
