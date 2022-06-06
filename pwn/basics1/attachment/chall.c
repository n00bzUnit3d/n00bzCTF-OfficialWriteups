// gcc -no-pie -fno-stack-protector chall.c -o chall
#include <stdio.h>
int main() {
	setup();
	char welcome[71] = "Welcome to the challenge series of basic and intermidate pwn! Good luck";
	printf("%s\n",welcome);
	char buf[50];
	fgets(buf,0x100,stdin);
	return 0;
}
void win() {
	system("sh");
}
void setup() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
}
