from itertools import count, takewhile

is_square=lambda x: int(x**0.5)**2==x

if __name__ == '__main__':
	N=1
	for i in range(N):
		for a in count(6):
			a_square=a**2
			for f in (f for f in takewhile(lambda f: f < a, count(4)) if is_square(a_square-f**2)):
				f_sqaure=f**2
				c_square=a_square-f_sqaure
				setoff= 3 if f&1 else 2
				for e in (e for e in takewhile(lambda e: e**2<c_square, count(setoff, 2)) if is_square(c_square-e**2) and is_square(a_square-e**2)):
					e_square=e**2
					b_square=c_square-e_square
					d_square=a_square-e_square
					z=-(d_square - c_square) //2
					y=-(-d_square - c_square + 2*b_square) // 2
					x=(d_square + c_square) // 2
					print (x,y,z)