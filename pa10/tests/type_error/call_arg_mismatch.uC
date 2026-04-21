int foo(int x, int y);

int main() {
	int a;
	float b;
	a = 1;
	b = 2.0;
	a = foo(a, b);
	return 0;
}

int foo(int x, int y) {
	return x + y;
}
