/* symbolic-link.c */

#include <stdio.h>

#include<unistd.h>

#include <string.h>

int main(int argc, char * argv[])

{

unlink(argv[1]);

symlink("./passwd",argv[1]);

}