int foo(int x, int y);

int main() {
	int a;
	a = 1;
	a = foo(a);
	return 0;
}

int foo(int x, int y) {
	return x + y;
}
